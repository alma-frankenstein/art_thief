from metadata_from_json import dztiles_url, artist_and_title
from format_url import image_json
from main import fabulous_picture


def save_pic(artsy_url):
    bootstrap = image_json(artsy_url)
    jpeg_label = artist_and_title(bootstrap)
    root_url = dztiles_url(bootstrap)
    fabulous_picture(root_url, jpeg_label)
    
# save_pic("https://www.artsy.net/artwork/david-wojnarowicz-arthur-rimbaud-in-new-york-diner-2")
# save_pic("https://www.artsy.net/artwork/doug-and-mike-starn-bbmet-06-slash-03-slash-10-s2257f")
