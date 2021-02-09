import logging
from metadata_from_json import dztiles_url, artist_and_title
from format_url import image_json
from main import get_tiles_and_save
from urllib.parse import urljoin


# def amend_dz_url(root_url):
#     stem = root_url[:-12]
#     new_dz_num = "9/{}_{}.jpg"
#     new_dz_url = urljoin(stem, new_dz_num)
#     return new_dz_url

# def amend_dz_url(root_url:str, dz_num:str="9") -> str:
#     stem = root_url.rsplit("/", 2)
#     stem[-2] = dz_num # TODO Why???????
#     return "/".join(stem)  

def amend_dz_url(root_url:str, dz_num) -> str:
    stem = root_url.rsplit("/", 2)
    stem[-2] = str(dz_num) # TODO Why???????
    return "/".join(stem)  
    

def save_pic(artsy_url):
    bootstrap = image_json(artsy_url)
    jpeg_label = artist_and_title(bootstrap)
    root_url = dztiles_url(bootstrap)
    if root_url:
        try:
            get_tiles_and_save(root_url, jpeg_label)
        except SystemError as e:
            dz_num_counter = 11
            logging.error(f"attempting to fetch: {artsy_url}")
            logging.error(f"artwork name: {jpeg_label}")
            try:
                while dz_num_counter > 8:
                    amended_dz_url = amend_dz_url(root_url, dz_num_counter)
                    logging.info(f"dztiles number was too large. trying {dz_num_counter} as {amend_dz_url(root_url, dz_num_counter)}")
                    if get_tiles_and_save(amended_dz_url, jpeg_label):
                        logging.info(f"Success at {dz_num_counter} with url {amended_dz_url}")
                        break
                    dz_num_counter -= 1
            except:
                raise e
    else:
        logging.warning(f"{jpeg_label} has no high resolution version. Skipping")
        
    
# save_pic("https://www.artsy.net/artwork/david-wojnarowicz-arthur-rimbaud-in-new-york-diner-2")
# save_pic("https://www.artsy.net/artwork/bert-stern-pirelli-calendar-by-bert-stern")  # no dztiles
# save_pic("https://www.artsy.net/artwork/salvador-dali-madonne")

# large enough to be dztiles/12, actually need to be a smaller number
# save_pic("https://www.artsy.net/artwork/georges-mazilu-portrait-de-femme")
# save_pic("https://www.artsy.net/artwork/stanley-whitney-untitled-449")
# save_pic("https://www.artsy.net/artwork/andy-warhol-camouflage-set-of-5-skateboard-decks")  # 10
# save_pic("https://www.artsy.net/artwork/greg-gong-untitled-7")   # 10
# save_pic("https://www.artsy.net/artwork/vik-muniz-handmade-noise") # 10


# print(amend_dz_url("https://d32dm0rphc51dk.cloudfront.net/naV_9uqzYITVYviI1V2iHA/dztiles/10/{}_{}.jpg"))