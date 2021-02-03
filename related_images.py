import requests
import json
from bs4 import BeautifulSoup
from main import fabulous_picture


def get_source(url):
    r = requests.get(url)
    return(r.content)


def parse_source_code(source_string):
    with open('source_code.html', 'wb') as file_obj:
        file_obj.write(source_string)
        
    with open('source_code.html') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    return soup
    
    
# TODO 11 vs 12 in dztiles

# def get_dztiles_url(parsed_html, substring):
#     for block in parsed_html.find_all('script'):
#         if substring in str(block):
#             bootstrap_string = block.string.strip()
#             bootstrap_string = bootstrap_string.replace("var __RELAY_BOOTSTRAP__ = ", "")   
#             bootstrap_string = bootstrap_string[:-1]
#             bootstrap_json = json.loads(json.loads(bootstrap_string))
#             with open('output.json', 'w') as f:
#                 f.write(json.dumps(bootstrap_json, indent=4))
#             jpeg_url = (bootstrap_json[0][1]["json"]["data"]["artwork"]["images"][0]["deepZoom"]["Image"]["Url"])
#             dztiles_url_11 = jpeg_url + "11/{}_{}.jpg"
#             piece_info = (bootstrap_json[0][1]["json"]["data"]["artwork"]["meta"]["title"]).split("|")
#             artist_name = piece_info[0].strip().replace(" ", "_")
#             title_and_year = piece_info[1].strip().replace(" ", "_")
#             title_artist =  title_and_year + "_by_" + artist_name
#             related_image_href = (bootstrap_json[0][1]["json"]["data"]["artwork"]["layer"]["artworksConnection"]["edges"][0]["node"]["href"]) # [0] after ["edges"] is the first related image
#             print(related_image_href)
#             related_image_url = "https://www.artsy.net" + related_image_href
#             print(related_image_url)
#             return dztiles_url_11, title_artist, related_image_url

def _get_bootstrap_json(parsed_html, substring):
    for block in parsed_html.find_all('script'):
        if substring in str(block):
            bootstrap_string = block.string.strip()
            bootstrap_string = bootstrap_string.replace("var __RELAY_BOOTSTRAP__ = ", "")   
            bootstrap_string = bootstrap_string[:-1]
            bootstrap_json = json.loads(json.loads(bootstrap_string))
            with open('output.json', 'w') as f:
                f.write(json.dumps(bootstrap_json, indent=4))
            return bootstrap_json
        
     
        
def image_url(artsy_url):  
    source_string = get_source(artsy_url)
    the_soup = parse_source_code(source_string)
    return(get_dztiles_url(the_soup, "RELAY"))
        
def rabbit_hole(num_images, start_url):
    counter = 0
    current_url = start_url
    while counter < num_images:
        root_url, jpg_label, next_artsy_url = image_url(current_url)
        current_url = next_artsy_url
        fabulous_picture(root_url, jpg_label)
        counter += 1

rabbit_hole(3, "https://www.artsy.net/artwork/david-wojnarowicz-arthur-rimbaud-in-new-york-diner-2")

# TODO make random
# TODO break get_dztile_url() into separate functions