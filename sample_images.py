from format_url import image_url
from main import *
import PIL

sample_images = ["https://www.artsy.net/artwork/man-ray-cadeau-1926", "https://www.artsy.net/artwork/joseph-cornell-hotel-du-nord-little-durer",
                 "https://www.artsy.net/artwork/salvador-dali-madonne"]


for url in sample_images:
    root_url = image_url(url)
    fabulous_picture(root_url)
    