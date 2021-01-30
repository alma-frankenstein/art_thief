from io import BytesIO
import requests
from PIL import Image
# from format_url import dztiles_url_11
from format_url import image_url
# https://www.artsy.net/artwork/salvador-dali-madonne
# https://d32dm0rphc51dk.cloudfront.net/dAMtqpwtIUgN0zlJpjYrmA/dztiles/10/1_1.jpg
# TODO Automate the url grab
# TODO Automate the tile counts
# TODO Include Metadata (artist, title, etc)

# root_url = "https://d32dm0rphc51dk.cloudfront.net/dAMtqpwtIUgN0zlJpjYrmA/dztiles/12/{}_{}.jpg"   # Dali
# root_url = "https://d32dm0rphc51dk.cloudfront.net/z6cZrfbgQXCnoZPztYQTsQ/dztiles/11/{}_{}.jpg"  # Mucha
# root_url = "https://d32dm0rphc51dk.cloudfront.net/HFgPe_vJgqATQdyClCvyMQ/dztiles/11/{}_{}.jpg"  # Man Ray
# root_url = "https://d32dm0rphc51dk.cloudfront.net/wslu5vVcYM-CRPQ72I3fEQ/dztiles/12/{}_{}.jpg"  # Picasso

# root_url_11 = dztiles_url_11
# root_url_12 = dztiles_url_12
# root_url = dztiles_url_11
# root_url = url_for_image

# Mucha 3x3
# Dali 5x8 (final: Fetching image 4_7.jpg)
TILE_MAX_RANGE = 5
TILE_SIZE = 512

# TODO It should be safe to assume the first tile is enough to determine the maximum TILE_SIZE.
#   If the image creation could be delayed until after the first tile is fetched we wouldn't need TILE_SIZE
new_image = Image.new(
    'RGB', (TILE_SIZE * TILE_MAX_RANGE, TILE_SIZE * TILE_MAX_RANGE))

# def check_dztiles(url_11, url_12):
#     r = requests.get(url_11.format(0, 0))
#     if r.ok:
#         root_url = url_11
#     else:
#         root_url = url_12
#     return root_url

# root_url = check_dztiles(root_url_11, root_url_12)
# print(root_url)

def fabulous_picture(dz_url):
    width_counter, actual_width = find_max_width(dz_url)
    height_counter, actual_height = find_max_height(dz_url)
    get_tiles(dz_url, width_counter, height_counter)
    print(f"Image size computed at: {actual_width}x{actual_height} (NOT {new_image.size})")
    crop_n_show(actual_width, actual_height, dz_url)
    

def paste_on_canvas(i, j, image_data):
    im = Image.open(BytesIO(image_data))
    new_image.paste(im, (TILE_SIZE * i, TILE_SIZE * j))
    print(f"Fetching image {i}_{j}.jpg")


def crop_n_show(actual_w, actual_h, url):
    temp_id = url[40:46]
    cropped_image = new_image.crop((0, 0, actual_w, actual_h))
    cropped_image.save(f"image{temp_id}.jpg")
    # cropped_image.show()  ## RyJ! You'll probably want to uncomment this


def find_max_width(dz_url) -> int:
    return _find_max_dimension(dz_url, TILE_MAX_RANGE, find_width=True)


def find_max_height(dz_url) -> int:
    return _find_max_dimension(dz_url, TILE_MAX_RANGE, find_width=False)


def _find_max_dimension(dz_url, max_range, find_width: bool = True) -> (int, int):
    root_url = dz_url
    actual_size = 0
    for dim in range(TILE_MAX_RANGE):
        x, y = 0, dim
        if find_width:
            y, x = x, y
        r = requests.get(root_url.format(x, y))
        if r.ok:
            im = Image.open(BytesIO(r.content))
            width, height = im.size
            paste_on_canvas(x, y, r.content)
            if find_width:
                actual_size += width
            else:
                actual_size += height
            print("in counter")
        else:
            return dim, actual_size
    print("WARNING:  Image boundary not found.  This may only be part of it!")
    return dim + 1, actual_size



# TODO Parallelize the tile fetch
# #TODO Capture Title, Author, Year, etc and put in filename/metadata

def get_tiles(dz_url, w_counter, h_counter):
    root_url = dz_url
    for i in range(1, w_counter):
        for j in range(1, h_counter):
            r = requests.get(root_url.format(i, j))
            paste_on_canvas(i, j, image_data=r.content)



# # TODO Turn the whole thing into a flask app and host it on GH?

# show a single picture:
# fabulous_picture("https://d32dm0rphc51dk.cloudfront.net/z6cZrfbgQXCnoZPztYQTsQ/dztiles/11/{}_{}.jpg")