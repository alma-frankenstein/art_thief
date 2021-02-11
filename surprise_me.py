import random
import logging
import sys
from save_pic import save_pic
from urllib.parse import urljoin
from format_url import get_source, parse_source_code, image_json
# from main import bcolors
from loggers import surprise_me_logger

# # logging.basicConfig(level=logging.INFO)

# surprise_me_logger = logging.getLogger(__name__)
# # high_alert_logger = logging.getLogger("We found a BIG ONE!")

# surprise_handler = logging.StreamHandler(sys.stdout)  # to console 
# hq_formatter = logging.Formatter(bcolors.OKBLUE + '%(name)-12s: %(levelname)-8s %(message)s' + bcolors.ENDC)  # custom format to add to handler
# surprise_handler.setFormatter(hq_formatter)

# surprise_me_logger.addHandler(surprise_handler)  # add handler to logger
# surprise_me_logger.propagate = False


# surprise_me_logger.setLevel(logging.DEBUG)
# # high_alert_logger.setLevel(logging.DEBUG)


def get_collections(parsed_html, substring):
    collection_hrefs = []
    for link in parsed_html.find_all('a'):
        if substring in str(link):
            collection_hrefs.append(link.get('href'))
    return collection_hrefs


def filter_collections() -> list:
    source_string = get_source("https://www.artsy.net/")
    the_soup = parse_source_code(source_string)
    all_collections = get_collections(the_soup, "collection") 
    filtered_collections = list(set(x for x in all_collections if "http" not in x))   # remove https://www.artsy.net/collection/textured-histories', 'https://www.artsy.net/collections'
    return filtered_collections


def rand_collection_href(collections):
    collection_href = random.choice(collections)
    # logging.info(f"collection_href: {collection_href}")
    return collection_href


def random_picture_in_collection(collection_href):    
    collection_url = urljoin("https://www.artsy.net", collection_href)
    # logging.info(f"Fetching from collection url: {collection_url}") 
    collection_json = image_json(collection_url)
    artist_images = collection_json[0][1]["json"]["data"]["collection"]["artworksConnection"]["edges"]
    possible_images = len(artist_images)   
    image_index = random.randint(0, possible_images - 1)   # -1 because randint is inclusive
    rando_pic_href = artist_images[image_index]["node"]["href"]   # ex. /artwork/mindy-cherri-wwjd
    # logging.info(f"random picture href: {rando_pic_href}")
    rando_url = urljoin("https://www.artsy.net", rando_pic_href)
    # logging.info(f"random url: {rando_url}")
    surprise_me_logger.info(f"random url: {rando_url}")
    save_pic(rando_url)


def get_random_picture():
    filtered_collections = filter_collections()
    collection_href = rand_collection_href(filtered_collections)
    random_picture_in_collection(collection_href)
    

for _ in range(40):
    get_random_picture()

# random_picture_in_collection('collection/post-war')

get_random_picture()