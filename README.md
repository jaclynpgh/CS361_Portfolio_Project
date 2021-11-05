# Portfolio Project for CS361 Software Engineering 

#### 1. Created a Travel Application that employs a teammate's mapping microservice as well as a Yelp API and Image Scraper API to obtain data.
#### 2. Created two Image scrapper microservices to be utilized by teammate's applications:
   - bingimagescrapper.py Scrapes Bing images by passing in a search query. Returns the first 35 images corresponding to the query.
   - imagescrapper.py Scrapes any website by passing in the website's url. Returns all images on the website.

#### My Travel Application was created via Python and Tkinter.
#### My Image Scraper API was created via Python, Beautiful Soup and Flask REST API. It uses Heroku as it's server. 
## Image Scraper Usage
#### Access it at https://jaclynsimagescraper.herokuapp.com/
#### API Request GET https://jaclynsimagescraper.herokuapp.com/ImageSearchTermHere
##### For example https://jaclynsimagescraper.herokuapp.com/tomatosouprecipes
##### Returns { image title : image.jpg }

