""" Pull specific information (artist info, url for dztiles, related images)
    from the jsonified Bootstrap section of the source code """

import logging
import random
from typing import Optional
from urllib.parse import urljoin


def dztiles_url(json_bootstrap: dict) -> Optional[str]:
    """ ex: 'https://d32dm0rphc51dk.cloudfront.net/dFyhynkSypHRoFpJsyj0pg/dztiles/' """
    deep_zoom_data = json_bootstrap[0][1]["json"]["data"]["artwork"]["images"][0]["deepZoom"]
    if deep_zoom_data is not None:
        jpeg_url = deep_zoom_data["Image"]["Url"]
        # reassigned before calling in save_pic()
        dz_url = urljoin(jpeg_url, "14/{}_{}.jpg")
        logging.info(f"high resolution url: {dz_url}")
        return dz_url


def artist_and_title(json_bootstrap):
    """ example return value: 'Fix (2019) by Jeremy Okai Davis' """
    piece_info = (json_bootstrap[0][1]["json"]["data"]
                  ["artwork"]["meta"]["title"]).split("|")

    # Ex. David Wojnarowicz
    artist_name = piece_info[0].strip()

    # Ex. Untitled (Face in Dirt), 1991
    title_and_year = piece_info[1].strip()

    return f"{title_and_year} by {artist_name}"


def related_image_url(json_bootstrap):
    """ Get a random image similar to a given image """
    related_images = json_bootstrap[0][1]["json"]["data"]["artwork"]["layer"]["artworksConnection"]["edges"]
    num_possible_related = len(related_images)
    # -1 because randint is inclusive
    image_index = random.randint(0, num_possible_related - 1)
    related_image_href = related_images[image_index]["node"]["href"]
    return urljoin("https://www.artsy.net", related_image_href)