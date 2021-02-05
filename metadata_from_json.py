from typing import Optional
from urllib.parse import urljoin
import logging
import random

def get_dz_num(width, height):
    if width < height:
        smaller_dim = width
    else:
        smaller_dim = height
    
    if smaller_dim <= 512:
        dz_num = "9/{}_{}.jpg"
    elif smaller_dim <= 1024:
        dz_num = "10/{}_{}.jpg"  # guessing here
    elif smaller_dim <= 1536:
        dz_num = "11/{}_{}.jpg"
    else:
        dz_num = "12/{}_{}.jpg"
    return dz_num
    

def dztiles_url(json_bootstrap: dict) -> Optional[str]:
    """ ex: 'https://d32dm0rphc51dk.cloudfront.net/dFyhynkSypHRoFpJsyj0pg/dztiles/' """
    deep_zoom_data = json_bootstrap[0][1]["json"]["data"]["artwork"]["images"][0]["deepZoom"]
    # width = deep_zoom_data["Image"]["Size"]["Width"]
    # height = deep_zoom_data["Image"]["Size"]["Height"]

    if deep_zoom_data is not None:
        width = deep_zoom_data["Image"]["Size"]["Width"]
        height = deep_zoom_data["Image"]["Size"]["Height"]
        jpeg_url = deep_zoom_data["Image"]["Url"]
        dz_num = get_dz_num(width, height)
        dz_url = urljoin(jpeg_url, dz_num)
        logging.info(f"high resolution url: {dz_url}")
        return dz_url


def artist_and_title(json_bootstrap):
    piece_info = (json_bootstrap[0][1]["json"]["data"]["artwork"]["meta"]["title"]).split("|")
    
    # Ex. David Wojnarowicz
    artist_name = piece_info[0].strip()

    # Ex. Untitled (Face in Dirt), 1991/2018
    title_and_year = piece_info[1].strip()
    
    title_artist =  f"{title_and_year} by {artist_name}"
    return title_artist
        
        
def related_image_url(json_bootstrap):
    image_index = random.randint(0, 7)  # make range num of possible images
    related_image_href = json_bootstrap[0][1]["json"]["data"]["artwork"]["layer"]["artworksConnection"]["edges"][image_index]["node"]["href"] # [0] after ["edges"] is the first related image
    next_image_url = urljoin("https://www.artsy.net", related_image_href)
    return next_image_url