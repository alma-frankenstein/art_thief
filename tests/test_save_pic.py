from save_pic import amend_dz_url, save_pic
from tests.example_urls import ExampleUrls
import pytest


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
    assert save_pic(url) == "successfully saved"


def test_save_pic_with_jpg_only_artsy_url():
    url = ExampleUrls.jpg_only
    assert save_pic(url) == "no high res version"


@pytest.mark.xfail
def test_save_pic_with_invalid_url():
    url = ExampleUrls.bogus_url
    assert save_pic(url) == "works okay"




