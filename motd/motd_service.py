import json, requests
import geo.Location as location
import datetime
from motd import WeatherReport
from motd import Gif
from motd import Motd

with open('settings.json') as json_data_file:
    config = json.load(json_data_file)

W_API_KEY = config["Settings"]["Api"]["WeatherApiKey"]  # secure this some time
G_API_KEY = config["Settings"]["Api"]["GiphyApiKey"]  # secure this some time


def get_weather_report(location: location):
    weather = requests.get(f"https://api.openweathermap.org/data/2.5/forecast/daily?lat={location.lat}&lon={location.lon}&cnt={1}&APPID={W_API_KEY}").json()
    degrees = round(((weather['list'][0]['deg'] - 32) / 1.8), 1)
    description = weather['list'][0]['weather'][0]['description']

    return WeatherReport(datetime.datetime.now(), location.name, degrees, description)


def get_trending_gifs():
    gifs = requests.get(f"https://api.giphy.com/v1/gifs/trending?api_key={G_API_KEY}&limit=5&rating=R").json()['data']
    return[Gif(gif["title"], gif["bitly_gif_url"]) for gif in gifs]


def get_motd():
    return Motd(get_trending_gifs(), get_weather_report())

# Save, Load, (by weather_report.name)
