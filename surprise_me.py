import random
import logging
from save_pic import save_pic
from urllib.parse import urljoin
from format_url import get_source, parse_source_code, image_json


def get_collections(parsed_html, substring):
    collection_hrefs = []
    for link in parsed_html.find_all('a'):
        if substring in str(link):
            collection_hrefs.append(link.get('href'))
    return collection_hrefs


source_string = get_source("https://www.artsy.net/")
the_soup = parse_source_code(source_string)

all_collections = get_collections(the_soup, "collection") 
filtered_collections = list(filter(lambda x: "http" not in x, all_collections))  # remove https://www.artsy.net/collection/textured-histories', 'https://www.artsy.net/collections'


def rand_collection(collections):
    collection_href = random.choice(collections)
    logging.info(f"collection_href: {collection_href}")
    return collection_href
    
random_collection_href = rand_collection(all_collections)

(the_soup, "RELAY")
collection_url = urljoin("https://www.artsy.net", random_collection_href) 

collection_json = image_json(collection_url)
image_index = random.randint(0, 9)  # TODO make range num of possible images
rando_pic_href = (collection_json[0][1]["json"]["data"]["collection"]["artworksConnection"]["edges"][image_index]["node"]["href"])  # ex. /artwork/mindy-cherri-wwjd

rando_url = urljoin("https://www.artsy.net", rando_pic_href)
logging.info(f"random url: {rando_url}")
save_pic(rando_url)

