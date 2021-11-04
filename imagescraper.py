# sources: https://www.youtube.com/watch?v=stIxEKR7o-c
# https://github.com/jhnwr/image-downloader/blob/main/imagedownloader.py
# https://dev.to/swarnimwalavalkar/build-and-deploy-a-rest-api-microservice-with-python-flask-and-docker-5c2d

import requests
from bs4 import BeautifulSoup
import urllib


def image_scraper(site):
    """scrapes user inputed url for all images on a website and
    :param http url ex. https://www.cookinglight.com
    :return dictionary key:alt text; value: source link"""
    search = site.strip()
    search = search.replace(' ', '+')

    website = 'https://' + search
    response = requests.get(website)

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