from io import BytesIO
import requests
from PIL import Image
import logging
from pathlib import Path
import re
from typing import Tuple
from loggers import get_tiles_logger


TILE_MAX_RANGE = 10
TILE_SIZE = 512

# TODO It should be safe to assume the first tile is enough to determine the maximum TILE_SIZE.
#   If the image creation could be delayed until after the first tile is fetched we wouldn't need TILE_SIZE
new_image = Image.new(
    'RGB', (TILE_SIZE * TILE_MAX_RANGE, TILE_SIZE * TILE_MAX_RANGE))


def get_tiles_and_save(dz_url, title_artist):
    width_counter, actual_width = find_max_width(dz_url)
    height_counter, actual_height = find_max_height(dz_url)
    get_tiles(dz_url, width_counter, height_counter)
    # print(f"Image size computed at: {actual_width}x{actual_height} (NOT {new_image.size})")
    try:
        crop_and_save(actual_width, actual_height, title_artist)
    except SystemError:
        get_tiles_logger.info("Wrong dztile number, unable to save image!")
        return False
    return True

def paste_on_canvas(i, j, image_data):
    im = Image.open(BytesIO(image_data))
    new_image.paste(im, (TILE_SIZE * i, TILE_SIZE * j))
    # print(f"Fetching image {i}_{j}.jpg")
    
    
def remove_special(stem):
    stem = re.sub(r"[^a-zA-Z0-9]+", ' ', stem)
    return stem


def crop_and_save(actual_w, actual_h, title_artist):
    cropped_image = new_image.crop((0, 0, actual_w, actual_h))
    title_artist = remove_special(title_artist)
    p = Path.cwd().joinpath("saved_images", f"{title_artist}.jpg")
    cropped_image.save(p)


def find_max_width(dz_url) -> Tuple[int, int]:
    return _find_max_dimension(dz_url, TILE_MAX_RANGE, find_width=True)


def find_max_height(dz_url) -> Tuple[int, int]:
    return _find_max_dimension(dz_url, TILE_MAX_RANGE, find_width=False)


def _find_max_dimension(dz_url, max_range, find_width: bool = True) -> Tuple[int, int]:
    root_url = dz_url
    actual_size = 0
    for dim in range(max_range):
        x, y = 0, dim
        if find_width:
            y, x = x, y
        r = requests.get(root_url.format(x, y))
        if r.ok:
            im = Image.open(BytesIO(r.content))
            width, height = im.size
            paste_on_canvas(x, y, r.content)
            if find_width:
                actual_size += width
            else:
                actual_size += height
        else:
            return dim, actual_size
    print("WARNING:  Image boundary not found.  This may only be part of it!")
    get_tiles_logger.info(f"Max dim found: {dim}")
    return dim + 1, actual_size


def get_tiles(dz_url, w_counter, h_counter):
    root_url = dz_url
    for i in range(1, w_counter):
        for j in range(1, h_counter):
            get_tiles_logger.debug(f"fetching {root_url.format(i, j)} ...")
            r = requests.get(root_url.format(i, j))
            paste_on_canvas(i, j, image_data=r.content)



# # TODO Turn the whole thing into a flask app and host it on GH?

