from geo.geo_service import GeoService, list_all_locations, get_distance
from termcolor import colored
from tqdm import tqdm

import requests
import json

with open('settings.json') as json_data_file:
    config = json.load(json_data_file)

print(colored(config["Settings"]["App"]["AppName"], 'red', attrs=['reverse', 'bold', 'blink']))
W_API_KEY = config["Settings"]["Api"]["WeatherApiKey"]  # secure this some time


geo_service = GeoService()

geo_service.add_location("thuis", "Tweede Westerparklaan", "202")
geo_service.add_location("vriendin", "Mondriaanerf", "19")
geo_service.add_location("werk", "Atoomweg", "63")

geo_service.save_all_locations()

#
# for i in range(1,11):
#     geo_service.add_location(f"thuis{str(i)}", "Tweede Westerparklaan", "202")


[print(name) for name in tqdm(list_all_locations())]  # use tqdm as list grows


a = geo_service.get_location("vriendin")
b = geo_service.get_location("werk")
#
print(f"Van {a.name} naar {b.name} is {round(get_distance((a.lat, a.lon), (b.lat, b.lon)).kilometers, 2)} km")
#
# print('Locations')
# for l in geo_service.get_all_locations():
#     print("- "+l.name+": "+l.display_name)

response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast/daily?lat={a.lat}&lon={a.lon}&cnt={1}&APPID={W_API_KEY}")
weather = response.json()
degrees = (weather['list'][0]['deg'] - 32)/1.8
print(f"Weather of today at {weather['city']['name']}:")
print(f"{weather['list'][0]['weather'][0]['description']}, {round(degrees, 1)} C")
#
# geo_service.save_all_locations()

