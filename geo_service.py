from geopy.geocoders import Nominatim
from location import Location
from termcolor import colored

import sys
import json

with open('settings.json') as json_data_file:
    config = json.load(json_data_file)


def from_json(json):
    return Location(json['name'], json['street'], json['house_number'], json['lat'], json['lon'], json['display_name'])


class GeoService:
    geo_locator = Nominatim(user_agent=config["Settings"]["App"][0]["AppName"])
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
        return from_json(json.loads(self.locations.get(name)))

    @staticmethod
    def get_all_locations_json():
        try:
            return [json.loads(location) for location in json.load(open('locations.json', 'r')).values()]
        except FileNotFoundError:
            print("No locations.json file found")

    @staticmethod
    def get_all_locations():
        try:
            return [from_json(json.loads(location)) for location in json.load(open('locations.json', 'r')).values()]
        except FileNotFoundError:
            print("No locations.json file found")

    def save_all_locations(self):
        try:
            with open('locations.json', 'w') as file:
                json.dump(self.locations, file)
                print(f"\n{colored('***SAVED LOCATIONS TO SYSTEM***', attrs=['reverse', 'blink'])}\n")

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
            new_location_json = Location(name,
                                         street,
                                         house_number,
                                         new_location.latitude,
                                         new_location.longitude,
                                         new_location.address).to_json()

            self.locations.update({name: new_location_json})
            return True
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
