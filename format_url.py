import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint



def get_source(url):
    r = requests.get(url)
    return(r.content)


def parse_source_code(source_string):
    with open('source_code.html', 'wb') as file_obj:
        file_obj.write(source_string)
        
    with open('source_code.html') as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    return soup
    
    
def get_dztiles_url(parsed_html, substring):
    for block in parsed_html.find_all('script'):
        if substring in str(block):
            bootstrap_string = block.string.strip()
            bootstrap_string = bootstrap_string.replace("var __RELAY_BOOTSTRAP__ = ", "")   
            bootstrap_string = bootstrap_string[:-1]
            bootstrap_json = json.loads(json.loads(bootstrap_string))
            jpeg_url = (bootstrap_json[0][1]["json"]["data"]["artwork"]["images"][0]["url"])
            dztiles_url_11 = jpeg_url[:-10] + "dztiles/11/{}_{}.jpg"
            return dztiles_url_11
        

def image_url(artsy_url):  # Ryan! Both of these work. Is one preferred?
    # source_string = get_source(artsy_url)
    # the_soup = parse_source_code(source_string)
    # print(get_dztiles_url(the_soup, "RELAY"))
    
    print(get_dztiles_url(parse_source_code(get_source(artsy_url)), "RELAY"))
    return(get_dztiles_url(parse_source_code(get_source(artsy_url)), "RELAY"))
    
    


    
    