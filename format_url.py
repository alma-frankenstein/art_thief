import requests

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


madonne = "https://www.artsy.net/artwork/salvador-dali-madonne"

def get_source(url):
    r = requests.get(url)
    return(f"{r.content}")

source_string = get_source(madonne)
# source_string.save("source_string.py")
# cropped_image.save("img.png")

# print(get_source(madonne))

def get_relay_bootstrap(souce_code):
    pass

# looks like this: 
    # <script>
    #   var __RELAY_BOOTSTRAP__ = "[[\"{\\\"queryID\\\":\\\"artworkRoutes_ArtworkQuery\\\",\\\"variables\\\":{\\\"artworkID\\\":\\\"salva...
    # </script>
    
    # so, everything between 'var' and '</script>'
    # var __RELAY_BOOTSTRAP__ = "[[\\"{\\\\\\"queryID\\\\\\":\\\\\\"artworkRoutes_ArtworkQuery\\\\\\",\\\\\\"variables\\\\\\":{\\\\\\"artworkID\\\\\\":\\\\\\"salvador-dali-madonne" </script>