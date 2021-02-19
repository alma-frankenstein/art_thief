""" Suite of tests for the save_pic.py module """
from pathlib import Path
import pytest
import requests

from src.core.get_and_save_pic import amend_dz_url, save_pic, get_image_from_artsy, get_artist_title_from_artsy_url
from src.tests.example_urls import ExampleUrls


def test_amend_dz_url_single_digit():
    url = "https://d32dm0rphc51dk.cloudfront.net/JQI2YbnwwGCiT7dHH41_9A/dztiles/13/{}_{}.jpg"
    new_dz_num = 7
    assert amend_dz_url(
        url, new_dz_num) == "https://d32dm0rphc51dk.cloudfront.net/JQI2YbnwwGCiT7dHH41_9A/dztiles/7/{}_{}.jpg"


def test_amend_dz_url_single_digit_str():
    url = "https://d32dm0rphc51dk.cloudfront.net/JQI2YbnwwGCiT7dHH41_9A/dztiles/13/{}_{}.jpg"
    new_dz_num = "7"
    assert amend_dz_url(
        url, new_dz_num) == "https://d32dm0rphc51dk.cloudfront.net/JQI2YbnwwGCiT7dHH41_9A/dztiles/7/{}_{}.jpg"


def test_amend_dz_url_double_digit():
    url = "https://d32dm0rphc51dk.cloudfront.net/JQI2YbnwwGCiT7dHH41_9A/dztiles/13/{}_{}.jpg"
    new_dz_num = 77
    assert amend_dz_url(
        url, new_dz_num) == "https://d32dm0rphc51dk.cloudfront.net/JQI2YbnwwGCiT7dHH41_9A/dztiles/77/{}_{}.jpg"


def test_amend_dz_url_invalid_dz_num():
    url = "https://d32dm0rphc51dk.cloudfront.net/JQI2YbnwwGCiT7dHH41_9A/dztiles/13/{}_{}.jpg"
    new_dz_num = "7/7"
    with pytest.raises(ValueError):
        amend_dz_url(url, new_dz_num)


def test_save_pic_with_valid_artsy_url():
    url = ExampleUrls.vanilla
    assert save_pic(get_image_from_artsy(url), get_artist_title_from_artsy_url(
        url)) == Path('src/static/Fix (2019) by Jeremy Okai Davis.jpg').absolute()


def test_save_pic_with_jpg_only_artsy_url():
    url = ExampleUrls.jpg_only
    with pytest.raises(AttributeError):
        save_pic(get_image_from_artsy(url), "Title string!")
    # assert save_pic(get_image_from_artsy(url), "Title string!") == None


@ pytest.mark.parametrize("bad_url", ["hailSatan", "blah", "kdsajf", "sakfja", "1"])
def test_parametrized_save_pic_with_invalid_url(bad_url):
    """ save_pic() should fail with an invalid url """
    with pytest.raises(requests.exceptions.MissingSchema):
        get_image_from_artsy(bad_url)

