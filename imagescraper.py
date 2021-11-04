# sources: https://www.youtube.com/watch?v=stIxEKR7o-c
# https://github.com/jhnwr/image-downloader/blob/main/imagedownloader.py
# https://dev.to/swarnimwalavalkar/build-and-deploy-a-rest-api-microservice-with-python-flask-and-docker-5c2d
import urllib

import requests
from bs4 import BeautifulSoup
import base64
from oauthlib.common import urlencode, urldecode
from urllib.parse import urlencode, quote_plus

from requests.utils import requote_uri
from urllib import *

def image_scraper(site):
    """scrapes user inputed url for all images on a website and
    :param http url ex. https://www.cookinglight.com
    :return dictionary key:alt text; value: source link"""
    search = site.strip()
    search = search.replace(' ', '+')
    url = 'http://' + search

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    # create dictionary to add image alt tag and source link
    images = {}
    for img in img_tags:
        try:
            name = img['alt']
            link = img['src']
            images[name] = link
        except:
            pass
    return images
    #return json.dumps(images, indent=4)




if __name__ == "__main__":
    url = input("Enter a website starting with the www.: ")
    results = image_scraper(url)
    print(results)