# from main import fabulous_picture
# from format_url import image_json
# import pathlib
from urllib.parse import urljoin


def dztiles_url(json_bootstrap):
    jpeg_url = (json_bootstrap[0][1]["json"]["data"]["artwork"]["images"][0]["deepZoom"]["Image"]["Url"])
    dztiles_url = urljoin(jpeg_url, "11/{}_{}.jpg")
    return dztiles_url


def artist_and_title(json_bootstrap):
    piece_info = (json_bootstrap[0][1]["json"]["data"]["artwork"]["meta"]["title"]).split("|")
    
    # Ex. David Wojnarowicz
    artist_name = piece_info[0].strip()

    # Ex. Untitled (Face in Dirt), 1991/2018
    title_and_year = piece_info[1].strip()
    
    title_artist =  f"{title_and_year} by {artist_name}"
    return title_artist
        
        
def related_image_url(json_bootstrap):
    related_image_href = (json_bootstrap[0][1]["json"]["data"]["artwork"]["layer"]["artworksConnection"]["edges"][0]["node"]["href"]) # [0] after ["edges"] is the first related image
    related_image_url = urljoin("https://www.artsy.net", related_image_href)
    return related_image_url