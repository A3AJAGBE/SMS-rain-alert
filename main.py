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
print(half_day_weather)

