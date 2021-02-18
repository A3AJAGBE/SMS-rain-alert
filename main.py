import os
import requests
from dotenv import load_dotenv
load_dotenv()

OMW_KEY = os.environ.get("OMW_API_KEY")
OMW_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall?"

parameters = {
    "lat": os.environ.get("LAT"),
    "lon": os.environ.get("LONG"),
    "appid": OMW_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(OMW_ENDPOINT, params=parameters)
response.raise_for_status()

# Get the weather data
data = response.json()

# Get the data for the first 12 hours
half_day_weather = data['hourly'][:12]

# Get the condition of the next 12 hours
for hr_condition in half_day_weather:
    half_day_condition = hr_condition['weather'][0]['id']
    print(half_day_condition)