# https://pynative.com/parse-json-response-using-python-requests-library/
import requests
from requests.exceptions import HTTPError


def get_imageAPI(index, query):
    """:param index (int) for parsing json and getting different images
    :param query (string) search term to scrape corresponding images"""

    imageAPI_url = 'https://jaclynsimagescraper.herokuapp.com/'
    query = query.replace(' ', '+')
    try:
        response = requests.get(imageAPI_url + query)
        response.raise_for_status()
        # access JSON content
        jsonResponse = response.json()
        # grabs image url from json based on index
        image = list(jsonResponse.values())[index]
        return image

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')


def get_yelp_info(city, state):
    """Sam's microservice to return Yelp restaurant info"""
    imageAPI_url = 'https://yelp-sc.herokuapp.com/'
    try:
        response = requests.get(imageAPI_url + city + state)
        response.raise_for_status()
        # access JSON content
        jsonResponse = response.json()
        # grabs yelp info
        yelp_info = jsonResponse
        return yelp_info

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

def get_weather(city):
    """Bailey's microservice to return weather data, must be VPNed in to OSU server"""
    weather_url = 'http://flip1.engr.oregonstate.edu:5454/?city='
    try:
        response = requests.get(weather_url + city)
        response.raise_for_status()
        # access JSON content
        jsonResponse = response.json()
        # parse data from json
        forecast = jsonResponse['weather'][0]['main']
        current = jsonResponse['weather'][0]['description']
        temp_k = jsonResponse['main']['temp']
        temp_f = (temp_k - 273.15) * 9//5 + 32
        weather_data = [forecast, current, temp_f]

        return weather_data

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

