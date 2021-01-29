import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

# TODO format url for source code from an artsy url
    # https://www.artsy.net/artwork/salvador-dali-madonne  -> 
    # view-source:https://www.artsy.net/artwork/salvador-dali-madonne
# TODO get the content from that source page
# TODO get the value for 'var __RELAY_BOOTSTRAP__ ='
# TODO unescape that string
# TODO parse to get the ID
    # BeautifulSoup?
    # print(dali[0][1]["json"]["data"]["artwork"]["images"][0]["url"])
# TODO insert the id from 'https://d32dm0rphc51dk.cloudfront.net/dAMtqpwtIUgN0zlJpjYrmA/medium.jpg' into
#   "https://d32dm0rphc51dk.cloudfront.net/dAMtqpwtIUgN0zlJpjYrmA/dztiles/12/{}_{}.jpg"



def get_source(url):
    r = requests.get(url)
    return(r.content)

madonne = "https://www.artsy.net/artwork/salvador-dali-madonne"
source_string = get_source(madonne)

# cadeau = "https://www.artsy.net/artwork/man-ray-cadeau-1926"
# source_string = get_source(cadeau)
# https://d32dm0rphc51dk.cloudfront.net/HFgPe_vJgqATQdyClCvyMQ/medium.jpg

# fete = "https://www.artsy.net/artwork/marc-chagall-la-fete-autour-du-nu-rose"
# source_string = get_source(fete)

f = open('source_code.html', 'wb')
f.write(source_string)
f.close()

with open('source_code.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')
    
substring = "RELAY"
for block in soup.find_all('script'):
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