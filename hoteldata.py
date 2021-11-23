

api_key = " " #Input your own Google Places Api Key here

import requests
from requests.exceptions import HTTPError


def get_hotel_data(query):
	"""Uses Google Places API to return hotel information for a specified city"""
	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

	try:
		response = requests.get(url + 'query=' + query + '&key=' + api_key)
		response.raise_for_status()
		# access JSON content
		jsonResponse = response.json()
		# grabs hotel info
		result = jsonResponse['results']
		hotel_data = []
		for i in range(len(result)):
			hotel_data.append([result[i]['name'], result[i]['rating'], result[i]['formatted_address']])
		return hotel_data

	except HTTPError as http_err:
		print(f'HTTP error occurred: {http_err}')
	except Exception as err:
		print(f'Other error occurred: {err}')


