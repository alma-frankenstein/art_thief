from io import BytesIO
import requests
from PIL import Image
# https://www.artsy.net/artwork/salvador-dali-madonne
# https://d32dm0rphc51dk.cloudfront.net/dAMtqpwtIUgN0zlJpjYrmA/dztiles/10/1_1.jpg
# TODO Automate the url grab
# TODO Automate the tile counts
# TODO Include Metadata (artist, title, etc)

# root_url = "https://d32dm0rphc51dk.cloudfront.net/dAMtqpwtIUgN0zlJpjYrmA/dztiles/12/{}_{}.jpg"   # Dali
root_url = "https://d32dm0rphc51dk.cloudfront.net/z6cZrfbgQXCnoZPztYQTsQ/dztiles/11/{}_{}.jpg"  # Mucha

# Mucha 3x3
# Dali 5x8 (final: Fetching image 4_7.jpg)
TILE_MAX_RANGE = 9
TILE_SIZE = 512

# TODO It should be safe to assume the first tile is enough to determine the maximum TILE_SIZE.
#   If the image creation could be delayed until after the first tile is fetched we wouldn't need TILE_SIZE
new_image = Image.new(
    'RGB', (TILE_SIZE * TILE_MAX_RANGE, TILE_SIZE * TILE_MAX_RANGE))


def paste_on_canvas(i, j, image_data):
    im = Image.open(BytesIO(image_data))
    new_image.paste(im, (TILE_SIZE * i, TILE_SIZE * j))
    print(f"Fetching image {i}_{j}.jpg")


def crop_n_show():
    cropped_image = new_image.crop((0, 0, actual_width, actual_height))
    cropped_image.show()


def find_max_width() -> int:
    return _find_max_dimension(TILE_MAX_RANGE, find_width=True)


def find_max_height() -> int:
    return _find_max_dimension(TILE_MAX_RANGE, find_width=False)


def _find_max_dimension(max_range, find_width: bool = True) -> int:
    max_found = False
    counter = 0
    actual_size = 0
    for dim in range(TILE_MAX_RANGE):
        x, y = 0, dim
        if find_width:
            y, x = x, y
        r = requests.get(root_url.format(x, y))
        if r.ok:
            counter += 1
            im = Image.open(BytesIO(r.content))
            width, height = im.size
            paste_on_canvas(x, y, r.content)
            if find_max_width:
                actual_size += width
            else:
                actual_size += height
            print("in counter")
        else:
            # max_found = True
            # print("WARNING:  Image boundary not found.  This may only be part of it!")
            return dim, actual_size
            # return counter, actual_size
    # else:
    #     return dim, actual_size


width_counter, actual_width = find_max_width()
height_counter, actual_height = find_max_height()

# if not width_counter or not height_counter:
#     print("WARNING:  Image boundary not found.  This may only be part of it!")
# TODO Parallelize the tile fetch

# #TODO Capture Title, Author, Year, etc and put in filename/metadata


def get_tiles(w_counter, h_counter):
    for i in range(1, w_counter):
        for j in range(1, h_counter):
            r = requests.get(root_url.format(i, j))
            paste_on_canvas(i, j, image_data=r.content)


get_tiles(width_counter, height_counter)

print(
    f"Image size computed at: {actual_width}x{actual_height} (NOT {new_image.size})")

crop_n_show()

# # TODO Turn the whole thing into a flask app and host it on GH?
