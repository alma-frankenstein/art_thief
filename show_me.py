import PIL
import argparse
# import os
# import sys

from format_url import image_url
from main import fabulous_picture

parser = argparse.ArgumentParser(description="Enter '--nargs' followed by the urls, in quotes. Saves images in file tree.")
# example: 
# python3 show_me.py --nargs "https://www.artsy.net/artwork/salvador-dali-madonne" "https://www.artsy.net/artwork/vivian-maier-0117585-jeweler-through-window"

parser.add_argument('--nargs', nargs='+')
args = parser.parse_args()

for url in args.nargs:
    root_url = image_url(url)
    fabulous_picture(root_url)
