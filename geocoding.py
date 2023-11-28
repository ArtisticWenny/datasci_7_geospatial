import requests
import requests
import pandas as pd
import numpy as np
import re
import geopandas as gpd
import matplotlib.pyplot as plt
import urllib.parse
import os
import json

df = pd.read_csv('/home/jason_tang/datasci_7_geospatial/data/assignment7_slim_hospital_addresses.csv')
list_of_addresses = df['NAME'] + ', ' + df['ADDRESS'] + ', ' + df['CITY'] + ', ' + df['STATE']

for x in list_of_addresses:
    api_key = os.getenv("GOOGLE_MAPS_API")
google_response = []

for address in list_of_address: 
    api_key = os.getenv(api_key)

    search = 'https://maps.googleapis.com/maps/api/geocode/json?address='
    location = x

    location_cleaned = urllib.parse.quote(location)
    location_raw = address
    location_clean = urllib.parse.quote(location_raw)

    url_request_part1 = search + location_cleaned + '&key=' + api_key
    url_request_part1 = search + location_clean + '&key=' + api_key
    url_request_part1

    response = requests.get(url_request_part1)

    json = response.json()
    response_dictionary = response.json()

    lat_long = response_dictionary['results'][0]['geometry']['location']
    lat_response = lat_long['lat']
    lng_response = lat_long['lng']

    final = {'address': address, 'lat': lat_response, 'lon': lng_response}
    google_response.append(final)

    lat_long = response['results'][0]['geometry']['location']
    lat = location['lat']
    lng = location['lng']
    print(f'....finished with {address}')

    print(f'Address: {location}, Lat: {lat}, Lng: {lng} ')

df2 = pd.DataFrame(google_response)
