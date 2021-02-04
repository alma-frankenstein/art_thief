import logging
from metadata_from_json import dztiles_url, artist_and_title
from format_url import image_json
from main import fabulous_picture


def save_pic(artsy_url):
    bootstrap = image_json(artsy_url)
    jpeg_label = artist_and_title(bootstrap)
    root_url = dztiles_url(bootstrap)
    if root_url:
        try:
            fabulous_picture(root_url, jpeg_label)
        except SystemError as e:
            logging.error(f"attempting to fetch: {artsy_url}")
            logging.error(f"artwork name: {jpeg_label}")
            raise e
    else:
        logging.warning(f"{jpeg_label} has no high resolution version. Skipping")
        
    
# save_pic("https://www.artsy.net/artwork/david-wojnarowicz-arthur-rimbaud-in-new-york-diner-2")
# save_pic("https://www.artsy.net/artwork/bert-stern-pirelli-calendar-by-bert-stern")
# save_pic("https://www.artsy.net/artwork/salvador-dali-madonne")
# save_pic("https://www.artsy.net/artwork/joel-peter-witkin-carrot-cake-number-1")

