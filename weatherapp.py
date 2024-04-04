import requests
import os
from pprint import pprint
from dotenv import load_dotenv, dotenv_values

load_dotenv()

city = input("Enter a city: ")

key = os.getenv("WEATHER_KEY")

base_url = "http://api.openweathermap.org/data/2.5/weather?appid=" + key + "&q="+ city

weather_data = requests.get(base_url).json()

pprint(weather_data)