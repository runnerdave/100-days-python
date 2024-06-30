import os
import requests
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
FLIGHTS_SHEET_URL = os.environ.get("SHEETY_END_POINT_FLIGHTS")

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.prices = self.get_prices()

    def prices(self):
        return self.prices

    def get_prices(self):
        headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}",
        }
        response = requests.get(url=FLIGHTS_SHEET_URL, headers=headers, verify=False)
        response.raise_for_status()
        return response.json()["prices"]
    
    def update_row(self, price):
        headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}",
        }
        id = price["id"]
        body = {
            "price": price
        }
        response = requests.put(url=f"{FLIGHTS_SHEET_URL}/{id}", json=body, headers=headers, verify=False)
        response.raise_for_status()
        return response.json()

    def get_flights_spreadsheet(self):
        headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}",
        }
        response = requests.get(url=FLIGHTS_SHEET_URL, headers=headers, verify=False)
        response.raise_for_status()
        return response.text

    def __repr__(self):
        return self.get_flights_spreadsheet()
    
