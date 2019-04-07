from geopy.geocoders import Nominatim
from ruamel import yaml
import json
with open('settings.json') as json_data_file:
    config = json.load(json_data_file)
    print(config["Settings"]["App"][0]["AppName"])

class GeoService:
    geo_locator = Nominatim(user_agent = config.Settings.App.AppName)
    locations = {}

    def __init__(self, locations):
        self.locations = self.get_all_locations

    def update_location(self, name, address):
        self.locations.update({name : address})
        return True

    def remove_location(self, name):
        try:
            self.locations.pop(name)
            return True
        except KeyError:
            return False

    def get_location(self, name):
        return self.locations.get(name)

    @staticmethod
    def get_all_locations(self):
        f = open('locations.yaml', 'r')
        return yaml.safe_load(f)

    def save_all_locations(self):
        with open('locations.yaml', 'w') as file:
            yaml.dump(self.locations, file)  # Write a YAML representation of data to 'locations.yaml'.

    def update_location(self, name, zipcode, housenumber):
        new_location = self.geo_locator.geocode(f"{zipcode} {housenumber}")
        self.update_location(name, new_location)
        return True







# def add_location(name, address):
#     locations[name] = address
#     return True
# updates or adds the location