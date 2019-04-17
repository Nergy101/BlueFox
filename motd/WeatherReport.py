import json


class WeatherReport:
    def __init__(self, date, place_name, degrees_c, description):
        self.date = date
        self.place_name = place_name
        self.degrees_c = degrees_c
        self.description = description

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


def from_json(json):
    return WeatherReport(json['date'], json['place_name'], json['degrees_c'], json['description'])