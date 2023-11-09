import requests
from datetime import datetime
import urllib3
# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SUNRISE_API = "https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400"
ISS_API = "http://api.open-notify.org/iss-now.json"

# ISS call
response = requests.get(url=ISS_API)

response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
# print(iss_position)

# translate latitude and longitude to an address here: https://www.latlong.net/Show-Latitude-Longitude.html

# SUNRISE call
parameters = {"lat": latitude, "lng": longitude, "formatted": 0}
response = requests.get(url=SUNRISE_API, params=parameters, verify=False)
response.raise_for_status()
data = response.json()
print(data["results"]["sunrise"])
print(data["results"]["sunset"])
sunset = datetime.fromisoformat(data["results"]["sunset"])
print(sunset.hour)
