
import requests
from bs4 import BeautifulSoup
import json


def image_scraper(url):

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
    url = input("Enter a website: ")
    results = image_scraper(url)
    print(results)