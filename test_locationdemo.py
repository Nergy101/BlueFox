from geopy.geocoders import Nominatim
from ruamel import yaml
from geo.Location import Location

geolocator = Nominatim(user_agent="locationTryOut")
home_location = geolocator.geocode("Tweede Westerparklaan 202")
work_location = geolocator.geocode("Atoomweg 63")
print(home_location.raw)
print(home_location.address)
# print((home_location.latitude, home_location.longitude))
# print(work_location.raw)
print(work_location.address)
# print((work_location.latitude, work_location.longitude))

home_location = home_location.address
work_location = work_location.address
data = [home_location, work_location]

with open('document.yaml', 'w') as file:
    yaml.dump(data, file)    # Write a YAML representation of data to 'document.yaml'.


f = open('document.yaml', 'r')
addresses = yaml.safe_load(f)
print()
print(addresses)

new_location = geolocator.geocode("Tweede Westerparklaan 202")
print(type(new_location))
print(new_location.latitude, new_location.longitude, new_location.address)

l = Location('a', "weede Westerparklaan", "202", new_location.latitude, new_location.longitude, new_location.address)
if type(l) == Location:
    print(type(l)== Location)