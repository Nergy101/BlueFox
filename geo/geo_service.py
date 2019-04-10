from geopy.geocoders import Nominatim
from geopy.distance import distance
from geo.location import Location
from termcolor import colored

import sys
import json

with open('settings.json') as json_data_file:
    config = json.load(json_data_file)


def from_json(json):
    return Location(json['name'], json['street'], json['house_number'], json['lat'], json['lon'], json['display_name'])


def get_all_locations():
    try:
        a = [from_json(json.loads(location)) for location in json.load(open('locations.json', 'r')).values()]
        return a if a else None
    except FileNotFoundError:
        print("No locations.json file found")
        raise


def list_all_locations():
    try:
        return [location.name for location in get_all_locations()]
    except FileNotFoundError:
        print("No locations.json file found")

def get_all_locations_json():
    try:
        return [json.loads(location) for location in json.load(open('locations.json', 'r')).values()]
    except FileNotFoundError:
        print("No locations.json file found")


def get_distance(from_location: (int, int), to_location: (int, int)):
    return distance((from_location[0], from_location[1]), (to_location[0], to_location[1]))


class GeoService:
    geo_locator = Nominatim(user_agent=config["Settings"]["App"]["AppName"])
    locations = {}

    def __init__(self):
        None

    def load_all_locations(self):
        self.locations = get_all_locations()

    def remove_location(self, name):
        try:
            self.locations.pop(name)
            return True
        except KeyError:
            return False

    def get_location(self, name):
        return from_json(json.loads(self.locations.get(name)))  #gets string from file, to json, to location object
        # for location in self.locations:
        #     print(type(location))
        # return [location for location in self.locations if location.name == name][0]

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
