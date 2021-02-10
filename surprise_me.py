import random
import logging
from save_pic import save_pic
from urllib.parse import urljoin
from format_url import get_source, parse_source_code, image_json
from pprint import pprint

def get_collections(parsed_html, substring):
    collection_hrefs = []
    for link in parsed_html.find_all('a'):
        if substring in str(link):
            collection_hrefs.append(link.get('href'))
    # pprint(collection_hrefs)
    return collection_hrefs


def filter_collections():
    source_string = get_source("https://www.artsy.net/")
    the_soup = parse_source_code(source_string)
    all_collections = get_collections(the_soup, "collection") 
    filtered_collections = list(filter(lambda x: "http" not in x, all_collections))  # remove https://www.artsy.net/collection/textured-histories', 'https://www.artsy.net/collections'
    return filtered_collections


def rand_collection_href(collections):
    collection_href = random.choice(collections)
    logging.info(f"collection_href: {collection_href}")
    return collection_href


def random_picture_in_collection(collection_href):    
    collection_url = urljoin("https://www.artsy.net", collection_href) 
    collection_json = image_json(collection_url)
    artist_images = collection_json[0][1]["json"]["data"]["collection"]["artworksConnection"]["edges"]
    possible_images = len(artist_images)   
    image_index = random.randint(0, possible_images - 1)   # -1 because randint is inclusive
    rando_pic_href = artist_images[image_index]["node"]["href"]   # ex. /artwork/mindy-cherri-wwjd
    # logging.info(f"random picture href: {rando_pic_href}")
    rando_url = urljoin("https://www.artsy.net", rando_pic_href)
    logging.info(f"random url: {rando_url}")
    save_pic(rando_url)


def get_random_picture():
    filtered_collections = filter_collections()
    collection_href = rand_collection_href(filtered_collections)
    random_picture_in_collection(collection_href)
    
# get_random_picture()