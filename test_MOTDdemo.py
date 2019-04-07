import requests, json

G_API_KEY = "xMqp15q3WXzVL1q0T8k6JMRQmD6SETe5"
W_API_KEY = "3e7479392874b48638d0847329f31fad"
lat = 52.09073739999999
lon = 5.121420100000023

print()
print()
print("Trending gifs of the day:")
response = requests.get(f"https://api.giphy.com/v1/gifs/trending?api_key={G_API_KEY}&limit=5&rating=R")
gifs = response.json()['data']
[print(gif["title"] + ", " + gif["bitly_gif_url"]) for gif in gifs]

print()

print("Good Job gif of the day:")
response = requests.get(f"https://api.giphy.com/v1/gifs/l4pSXGlTtOKwOIR3O?api_key={G_API_KEY}")
gif = response.json()['data']
print(gif["title"] + ", " + gif["bitly_gif_url"])

print()

print("Random gif of the day:")
response = requests.get(f"https://api.giphy.com/v1/gifs/random?api_key={G_API_KEY}&rating=R")
gif = response.json()['data']
print(gif["title"] + ", " + gif["bitly_gif_url"])

print()

response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast/daily?lat={lat}&lon={lon}&cnt={1}&APPID={W_API_KEY}")
weather = response.json()
print(f"Weather of today at {weather['city']['name']}:")
print(f"{weather['list'][0]['weather'][0]['description']}, {round(weather['list'][0]['deg'], 1)} graden F")

print()

city_name = 'Utrecht'
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&APPID={W_API_KEY}")
weather = response.json()
print(f"Weather of today at {city_name}:")
print(f"Curently there is a {weather['weather'][0]['description']}")

# api.openweathermap.org/data/2.5/forecast?id={city ID}

with open('settings.json') as json_data_file:
    config = json.load(json_data_file)
    print(config["Settings"]["App"][0]["AppName"])