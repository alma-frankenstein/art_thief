from format_url import image_url
from main import *

sample_images = ["https://www.artsy.net/artwork/man-ray-cadeau-1926", "https://www.artsy.net/artwork/alphonse-mucha-job-30",
                 "https://www.artsy.net/artwork/salvador-dali-madonne"]

# du_nord = "https://www.artsy.net/artwork/joseph-cornell-hotel-du-nord-little-durer"
# root_url = image_url(du_nord)
# fabulous_picture(root_url)

for url in sample_images:
    root_url = image_url(url)
    fabulous_picture(root_url)
    