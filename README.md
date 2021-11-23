# Portfolio Project for CS361 Software Engineering 

#### 1. Created a Travel Application that employs a teammate's weather microservice as well as a Yelp API and Image Scraper API to obtain data.
#### 2. Created two Image scrapper microservices to be utilized by teammate's applications:
   - bingimagescrapper.py Scrapes Bing images by passing in a search query. Returns the first 35 images corresponding to the query.
   - imagescrapper.py Scrapes any website by passing in the website's url. Returns all images on the website.

#### My Travel Application was created via Python and Tkinter.
#### My Image Scraper API was created via Python, Beautiful Soup and Flask REST API. It uses Heroku as it's server. 
## Bing Image Search Scraper Usage
#### Access it at https://jaclynsimagescraper.herokuapp.com/
#### API Request GET https://jaclynsimagescraper.herokuapp.com/ImageSearchTermHere
##### For example https://jaclynsimagescraper.herokuapp.com/tomatosouprecipes
##### Returns { image title : image.jpg }
##  Website Image Scraper Usage
#### View Repository for image scraper and heroku deployment at https://github.com/jaclynpgh/imagescraper
#### API Request GET https://websiteimagescraper.herokuapp.com/AddWebsiteToScrapeHere
##### For example https://websiteimagescraper.herokuapp.com/https://www.cookinglight.com/recipes/vegetarian-green-curry-stew
##### Returns { image title : image.jpg }

## Integration
#### A video showcasing how I integrated my teammate's microservices into my project:
https://vimeo.com/644174803

## Project Showcase
<div style="padding:67.92% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/649264258?h=01f64310e6&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="CS361 Portfolio Project: Micro Travel Agent"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>
