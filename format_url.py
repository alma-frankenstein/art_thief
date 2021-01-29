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
# TODO insert the id into 'https://d32dm0rphc51dk.cloudfront.net/{ID}/larger.jpg'


def get_source(url):
    r = requests.get(url)
    return(r.content)

# def string_escape(s, encoding='utf-8'):
#     return (s.encode('latin1')         # To bytes, required by 'unicode-escape'
#              .decode('unicode-escape') # Perform the actual octal-escaping decode
#              .encode('latin1')         # 1:1 mapping back to bytes
#              .decode(encoding))  


madonne = "https://www.artsy.net/artwork/salvador-dali-madonne"
source_string = get_source(madonne)

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
        bootstrap_json = json.loads(json.loads((bootstrap_string))
        pprint(bootstrap_json)
        print(bootstrap_json[0][1]["json"]["data"]["artwork"]["images"][0]["url"])

