""" Find the dimensions of an image, then get each tile and paste it onto a blank canvas """
from io import BytesIO
from typing import Tuple

import requests
from PIL import Image

from src.core.loggers import get_tiles_logger

TILE_MAX_RANGE = 20
TILE_SIZE = 512


def get_tiles_and_build_img(dz_url) -> Image:
    """
    Retreive image pieces and return a cropped completed image

    Args:
        dz_url:  The template string for the image tiles.
        example: 'https://d32dm0rphc51dk.cloudfront.net/dFyhynkSypHRoFpJsyj0pg/dztiles/14/{}_{}.jpg'
    Returns:
        The completed Image file from those pieces.

    """
    width_counter, actual_width = find_max_width(dz_url)
    height_counter, actual_height = find_max_height(dz_url)
    uncropped_img = get_tiles(dz_url, width_counter, height_counter)
    return crop(uncropped_img, actual_width, actual_height)


def paste_on_canvas(canvas, x, y, tile_data):
    """ Put each fetched tile in its proper place on the blank canvas """
    image = Image.open(BytesIO(tile_data))
    canvas.paste(image, (TILE_SIZE * x, TILE_SIZE * y))


def replace_slashes(stem):
    """ Replace '/' with 'slash' so the artwork title can be used as a file name """
    return stem.replace("/", "slash")


def crop(an_img: Image, actual_w: int, actual_h: int) -> Image:
    """ Trim blank margins from the image canvas"""
    return an_img.crop((0, 0, actual_w, actual_h))


def find_max_width(dz_url) -> Tuple[int, int]:
    """ Return image width """
    return _find_max_dimension(dz_url, TILE_MAX_RANGE, find_width=True)


def find_max_height(dz_url) -> Tuple[int, int]:
    """ Return image height """
    return _find_max_dimension(dz_url, TILE_MAX_RANGE, find_width=False)


def _find_max_dimension(dz_url, max_range, find_width: bool = True) -> Tuple[int, int]:
    """ Traverse top row and left column to find image dimensions """
    root_url = dz_url
    actual_size = 0
    for dim in range(max_range):
        row_index, column_index = 0, dim
        if find_width:
            column_index, row_index = row_index, column_index
        tile_request = requests.get(root_url.format(row_index, column_index))
        if tile_request.ok:
            tile = Image.open(BytesIO(tile_request.content))
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


def get_tiles(dz_url: str, w_counter: int, h_counter: int) -> Image:
    """ Excludes first row and column, which should be fetched with _find_max_dimension() """
    new_image = Image.new('RGB', (TILE_SIZE * TILE_MAX_RANGE, TILE_SIZE * TILE_MAX_RANGE))

    for i in range(w_counter):
        for j in range(h_counter):
            get_tiles_logger.debug(f"fetching {dz_url.format(i, j)} ...")
            response = requests.get(dz_url.format(i, j))
            paste_on_canvas(canvas=new_image, x=i, y=j, tile_data=response.content)

    return new_image
