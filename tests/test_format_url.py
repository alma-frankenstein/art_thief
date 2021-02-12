from format_url import parse_source_code, json_bootstrap, image_json
import pytest


# def test_amend_dz_url_single_digit():
#     url = "https://d32dm0rphc51dk.cloudfront.net/JQI2YbnwwGCiT7dHH41_9A/dztiles/13/{}_{}.jpg"
#     new_dz_num = 7
#     assert amend_dz_url(
#         url, new_dz_num) == "https://d32dm0rphc51dk.cloudfront.net/JQI2YbnwwGCiT7dHH41_9A/dztiles/7/{}_{}.jpg"


# def test_amend_dz_url_single_digit_str():
#     url = "https://d32dm0rphc51dk.cloudfront.net/JQI2YbnwwGCiT7dHH41_9A/dztiles/13/{}_{}.jpg"
#     new_dz_num = "7"
#     assert amend_dz_url(
#         url, new_dz_num) == "https://d32dm0rphc51dk.cloudfront.net/JQI2YbnwwGCiT7dHH41_9A/dztiles/7/{}_{}.jpg"

# --------------------
# def get_source(url):
#     r = requests.get(url)
#     return(r.content)


# def parse_source_code(source_string):
#     with open('source_code.html', 'wb') as file_obj:
#         file_obj.write(source_string)
        
#     with open('source_code.html') as fp:
#         soup = BeautifulSoup(fp, 'html.parser')
#     return soup
    
    
# def json_bootstrap(parsed_html, substring):  
#     for block in parsed_html.find_all('script'):
#         if substring in str(block):
#             bootstrap_string = block.string.strip()
#             bootstrap_string = bootstrap_string.replace("var __RELAY_BOOTSTRAP__ = ", "")   
#             bootstrap_string = bootstrap_string[:-1]
#             bootstrap_json = json.loads(json.loads(bootstrap_string))
#             # with open('output.json', 'w') as f:
#             #     f.write(json.dumps(bootstrap_json, indent=4))    # only need one of these
#             return bootstrap_json
            
            
# def image_json(artsy_url):  
#     source_string = get_source(artsy_url)
#     the_soup = parse_source_code(source_string)
#     return(json_bootstrap(the_soup, "RELAY"))