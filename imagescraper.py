import requests, shutil
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve, urlopen

query = input("Enter a search term for your image: ")
adlt = 'moderate'
search = query.strip()
search = search.replace(' ', '+')
url = 'https://bing.com/images/search?q=' + search + '&safeSearch=' + adlt
print(url)
# A user agent is a computer program representing a person; https://developer.mozilla.org/en-US/docs/Glossary/User_agent
USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent": USER_AGENT}
resp = requests.get(url, headers=headers)
results = []
soup = BeautifulSoup(resp.content, "html.parser")

# finds image links
links = soup.find_all('a', class_='iusc')

DIR = "Results"
if not os.path.isdir(DIR):
    print("[+] Creating Directory Named '{0}'".format(DIR))
    os.mkdir(DIR)
DIR = os.path.join(DIR, query.split()[0])
if not os.path.exists(DIR):
        os.mkdir(DIR)


for i in links:
    try:
        # req = requests.get(i)
        img_url = eval(i['m'])['murl']
        #img_title = img_url.split("/")[-1]
        print(img_url)

            #with open(img_title, 'wb') as img_file:
             #   shutil.copyfileobj(img_url, img_file)
              #  print(img_title, ' found')
    except:

        pass


