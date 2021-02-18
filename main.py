import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# Open configs
OMW_KEY = os.environ.get("OMW_API_KEY")
OMW_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall?"

# Twilio configs
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

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

will_rain = False

# Get the condition of the next 12 hours
for hr_condition in half_day_weather:
    half_day_condition = hr_condition['weather'][0]['id']

    # Check will they will be rain
    if int(half_day_condition) < 700:
        will_rain = True

# Provide a feedback if there's rain
if will_rain:
    message = client.messages.create(
        body="Take an umbrella 🌂 on your way out, It is going to rain 🌧 today. From: A3AJAGBE RAIN ALERT",
        from_=os.environ.get('TWILIO_NUMBER'),
        to=os.environ.get('MY_NUMBER')
    )
