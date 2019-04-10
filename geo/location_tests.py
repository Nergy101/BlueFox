from geo.geo_service import GeoService, list_all_locations, get_distance
from termcolor import colored

import json

with open('settings.json') as json_data_file:
    config = json.load(json_data_file)

print(colored(config["Settings"]["App"][0]["AppName"], 'red', attrs=['reverse', 'bold', 'blink']))

geo_service = GeoService()
geo_service.add_location("thuis", "Tweede Westerparklaan", "202")
geo_service.add_location("vriendin", "Mondriaanerf", "19")
geo_service.add_location("werk", "Atoomweg", "63")

geo_service.save_all_locations()

[print(name) for name in list_all_locations()]  # use tqdm as list grows

a = geo_service.get_location("vriendin")
b = geo_service.get_location("werk")

print(f"Van {a.name} naar {b.name} is {round(get_distance(a.coords, b.coords).kilometers, 2)} km")

# print('Locations')
# for l in geo_service.get_all_locations():
#     print("- "+l.name+": "+l.display_name)
