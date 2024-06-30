#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch

if __name__ == '__main__':
    sheet_data = DataManager()
    fs = FlightSearch()
    pprint(sheet_data.prices)
    for price in sheet_data.prices:
        if price["iataCode"] == "":
            city = price["city"]
            price["iataCode"] = fs.get_iata_code(city)
            sheet_data.update_row(price)
