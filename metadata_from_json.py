from typing import Optional
from urllib.parse import urljoin
import logging
import random



def dztiles_url(json_bootstrap: dict) -> Optional[str]:
    """ ex: 'https://d32dm0rphc51dk.cloudfront.net/dFyhynkSypHRoFpJsyj0pg/dztiles/' """
    deep_zoom_data = json_bootstrap[0][1]["json"]["data"]["artwork"]["images"][0]["deepZoom"]
    if deep_zoom_data is not None:
        jpeg_url = deep_zoom_data["Image"]["Url"]
        dz_url = urljoin(jpeg_url, "14/{}_{}.jpg")  # reassigned before calling in save_pic()
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
    related_images = json_bootstrap[0][1]["json"]["data"]["artwork"]["layer"]["artworksConnection"]["edges"]
    num_possible_related = len(related_images)  
    image_index = random.randint(0, num_possible_related - 1)   # -1 because randint is inclusive
    related_image_href = related_images[image_index]["node"]["href"]
    next_image_url = urljoin("https://www.artsy.net", related_image_href)
    return next_image_url