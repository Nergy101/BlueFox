import json
from motd import Gif
from motd import WeatherReport

# Do this sometime
# def from_json(json):
#     return Motd(json['weather_report']['date'], for GifGif(json['gif']['title'], json['gif']['bitly_gif_url']), WeatherReport(json['weather_report']['date'], json['weather_report']['place_name'], json['weather_report']['degrees_c'], json['weather_report']['description']))


class Motd:
    def __init__(self, gif_list, weather_report):
        self.date = WeatherReport.date
        self.gif_list = gif_list
        self.weather_report = weather_report

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
