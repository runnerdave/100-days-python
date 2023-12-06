import requests
import os
from twilio.rest import Client
import urllib3
# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# twilio
twilio_account_sid = os.environ.get("twilio_account_sid")
twilio_auth_token = os.environ.get("twilio_auth_token")

OPENWEATHER_API = "https://api.openweathermap.org/data/2.5/forecast"

latitude = -37.823250
longitude = 144.959744
entries = 4
open_weather_api_key = os.environ.get("open_weather_api_key")

# Get the weather data
parameters = {"lat": latitude, "lon": longitude, "appid": open_weather_api_key, "cnt": entries}
response = requests.get(url=OPENWEATHER_API, params=parameters, verify=False)
response.raise_for_status()
data = response.json()

status_code = data["cod"]
weather_id = data["list"][0]["weather"][0]["id"]
print("status", status_code, "weather_id", weather_id)

if int(weather_id) < 900:
    client = Client(twilio_account_sid, twilio_auth_token)

    message = client.messages.create(
        from_='+14322017247',
        body='Hablame 🗣️',
        to='+61422521841'
    )
    print(message.status)

weather_id_list = []

for i in range(0, entries):
    weather_id_list.append(data["list"][i]["weather"][0]["id"])
    weather_list_length = len(data["list"][i]["weather"])
    if weather_list_length > 1:
        weather_id_list = []
        for j in range(1, weather_list_length):
            weather_id_list.append(data["list"][i]["weather"][j]["id"])
        
print(weather_id_list)
