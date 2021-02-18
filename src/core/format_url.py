""" Sequence of functions required to take an artsy url
(ex. 'https://www.artsy.net/artwork/jeremy-okai-davis-fix') and get just the necessary JSON.
These are the preliminary steps before pulling out metadata about the piece of art. """

import json

import requests

from typing import Optional
from bs4 import BeautifulSoup


def get_json_bootstrap(parsed_html: BeautifulSoup, substring: str, save_locally: bool = False) -> Optional[dict]:
    """ Pull the relevant code from the parsed html, return it as a json object """
    for block in parsed_html.find_all('script'):
        if substring in str(block):
            bootstrap_string = block.string.strip()
            bootstrap_string = bootstrap_string.replace("var __RELAY_BOOTSTRAP__ = ", "")
            bootstrap_string = bootstrap_string[:-1]
            bootstrap_json = json.loads(json.loads(bootstrap_string))
            if save_locally:
                with open('output.json', 'w') as f:
                    f.write(json.dumps(bootstrap_json, indent=4))  # only need one of these
            return bootstrap_json


def get_image_json(artsy_url):
    """ String together steps to get, parse, and jsonify source code """
    r = requests.get(artsy_url)
    the_soup = BeautifulSoup(r.content, 'html.parser')
    return get_json_bootstrap(the_soup, "__RELAY_BOOTSTRAP__")
