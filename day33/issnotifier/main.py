import time
import requests
from datetime import datetime
import urllib3
# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

MY_LAT = -37.766410  # Your latitude
MY_LONG = 144.960980  # Your longitude


# Your position is within +5 or -5 degrees of the ISS position.

def is_iss_overhead(my_lat=MY_LAT, my_lng=MY_LONG, error=5):
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print("iss_latitude:", iss_latitude, "iss_longitude:", iss_longitude)
    
    if (abs(my_lat - iss_latitude) <= error) and (abs(my_lng - iss_longitude) <= error):
        return True
    
    return False

def is_night(lat=MY_LAT, lng=MY_LONG):
    parameters = {
        "lat": lat,
        "lng": lng,
        "formatted": 0,#comes in utc
    }

    response = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()
    sunrise = datetime.fromisoformat(data["results"]["sunrise"])
    sunset = datetime.fromisoformat(data["results"]["sunset"])

    time_now = datetime.utcnow()
    return (sunrise.hour >= time_now.hour >= sunset.hour)

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    print("iss is overhead?", is_iss_overhead(error=100))
    print("is night?", is_night())
    if is_iss_overhead() and is_night():
        print("send email")
    time.sleep(60)
