import logging
from metadata_from_json import dztiles_url, artist_and_title
from format_url import image_json
from main import get_tiles_and_save
# from urllib.parse import urljoin
# from main import bcolors
from loggers import save_pic_logger, high_alert_logger
import sys

MAX_DZNUM = 13

# save_pic_logger = logging.getLogger(__name__)
# high_alert_logger = logging.getLogger("We found a BIG ONE!")

# alert_handler = logging.StreamHandler(sys.stdout)  # to console 
# hq_formatter = logging.Formatter(bcolors.OKGREEN + '%(name)-12s: %(levelname)-8s %(message)s' + bcolors.ENDC)  # custom format to add to handler
# alert_handler.setFormatter(hq_formatter)

# high_alert_logger.addHandler(alert_handler)  # add handler to logger


# save_pic_logger.setLevel(logging.DEBUG)
# high_alert_logger.setLevel(logging.DEBUG)


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
        save_pic_logger.info(f"attempting to fetch: {artsy_url}")
        save_pic_logger.info(f"artwork name: {jpeg_label}")
        dz_num_counter = MAX_DZNUM
        while dz_num_counter > 8:
            amended_dz_url = amend_dz_url(root_url, dz_num_counter)
            save_pic_logger.info(f"dztiles number was too large. trying {dz_num_counter} as {amended_dz_url}")
            if get_tiles_and_save(amended_dz_url, jpeg_label):
                if dz_num_counter > MAX_DZNUM:
                    high_alert_logger.debug(f"picture bigger than MAX_DZNUM {MAX_DZNUM}!")
                save_pic_logger.info("successfully saved picture")
                break
            dz_num_counter -= 1
    else:
        save_pic_logger.warning(f"{jpeg_label} has no high resolution version. Skipping")
        
    
# save_pic("https://www.artsy.net/artwork/david-wojnarowicz-arthur-rimbaud-in-new-york-diner-2")
# save_pic("https://www.artsy.net/artwork/bert-stern-pirelli-calendar-by-bert-stern")  # no dztiles
# save_pic("https://www.artsy.net/artwork/salvador-dali-madonne")
# save_pic("https://www.artsy.net/artwork/jeremy-okai-davis-fix")

# large enough to be dztiles/12, actually need to be a smaller number
# save_pic("https://www.artsy.net/artwork/georges-mazilu-portrait-de-femme")
# save_pic("https://www.artsy.net/artwork/stanley-whitney-untitled-449")
# save_pic("https://www.artsy.net/artwork/andy-warhol-camouflage-set-of-5-skateboard-decks")  # 10
# save_pic("https://www.artsy.net/artwork/greg-gong-untitled-7")   # 10
# save_pic("https://www.artsy.net/artwork/vik-muniz-handmade-noise") # 10


# print(amend_dz_url("https://d32dm0rphc51dk.cloudfront.net/naV_9uqzYITVYviI1V2iHA/dztiles/10/{}_{}.jpg"))


# Nonetype error
# save_pic("https://www.artsy.net/artwork/bernard-aubertin-tableau-clous-199") 
# save_pic("https://www.artsy.net/artwork/frida-orupabo-resting-head")   # dz 13?!
# save_pic("https://www.artsy.net/artwork/salvador-dali-la-femme-aux-cheveus-dor-et-son-garde-1967")
# save_pic("https://www.artsy.net/artwork/andy-warhol-camouflage-set-of-5-skateboard-decks")

# https://www.artsy.net/artwork/dapper-bruce-lafitte-no-summercamp #dz13