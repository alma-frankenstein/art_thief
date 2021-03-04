import json
import logging
import random
from io import BytesIO
from pathlib import Path
from typing import Optional, Tuple
from urllib.parse import urljoin

import requests
from PIL import Image
from bs4 import BeautifulSoup

from src.core.loggers import get_tiles_logger, high_alert_logger, save_pic_logger
from src.corev2.utils import replace_slashes


class ArtsyImage:
    image: Image
    image_json: Optional[dict]

    _tile_width: int
    _tile_height: int

    pixel_width: int
    pixel_height: int

    TILE_MAX_RANGE: int = 20
    TILE_SIZE: int = 512
    MAX_DZNUM: int = 14
    MIN_DZNUM: int = 8

    JSON_VARIABLE_NAME: str = "__RELAY_BOOTSTRAP__"

    def __init__(self, url: str, debug: bool = False):
        self.debug = debug
        self.main_page_url = url
        self.image_json = None
        self.image = Image.new('RGB', (self.TILE_SIZE * self.TILE_MAX_RANGE, self.TILE_SIZE * self.TILE_MAX_RANGE))
        self._get_image_json_data()

        self._tile_width = -1
        self._tile_height = -1

        self.pixel_width = 0
        self.pixel_height = 0
        self._dz_index = self.MAX_DZNUM

    @property
    def artist_and_title(self) -> str:
        """
        Returns:
            The Title and Artist info for the image in question.
            ex: 'Fix (2019) by Jeremy Okai Davis'
        """

        piece_info = self.image_json[0][1]["json"]["data"]["artwork"]["meta"]["title"].split("|")

        # Ex. David Wojnarowicz
        artist_name = piece_info[0].strip()

        # Ex. Untitled (Face in Dirt), 1991
        title_and_year = piece_info[1].strip()

        return f"{title_and_year} by {artist_name}"

    @property
    def dztiles_url(self) -> Optional[str]:
        """
        Returns:
            The template string url for the maximum resolution tiles of the image
            ex: 'https://d32dm0rphc51dk.cloudfront.net/dFyhynkSypHRoFpJsyj0pg/dztiles/14/{}_{}.jpg'
        """

        deep_zoom_data = self.image_json[0][1]["json"]["data"]["artwork"]["images"][0]["deepZoom"]
        if deep_zoom_data is not None:
            jpeg_url = deep_zoom_data["Image"]["Url"]
            dz_url = urljoin(jpeg_url, str(self._dz_index) + "/{}_{}.jpg")
            logging.info(f"high resolution url: {dz_url}")
            return dz_url
        else:
            raise ValueError("No High resolution image available for this image")

    def _get_image_json_data(self):
        """
        Pull the relevant code from the parsed html, return it as a json object
        """
        r = requests.get(self.main_page_url)
        the_soup = BeautifulSoup(r.content, 'html.parser')
        for block in the_soup.find_all('script'):
            if self.JSON_VARIABLE_NAME in str(block):
                bootstrap_string = block.string.strip()
                bootstrap_string = bootstrap_string.replace("var __RELAY_BOOTSTRAP__ = ", "")
                bootstrap_string = bootstrap_string[:-1]
                bootstrap_json = json.loads(json.loads(bootstrap_string))
                if self.debug:
                    with open('output.json', 'w') as f:
                        f.write(json.dumps(bootstrap_json, indent=4))
                self.image_json = bootstrap_json
                break

    def _find_max_width(self):
        """ Set image tile width and pixel width """
        self._tile_width, self.pixel_width = self._find_max_dimension(find_width=True)

    def _find_max_height(self):
        """ Set image tile height and pixel height """
        self._tile_height, self.pixel_height = self._find_max_dimension(find_width=False)

    def _find_max_dimension(self, find_width: bool = True) -> Tuple[int, int]:
        """
        Traverse top row and left column to find image dimensions

        If tiles are found they are added to the final image as they are fetched

        Returns:
            A tuple of the number of tiles and the number of pixels for this image
        """
        actual_size = 0
        for dim in range(self.TILE_MAX_RANGE):
            row_index, column_index = 0, dim
            if find_width:
                column_index, row_index = row_index, column_index
            response = requests.get(self.dztiles_url.format(row_index, column_index))
            if response.ok:
                self._add_tile_to_canvas(x=row_index, y=column_index, tile_data=response.content)
                tile = Image.open(BytesIO(response.content))
                width, height = tile.size
                if find_width:
                    actual_size += width
                else:
                    actual_size += height
            elif actual_size == 0:
                raise ValueError("No tiles found for this url.")
            else:
                return dim, actual_size
        get_tiles_logger.info("WARNING:  Image boundary not found.  This may only be part of it!")
        get_tiles_logger.info(f"Max dim found: {dim}")
        return dim + 1, actual_size

    def _add_tile_to_canvas(self, x: int, y: int, tile_data: bytes):
        """
        Put each fetched tile in its proper place on the blank canvas
        """
        image = Image.open(BytesIO(tile_data))
        self.image.paste(image, (self.TILE_SIZE * x, self.TILE_SIZE * y))

    def _get_tiles(self):
        """
        Fetches remaining tiles for the image

        Excludes first row and column, which should be fetched with _find_max_dimension()

        # TODO Async goes here
        """
        for i in range(1, self._tile_width):
            for j in range(1, self._tile_height):
                get_tiles_logger.debug(f"fetching {self.dztiles_url.format(i, j)} ...")
                response = requests.get(self.dztiles_url.format(i, j))
                self._add_tile_to_canvas(x=i, y=j, tile_data=response.content)

    def _crop(self):
        """
        Crops the image to the computed pixel width
        """
        self.image = self.image.crop((0, 0, self.pixel_width, self.pixel_height))

    def fetch(self):
        """
        Fetch the image data from Artsy
        """
        save_pic_logger.info(f"attempting to fetch: {self.main_page_url} ...")

        dz_num_counter = self.MAX_DZNUM
        while dz_num_counter > self.MIN_DZNUM:
            self._dz_index = dz_num_counter
            save_pic_logger.info(f"dztiles number was too large. Trying {dz_num_counter} as {self.dztiles_url.format(0, 0)} ...")
            try:
                self._find_max_height()
                self._find_max_width()
                self._get_tiles()
                break
            except ValueError as e:
                save_pic_logger.debug(f"{dz_num_counter} is too large. Decrementing and trying a lower resolution...")
                dz_num_counter -= 1
                continue
        if dz_num_counter == self.MAX_DZNUM:
            high_alert_logger.debug(f"This picture is the same size as the maximum tile size we are "
                                    f"fetching({self.MAX_DZNUM})! It may be time to make it bigger")
        self._crop()
        save_pic_logger.info("Successfully assembled picture.")

    def save(self, custom_path: Optional[Path] = None) -> Path:
        """
        Save the image with the given title to the local filesystem
        Returns:
            Final Path to image

        """
        if custom_path:
            image_path = custom_path
        else:
            image_path = Path.cwd().joinpath("src/static", f"{replace_slashes(self.artist_and_title)}.jpg")
            image_path.parent.mkdir(parents=True, exist_ok=True)
        self.image.save(image_path)
        save_pic_logger.info(f"image saved as {image_path}.")
        return image_path

    def get_related_image_url(self) -> str:
        """
        Get a random image similar to a given image from the json metadata

        Returns:
            The base url for another image related to the json_bootstrap data
            ex: 'https://www.artsy.net/artwork/joshua-goode-pop-culture-bronze-sculpture-sabart-toothed-cat'
        """
        related_images = self.image_json[0][1]["json"]["data"]["artwork"]["layer"]["artworksConnection"]["edges"]
        num_possible_related = len(related_images)
        image_index = random.randint(0, num_possible_related - 1)
        related_image_href = related_images[image_index]["node"]["href"]
        return urljoin("https://www.artsy.net", related_image_href)


if __name__ == "__main__":
    x = ArtsyImage("https://www.artsy.net/artwork/jeremy-okai-davis-fix")
    x.fetch()
    x.image.show()
