import json


class Location:

    def __init__(self, name, street, house_number, lat, lon, display_name):
        self.name = name
        self.street = street
        self.house_number = house_number
        self.lat = lat
        self.lon = lon
        self.display_name = display_name

    def to_string(self):
        return self.display_name

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


