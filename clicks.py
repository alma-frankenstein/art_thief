import click
from save_pic import save_pic
from related_images import rabbit_hole
from surprise_me import get_random_picture

#----------argparse---------------

# parser = argparse.ArgumentParser(description="Enter '--nargs' followed by the urls, in quotes. Saves images in file tree.")
# # example: 
# # python3 show_me.py --nargs "https://www.artsy.net/artwork/salvador-dali-madonne" "https://www.artsy.net/artwork/vivian-maier-0117585-jeweler-through-window"

# parser.add_argument('--nargs', nargs='+')
# args = parser.parse_args()

# for url in args.nargs:
#     root_url = image_json(url)
#     get_tiles_and_save(root_url)

#-------------input()----------------------
# print("Hey, kids! Enter some Artsy urls!")
# print("Example: https://www.artsy.net/artwork/andy-warhol-jean-paul-gaultier-1 https://www.artsy.net/artwork/ndidi-emefiele-play-station-2-1")
# urls = input()
# urls = urls.split(" ")

# for url in urls:
#     root_url = image_json(url)
#     get_tiles_and_save(root_url)
    
#----------click------------------
# example: python3 clicks.py https://www.artsy.net/artwork/ndidi-emefiele-play-station-2-1 https://www.artsy.net/artwork/cindy-sherman-untitled-293
@click.group()
def save_or_explore():
    pass

# example: python3 clicks.py save_pics https://www.artsy.net/artwork/ndidi-emefiele-play-station-2-1
@click.command(name='save_pics')
@click.argument('artsy_urls', nargs=-1)
def save_pics(artsy_urls):
    for url in artsy_urls:
        save_pic(url)

# example: python3 clicks.py explore 4 https://www.artsy.net/artwork/gerhard-richter-abstract-painting-abstraktes-bild-1
@click.command(name='explore')
@click.argument('num_of_images', type=int)
@click.argument('artsy_url')
def explore(num_of_images, artsy_url):
    rabbit_hole(num_of_images, artsy_url)
    
# example: python3 clicks.py surprise 3
@click.command(name='surprise')
@click.argument('num_of_surprises', type=int)
def surprise(num_of_surprises):
    for i in range(num_of_surprises):
        get_random_picture()

save_or_explore.add_command(save_pics)
save_or_explore.add_command(explore)
save_or_explore.add_command(surprise)

if __name__=='__main__':
    save_or_explore()


# https://www.artsy.net/artwork/joel-peter-witkin-carrot-cake-number-1
# https://www.artsy.net/artwork/bert-stern-pirelli-calendar-by-bert-stern  