""" Sequence of functions required to take an artsy url
(ex. 'https://www.artsy.net/artwork/jeremy-okai-davis-fix') and get just the necessary JSON.
These are the preliminary steps before pulling out metadata about the piece of art. """

import json

from bs4 import BeautifulSoup

import requests


def get_source(url):
    """ Get source contents from a webpage """
    source = requests.get(url)
    return source.content


def parse_source_code(source_string):
    """ Take a string of source code, return it as parsed html """
    with open('source_code.html', 'wb') as file_obj:
        file_obj.write(source_string)

    with open('source_code.html') as file_obj:
        soup = BeautifulSoup(file_obj, 'html.parser')
    return soup


def json_bootstrap(parsed_html, substring):
    """ Pull the relevant code from the parsed html, return it as a json object """
    for block in parsed_html.find_all('script'):
        if substring in str(block):
            bootstrap_string = block.string.strip()
            bootstrap_string = bootstrap_string.replace(
                "var __RELAY_BOOTSTRAP__ = ", "")
            bootstrap_string = bootstrap_string[:-1]
            bootstrap_json = json.loads(json.loads(bootstrap_string))
            # with open('output.json', 'w') as f:
            #     f.write(json.dumps(bootstrap_json, indent=4))    # only need one of these
            return bootstrap_json


def image_json(artsy_url):
    """ String together steps to get, parse, and jsonify source code """
    source_string = get_source(artsy_url)
    the_soup = parse_source_code(source_string)
    return json_bootstrap(the_soup, "RELAY")
