import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint


# TODO parse to get the ID
    # BeautifulSoup?
    # print(dali[0][1]["json"]["data"]["artwork"]["images"][0]["url"])
# TODO insert the id from 'https://d32dm0rphc51dk.cloudfront.net/dAMtqpwtIUgN0zlJpjYrmA/medium.jpg' into
#   "https://d32dm0rphc51dk.cloudfront.net/dAMtqpwtIUgN0zlJpjYrmA/dztiles/12/{}_{}.jpg"

def get_source(url):
    r = requests.get(url)
    return(r.content)

# madonne = "https://www.artsy.net/artwork/salvador-dali-madonne"
# source_string = get_source(madonne)

# job = "https://www.artsy.net/artwork/alphonse-mucha-job-30"
# source_string = get_source(job)

# cadeau = "https://www.artsy.net/artwork/man-ray-cadeau-1926"
# source_string = get_source(cadeau)
# https://d32dm0rphc51dk.cloudfront.net/HFgPe_vJgqATQdyClCvyMQ/medium.jpg



def parse_source_code(source_string):
    # f = open('source_code.html', 'wb')  # change to with open
    # f.write(source_string)
    # f.close()
    with open('source_code.html', 'wb') as file_obj:
        file_obj.write(source_string)
        
    with open('source_code.html') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    return soup
    
# the_soup = parse_source_code(source_string)

# substring = "RELAY"
def get_dztiles_url(parsed_html, substring):
    for block in parsed_html.find_all('script'):
        if substring in str(block):
            bootstrap_string = block.string.strip()
            bootstrap_string = bootstrap_string.replace("var __RELAY_BOOTSTRAP__ = ", "")   
            bootstrap_string = bootstrap_string[:-1]
            # print(bootstrap_string)   
            bootstrap_json = json.loads(json.loads(bootstrap_string))
            # pprint(bootstrap_json)
            jpeg_url = (bootstrap_json[0][1]["json"]["data"]["artwork"]["images"][0]["url"])
            dztiles_url_11 = jpeg_url[:-10] + "dztiles/11/{}_{}.jpg"
            # print(dztiles_url_11)
            # dztiles_url_12 = jpeg_url[:-10] + "dztiles/12/{}_{}.jpg"
            return dztiles_url_11
        
# print(get_dztiles_url(the_soup, "RELAY"))

def image_url(artsy_url):  # Ryan! Both of these work. Is one preferred?
    # source_string = get_source(artsy_url)
    # the_soup = parse_source_code(source_string)
    # print(get_dztiles_url(the_soup, "RELAY"))
    
    print(get_dztiles_url(parse_source_code(get_source(artsy_url)), "RELAY"))
    return(get_dztiles_url(parse_source_code(get_source(artsy_url)), "RELAY"))
    
    
# url_for_image = image_url("https://www.artsy.net/artwork/man-ray-cadeau-1926")


    
    