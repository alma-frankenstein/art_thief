from metadata_from_json import dztiles_url, artist_and_title
from tests.example_urls import ExampleUrls
from tests.example_related_images import related_images
import pytest
import json


with open('example_bootstrap.json', 'r') as f:
    okai_example_bootstrap = json.load(f)


def test_get_deep_zoom_data():
    expected_data = {'Image': {'xmlns': 'http://schemas.microsoft.com/deepzoom/2008', 
                               'Url': 'https://d32dm0rphc51dk.cloudfront.net/9JBWR-XxkbcyOLUxbCKeOw/dztiles/',
                               'Format': 'jpg', 
                               'TileSize': 512, 
                               'Overlap': 0, 
                               'Size': {'Width': 961, 'Height': 1200}}}
    assert okai_example_bootstrap[0][1]["json"]["data"]["artwork"]["images"][0]["deepZoom"] == expected_data


def test_formatting_dztiles_url():
    assert dztiles_url(
        okai_example_bootstrap) == ExampleUrls.okai_fix_initial_dz_url


def test_artist_and_title():
    assert artist_and_title(
        okai_example_bootstrap) == "Fix (2019) by Jeremy Okai Davis"


def test_get_list_of_related_images_for_rabbit_hole():
    assert okai_example_bootstrap[0][1]["json"]["data"]["artwork"]["layer"]["artworksConnection"]["edges"] == related_images
