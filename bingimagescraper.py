import requests
from bs4 import BeautifulSoup
import json

def image_scraper(query):
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
    image_dict = {}
    # finds image links
    images = soup.find_all('a', class_='iusc')
    for i in images:
        try:
            img_url = eval(i['m'])['murl']
            img_title = img_url.split("/")[-1]
            image_dict[img_title] = img_url
           # print(img_title,':', img_url)
        except:

            pass

    return json.dumps(image_dict, indent=4)




if __name__ == "__main__":
    query = input("Enter a search term for your image: ")
    results = image_scraper(query)
    print(results)