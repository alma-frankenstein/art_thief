"""
These are live tests at the moment.  They do calls to artsy.net
"""
from src.corev2.main import ArtsyImage
from src.tests.example_urls import ExampleUrls


def test_get_json():
    x = ArtsyImage(ExampleUrls.vanilla)
    assert x.image_json is not None


def test_artist_and_title_present():
    x = ArtsyImage(ExampleUrls.vanilla)
    assert x.artist_and_title == "Fix (2019) by Jeremy Okai Davis"


def test_dz_tile_url():
    x = ArtsyImage(ExampleUrls.vanilla)
    assert x.dztiles_url == "https://d32dm0rphc51dk.cloudfront.net/9JBWR-XxkbcyOLUxbCKeOw/dztiles/14/{}_{}.jpg"


def test_random():
    x = ArtsyImage(ExampleUrls.vanilla)
    assert isinstance(x.get_related_image_url(), str)
