""" Suite of tests for the metadata_from_json.py module """

import json
from pathlib import Path

from src.core.metadata_from_json import artist_and_title, dztiles_url

from src.tests.example_related_images import related_images
from src.tests.example_urls import ExampleUrls

with open(Path(Path(__file__).resolve().parent, 'example_bootstrap.json'), 'r') as file_obj:
    okai_example_bootstrap = json.load(file_obj)


def test_get_deep_zoom_data():
    """ Test that parsing actually gets to deepZoom """
    expected_data = {'Image': {'xmlns': 'http://schemas.microsoft.com/deepzoom/2008',
                               'Url': 'https://d32dm0rphc51dk.cloudfront.net/9JBWR-XxkbcyOLUxbCKeOw/dztiles/',
                               'Format': 'jpg',
                               'TileSize': 512,
                               'Overlap': 0,
                               'Size': {'Width': 961, 'Height': 1200}}}
    assert okai_example_bootstrap[0][1]["json"]["data"]["artwork"]["images"][0]["deepZoom"] == expected_data


def test_formatting_dztiles_url():
    """ Test that dztiles_url() returns correct url """
    assert dztiles_url(okai_example_bootstrap) == ExampleUrls.okai_fix_initial_dz_url


def test_artist_and_title():
    """ Test that artist_and_title() returns correct string """
    assert artist_and_title(okai_example_bootstrap) == "Fix (2019) by Jeremy Okai Davis"


def test_get_list_of_related_images_for_rabbit_hole():
    """ Test for correct parsing of bootstrap json """
    assert okai_example_bootstrap[0][1]["json"]["data"]["artwork"]["layer"]["artworksConnection"]["edges"] == related_images
