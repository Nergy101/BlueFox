from geopy.geocoders import Nominatim
from ruamel import yaml
from location import Location

import sys, json

config = ""

with open('settings.json') as json_data_file:
    config = json.load(json_data_file)
    print(config["Settings"]["App"][0]["AppName"])


class GeoService:
    geo_locator = Nominatim(user_agent = config["Settings"]["App"][0]["AppName"])
    locations = {}

    def __init__(self):
        None

    def remove_location(self, name):
        try:
            self.locations.pop(name)
            return True
        except KeyError:
            return False

    def get_location(self, name):
        return self.locations.get(name)

    @staticmethod
    def get_all_locations():
        try:
            return yaml.safe_load(open('locations.yaml', 'r'))
        except FileNotFoundError:
            print("No locations.yaml file found")

    def save_all_locations(self):
        try:
            with open('locations.yaml', 'w') as file:
                yaml.dump(self.locations, file)  # Write a YAML representation of data to 'locations.yaml'.
                print("saved locations")
        except IOError:
            print("Unexpected error:"), sys.exc_info()[0]
            raise

    # update_location and overloads
    def update_location(self, name, location):
        return True if (self.locations.update({name: location}) if (type(location) == Location) else False)\
                       is None else False

    def add_location(self, name, street, house_number):
        try:
            new_location = self.geo_locator.geocode(f"{street} {house_number}")
            self.update_location(name, (Location(name, street, house_number, new_location.latitude, new_location.longitude, new_location.address)))
            return True
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
