import asyncio
import itertools
import time
from io import BytesIO
from pathlib import Path
from urllib.parse import urlparse

import aiohttp
from PIL import Image

# Benchmark for main.py:
# For Dali
#   Time to execute: 25.80s
# For Mucha
#   Time to execute: 4.31s

# Benchmark for async_main.py:
# For Dali
#   Time to execute: 2.84s
# For Mucha
#   Time to execute: 1.22s

t1 = time.time()


# https://www.artsy.net/artwork/salvador-dali-madonne
# https://d32dm0rphc51dk.cloudfront.net/dAMtqpwtIUgN0zlJpjYrmA/dztiles/10/1_1.jpg
# TODO Automate the url grab
# TODO Automate the tile counts
# TODO Include Metadata (artist, title, etc)


async def fetch(url, session):
    async with session.get(url) as response:
        if response.status == 200:
            response = await response.read()
            return Image.open((BytesIO(response))), parse_tile_number_from_url(url)
        return None, parse_tile_number_from_url(url)


async def fetch_many(loop, urls):
    async with aiohttp.ClientSession() as session:
        tasks = [loop.create_task(fetch(url, session)) for url in urls]
        return await asyncio.gather(*tasks)


def async_aiohttp_get_all(urls):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(fetch_many(loop, urls))


def parse_tile_number_from_url(url):
    return map(int, Path(urlparse(url).path).stem.split("_"))


# root_url = "https://d32dm0rphc51dk.cloudfront.net/dAMtqpwtIUgN0zlJpjYrmA/dztiles/12/{}_{}.jpg"  # Dali
root_url = "https://d32dm0rphc51dk.cloudfront.net/z6cZrfbgQXCnoZPztYQTsQ/dztiles/11/{}_{}.jpg"  # Mucha

# Mucha 3x3
# Dali 5x8 (final: Fetching image 4_7.jpg)
TILE_WIDTH_RANGE = 10
TILE_HEIGHT_RANGE = 10
TILE_SIZE = 512

# TODO It should be safe to assume the first tile is enough to determine the maximum TILE_SIZE.
#   If the image creation could be delayed until after the first tile is fetched we wouldn't need TILE_SIZE
new_image = Image.new('RGB', (TILE_SIZE * TILE_WIDTH_RANGE, TILE_SIZE * TILE_HEIGHT_RANGE))

# TODO A smarter algorithm for the actual_width/height would probably be:
#  Watch for smallest width
#  actual_width = (tile_count_width - 1) * TILE_SIZE + SMALLEST_WIDTH
actual_width = 0
actual_height = 0

# count width:
max_width = 1000000
max_height = 1000000

url_list = [root_url.format(i, 0) for i in range(TILE_WIDTH_RANGE)] + [root_url.format(0, j) for j in range(TILE_HEIGHT_RANGE)]

for image_tile, (i, j) in async_aiohttp_get_all(url_list):
    if not image_tile and not j > max_height and i == 0:
        max_height = j
    if not image_tile and not i > max_width and j == 0:
        max_width = i

if max_width > TILE_WIDTH_RANGE or max_height > TILE_HEIGHT_RANGE:
    print("WARNING:  Image boundary not found.  This may only be part of it!")

url_list = [root_url.format(i, j) for i, j in itertools.product(range(max_width), range(max_height))]

for image_tile, (i, j) in async_aiohttp_get_all(url_list):
    width, height = image_tile.size
    actual_height += height
    actual_width += width
    new_image.paste(image_tile, (TILE_SIZE * i, TILE_SIZE * j))

actual_width /= max_height
actual_height /= max_width

print(f"Image size computed at: {actual_width}x{actual_height} (NOT {new_image.size})")
cropped_image = new_image.crop((0, 0, actual_width, actual_height))
# cropped_image.save("img.png")
cropped_image.show()
t2 = time.time()
print(f"Time to execute: {t2 - t1:.2f}s")
# # TODO Turn the whole thing into a flask app and host it on GH?
