""" A sequence of functions to get a random art image from artsy.net """
import random
from typing import Tuple
from urllib.parse import urljoin

from PIL.Image import Image

from src.core.format_url import get_image_json, get_source, parse_source_code
from src.core.loggers import surprise_me_logger
from src.core.get_and_save_pic import get_artist_title_from_artsy_url, get_image_from_artsy, save_pic


def get_collections(parsed_html, substring):
    """ Returns a list of all hrefs for artsy's collections pages """
    collection_hrefs = []
    for link in parsed_html.find_all('a'):
        if substring in str(link):
            collection_hrefs.append(link.get('href'))
    return collection_hrefs


def filter_collections() -> list:
    """ Remove exceptions '/collection/textured-histories' and '/collections' from
    list of collections"""
    source_string = get_source("https://www.artsy.net/")
    the_soup = parse_source_code(source_string)
    all_collections = get_collections(the_soup, "collection")
    filtered_collections = list(set(x for x in all_collections if "http" not in x))
    return filtered_collections


def rand_collection_href(collections):
    """ Randomly choose a collection href from the list of all possible """
    return random.choice(collections)


def random_picture_in_collection(collection_href: str) -> str:
    """ Returns the url for a randomly chosen piece of art in a collection,
    ex. 'https://www.artsy.net/artwork/jeremy-okai-davis-model-and-charm' """
    collection_url = urljoin("https://www.artsy.net", collection_href)
    collection_json = get_image_json(collection_url)
    artist_images = collection_json[0][1]["json"]["data"]["collection"]["artworksConnection"]["edges"]
    possible_images = len(artist_images)
    image_index = random.randint(0, possible_images - 1)
    rando_pic_href = artist_images[image_index]["node"]["href"]  # ex. /artwork/mindy-cherri-wwjd
    rando_url = urljoin("https://www.artsy.net", rando_pic_href)
    surprise_me_logger.info(f"random url: {rando_url}")
    return rando_url


def get_random_picture() -> Tuple[Image, str]:
    """ Chain together functions to get a random image, with its title and artist, from artsy.net """
    filtered_collections = filter_collections()
    collection_href = rand_collection_href(filtered_collections)
    some_url = random_picture_in_collection(collection_href)
    img = get_image_from_artsy(some_url)
    title_artist = get_artist_title_from_artsy_url(some_url)
    return img, title_artist


if __name__ == '__main__':
    save_pic(*get_random_picture())
