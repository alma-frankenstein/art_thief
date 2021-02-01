import PIL
import argparse
import os
import sys

from format_url import image_url
from main import fabulous_picture

parser = argparse.ArgumentParser(description="show artsy pictures")

parser.add_argument('urls',
                    # type=list,
                    help='a list of artsy urls as strings. Example: "https://www.artsy.net/artist-series/felix-gonzalez-torres-candy" ')

args = parser.parse_args()

input_urls = args.urls

# for url in input_urls:
#     root_url = image_url(url)
#     fabulous_picture(root_url)

root_url = image_url(input_urls)
fabulous_picture(root_url)



# sample_images = ["https://www.artsy.net/artwork/vivian-maier-0117585-jeweler-through-window", "https://www.artsy.net/artwork/joseph-cornell-hotel-du-nord-little-durer",
#                  "https://www.artsy.net/artwork/salvador-dali-madonne", "https://www.artsy.net/artwork/david-wojnarowicz-arthur-rimbaud-in-new-york-diner-2"]


# # sample_images = ["https://www.artsy.net/artwork/salvador-dali-madonne"]
# # sample_images = ["https://www.artsy.net/artwork/nick-cave-until-8"]

# for url in sample_images:
#     root_url = image_url(url)
#     fabulous_picture(root_url)
    