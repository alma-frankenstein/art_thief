""" Get images and piece info for artsy.net, with the option to save by title and artist
    in the file tree """

from pathlib import Path
from typing import Optional, Union

from PIL.Image import Image

from src.core.format_url import get_image_json
from src.core.loggers import high_alert_logger, save_pic_logger
from src.core.main import get_tiles_and_build_img, replace_slashes
from src.core.metadata_from_json import artist_and_title, dztiles_url

MAX_DZNUM = 13


def amend_dz_url(root_url: str, dz_num: Union[str, int]) -> str:
    """
    Args:
        root_url: The url for the dztiles image, found when an artsy.net url is passed
        to get_image_from_artsy(). Ex. "https://d32dm0rphc51dk.cloudfront.net/SC4Y7ZKKj6t5c-qPOvSZkg/dztiles/11/0_0.jpg"
        dz_num: An integer to start decrementing from

    Returns: The root_url with the dztiles number decremented once

    """

    if not isinstance(dz_num, int) and not dz_num.isdigit():
        raise ValueError("dz_num must be an integer")
    stem = root_url.rsplit("/", 2)
    stem[-2] = str(dz_num)
    return "/".join(stem)


def get_artist_title_from_artsy_url(artsy_url: str) -> Optional[str]:
    """Takes artsy.net url, returns info about a piece of art"""
    bootstrap = get_image_json(artsy_url)
    return artist_and_title(bootstrap)


def get_image_from_artsy(artsy_url: str) -> Optional[Image]:
    """
    Args:
        artsy_url: String of artsy.net  artwork url, ex. "https://www.artsy.net/artwork/jeremy-okai-davis-model-and-charm"

    Returns: A high-resolution image

    """
    bootstrap = get_image_json(artsy_url)

    root_url = dztiles_url(bootstrap)

    if root_url:
        save_pic_logger.info(f"attempting to fetch: {artsy_url} ...")

        dz_num_counter = MAX_DZNUM
        while dz_num_counter > 8:
            amended_dz_url = amend_dz_url(root_url, dz_num_counter)
            save_pic_logger.info(
                f"dztiles number was too large. Trying {dz_num_counter} as {amended_dz_url.format(0, 0)} ...")
            try:
                img = get_tiles_and_build_img(amended_dz_url)
            except ValueError as e:
                save_pic_logger.debug(f"{dz_num_counter} is too large. Decrementing and trying a lower resolution...")
                dz_num_counter -= 1
                continue
            if dz_num_counter == MAX_DZNUM:
                high_alert_logger.debug(
                    f"This picture is the same size as the maximum tile size we are fetching({MAX_DZNUM})!\
                    It may be time to make it bigger")
            save_pic_logger.info("Successfully assembled picture.")
            return img
    else:
        return None


def save_pic(an_img: Image, title: str) -> Path:
    """
    Save the image with the given title to the local filesystem

    Args:
        an_img: The image object returned from get_image_from_artsy()
        title: String of info about the piece, returned from get_artist_title_from_artsy_url()

    Returns:
        Path to image

    """
    title_artist = replace_slashes(title)
    image_path = Path.cwd().joinpath("src/static", f"{title_artist}.jpg")
    image_path.parent.mkdir(parents=True, exist_ok=True)
    an_img.save(image_path)
    return image_path


if __name__ == '__main__':
    url = "https://www.artsy.net/artwork/jeremy-okai-davis-fix"

    save_pic(get_image_from_artsy(url), get_artist_title_from_artsy_url(url))  # vanilla dz 11
    # save_pic("https://www.artsy.net/artwork/bert-stern-pirelli-calendar-by-bert-stern")  # jpg only, no dz
    # save_pic("https://www.artsy.net/artwork/dapper-bruce-lafitte-no-summercamp")   # dz 13
