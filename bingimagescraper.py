import requests
from bs4 import BeautifulSoup
from flask import jsonify


def image_scraper(query):
    """scrapes user search term for all images via bing image search
    :param http url ex. https://www.cookinglight.com
    :return dictionary key:alt text; value: source link"""
    adlt = 'moderate'
    search = query.strip()
    search = search.replace(' ', '+')
    url = 'https://bing.com/images/search?q=' + search + '&safeSearch=' + adlt
    print("\nsearch url:", url, "\n")
    # A user agent is a computer program representing a person; https://developer.mozilla.org/en-US/docs/Glossary/User_agent
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    headers = {"user-agent": USER_AGENT}
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.content, "html.parser")
    print(soup)
    image_dict = {}
    # finds image links
    images = soup.find_all('a', class_='iusc')
    for i in images:
        try:
            img_url = eval(i['m'])['murl']
            # parse link to pull out a title
            img_title = img_url.split("/")[-1]
            img_title = img_title.split(".")[0]
            image_dict[img_title] = img_url
            #print(img_title,':', img_url)
        except:

            pass
    return image_dict




if __name__ == "__main__":
    query = input("Enter a search term for your image: ")
    results = image_scraper(query)
    print(results)