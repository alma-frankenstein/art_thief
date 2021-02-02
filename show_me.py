import PIL
import argparse
import click

from format_url import image_url
# from piece_info import image_url

from main import fabulous_picture

#----------argparse---------------

# parser = argparse.ArgumentParser(description="Enter '--nargs' followed by the urls, in quotes. Saves images in file tree.")
# # example: 
# # python3 show_me.py --nargs "https://www.artsy.net/artwork/salvador-dali-madonne" "https://www.artsy.net/artwork/vivian-maier-0117585-jeweler-through-window"

# parser.add_argument('--nargs', nargs='+')
# args = parser.parse_args()

# for url in args.nargs:
#     root_url = image_url(url)
#     fabulous_picture(root_url)

#-------------input()----------------------
# print("Hey, kids! Enter some Artsy urls!")
# print("Example: https://www.artsy.net/artwork/andy-warhol-jean-paul-gaultier-1 https://www.artsy.net/artwork/ndidi-emefiele-play-station-2-1")
# urls = input()
# urls = urls.split(" ")

# for url in urls:
#     root_url = image_url(url)
#     fabulous_picture(root_url)
    
#----------click------------------
# example: python3 show_me.py https://www.artsy.net/artwork/ndidi-emefiele-play-station-2-1 https://www.artsy.net/artwork/cindy-sherman-untitled-293
@click.command()
@click.argument('artsy_urls', nargs=-1)
def save_pics(artsy_urls):
    for url in artsy_urls:
        root_url, title_artist = image_url(url)
        fabulous_picture(root_url, title_artist)
    
save_pics()
