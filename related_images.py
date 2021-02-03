from format_url import image_json
from metadata_from_json import related_image_url
from save_pic import save_pic


def rabbit_hole(num_images, start_url):
    counter = 0
    current_url = start_url
    while counter < num_images:
        save_pic(current_url)
        bootstrap = image_json(current_url)
        current_url = related_image_url(bootstrap)
        counter += 1

rabbit_hole(3, "https://www.artsy.net/artwork/david-wojnarowicz-arthur-rimbaud-in-new-york-diner-2")
