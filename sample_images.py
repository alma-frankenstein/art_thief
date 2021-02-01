import PIL
from format_url import image_url
from main import fabulous_picture

sample_images = ["https://www.artsy.net/artwork/vivian-maier-0117585-jeweler-through-window", "https://www.artsy.net/artwork/joseph-cornell-hotel-du-nord-little-durer",
                 "https://www.artsy.net/artwork/salvador-dali-madonne", "https://www.artsy.net/artwork/david-wojnarowicz-arthur-rimbaud-in-new-york-diner-2"]

# sample_images = ["https://www.artsy.net/artwork/nick-cave-until-8"]

for url in sample_images:
    root_url = image_url(url)
    fabulous_picture(root_url)
    
