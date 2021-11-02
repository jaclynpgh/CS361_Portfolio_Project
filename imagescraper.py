
import requests
from bs4 import BeautifulSoup
import json


def image_scraper(url):
    """scrapes user inputed url for all images on a website and
    :param http url ex. http://www.cookinglight.com
    :return dictionary key:alt text; value: source link"""
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
    return json.dumps(images, indent=4)


if __name__ == "__main__":
    url = input("Enter a website formatted with 'http://': ")
    results = image_scraper(url)
    print(results)