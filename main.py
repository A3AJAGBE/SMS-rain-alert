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
data = response.json()
print(data)