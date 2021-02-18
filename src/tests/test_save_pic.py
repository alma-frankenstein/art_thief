""" Suite of tests for the save_pic.py module """
from pathlib import Path
import pytest
import requests

from src.core.get_and_save_pic import amend_dz_url, save_pic, get_image_from_artsy, get_artist_title_from_artsy_url
from src.tests.example_urls import ExampleUrls


def test_amend_dz_url_single_digit():
    """ Replace dztile num with single digit integer """
    url = "https://d32dm0rphc51dk.cloudfront.net/JQI2YbnwwGCiT7dHH41_9A/dztiles/13/{}_{}.jpg"
    new_dz_num = 7
    assert amend_dz_url(
        url, new_dz_num) == "https://d32dm0rphc51dk.cloudfront.net/JQI2YbnwwGCiT7dHH41_9A/dztiles/7/{}_{}.jpg"


def test_amend_dz_url_single_digit_str():
    """ Replace dztile num with single digit string """
    url = "https://d32dm0rphc51dk.cloudfront.net/JQI2YbnwwGCiT7dHH41_9A/dztiles/13/{}_{}.jpg"
    new_dz_num = "7"
    assert amend_dz_url(
        url, new_dz_num) == "https://d32dm0rphc51dk.cloudfront.net/JQI2YbnwwGCiT7dHH41_9A/dztiles/7/{}_{}.jpg"


def test_amend_dz_url_double_digit():
    """ Replace dztile num with double digit integer """
    url = "https://d32dm0rphc51dk.cloudfront.net/JQI2YbnwwGCiT7dHH41_9A/dztiles/13/{}_{}.jpg"
    new_dz_num = 77
    assert amend_dz_url(
        url, new_dz_num) == "https://d32dm0rphc51dk.cloudfront.net/JQI2YbnwwGCiT7dHH41_9A/dztiles/77/{}_{}.jpg"


def test_amend_dz_url_invalid_dz_num():
    """ Replace dztile num with non-numbers. Should raise error. """
    url = "https://d32dm0rphc51dk.cloudfront.net/JQI2YbnwwGCiT7dHH41_9A/dztiles/13/{}_{}.jpg"
    new_dz_num = "7/7"
    with pytest.raises(ValueError):
        amend_dz_url(url, new_dz_num)


def test_save_pic_with_valid_artsy_url():
    """ Pass vanilla artsy url to save_picture() """
    url = ExampleUrls.vanilla
    assert save_pic(get_image_from_artsy(url), get_artist_title_from_artsy_url(
        url)) == Path('src/static/Fix (2019) by Jeremy Okai Davis.jpg').absolute()

# E  AssertionError: assert PosixPath('/home/alma/repos/artscrapr/src/src/static/Fix (2019) by Jeremy Okai Davis.jpg') == '/home/alma/repos/artscrapr/src/src/static/Fix (2019) by Jeremy Okai Davis.jpg'
# E +  where PosixPath('/home/alma/repos/artscrapr/src/src/static/Fix (2019) by Jeremy Okai Davis.jpg') = save_pic(<PIL.Image.Image image mode=RGB size=961x1200 at 0x7F142B170670>, 'Fix (2019) by Jeremy Okai Davis')
# E +    where <PIL.Image.Image image mode=RGB size=961x1200 at 0x7F142B170670> = get_image_from_artsy('https://www.artsy.net/artwork/jeremy-okai-davis-fix')
# E +    and   'Fix (2019) by Jeremy Okai Davis' = get_artist_title_from_artsy_url('https://www.artsy.net/artwork/jeremy-okai-davis-fix')


def test_save_pic_with_jpg_only_artsy_url():
    """ Make sure save_picture catches non-dztiles urls """
    url = ExampleUrls.jpg_only
    assert save_pic(get_image_from_artsy(url), "Title string!") == "no high res version"


def test_save_pic_with_invalid_url():
    """ save_pic() should fail with an bogus url """
    url = ExampleUrls.bogus_url
    with pytest.raises(requests.exceptions.MissingSchema):
        save_pic(get_image_from_artsy(url), "Title string!")


@ pytest.mark.parametrize("bad_url", ["hailSatan", "blah", "kdsajf", "sakfja", "1"])
def test_parametrized_save_pic_with_invalid_url(bad_url):
    """ save_pic() should fail with an bogus url """
    with pytest.raises(requests.exceptions.MissingSchema):
        get_image_from_artsy(bad_url)
