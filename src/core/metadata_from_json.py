""" Pull specific information (artist info, url for dztiles, related images)
    from the jsonified Bootstrap section of the source code """

import logging
import random
from typing import Optional
from urllib.parse import urljoin


def dztiles_url(json_bootstrap: dict) -> Optional[str]:
    """

    Args:
        json_bootstrap: The json that was stored in the __RELAY_BOOTSTRAP__ variable in the artsy.com page data

    Returns:
        The template string url for the maximum resolution tiles of the image
        ex: 'https://d32dm0rphc51dk.cloudfront.net/dFyhynkSypHRoFpJsyj0pg/dztiles/14/{}_{}.jpg'
    """

    deep_zoom_data = json_bootstrap[0][1]["json"]["data"]["artwork"]["images"][0]["deepZoom"]
    if deep_zoom_data is not None:
        jpeg_url = deep_zoom_data["Image"]["Url"]
        dz_url = urljoin(jpeg_url, "14/{}_{}.jpg")
        logging.info(f"high resolution url: {dz_url}")
        return dz_url


def artist_and_title(json_bootstrap: dict) -> str:
    """
    Args:
        json_bootstrap: The json that was stored in the __RELAY_BOOTSTRAP__ variable in the artsy.com page data

    Returns:
        The Title and Artist info for the image in question.
        ex: 'Fix (2019) by Jeremy Okai Davis'
    """

    piece_info = json_bootstrap[0][1]["json"]["data"]["artwork"]["meta"]["title"].split("|")

    # Ex. David Wojnarowicz
    artist_name = piece_info[0].strip()

    # Ex. Untitled (Face in Dirt), 1991
    title_and_year = piece_info[1].strip()

    return f"{title_and_year} by {artist_name}"


def related_image_url(json_bootstrap):
    """
    Get a random image similar to a given image

    Args:
        json_bootstrap: The json that was stored in the __RELAY_BOOTSTRAP__ variable in the artsy.com page data

    Returns:
        The base url for another image related to the json_bootstrap data
        ex: 'https://www.artsy.net/artwork/joshua-goode-pop-culture-bronze-sculpture-sabart-toothed-cat'
    """
    related_images = json_bootstrap[0][1]["json"]["data"]["artwork"]["layer"]["artworksConnection"]["edges"]
    num_possible_related = len(related_images)
    image_index = random.randint(0, num_possible_related - 1)
    related_image_href = related_images[image_index]["node"]["href"]
    return urljoin("https://www.artsy.net", related_image_href)
