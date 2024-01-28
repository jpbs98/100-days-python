import os
from dotenv import load_dotenv
import requests
from flight_data import FlightData

load_dotenv()
TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")


class FlightSearch:
    def __init__(self):
        self.endpoint = "https://tequila-api.kiwi.com"
        self.headers = {
            "apikey": TEQUILA_API_KEY,
        }
        self.params = {
            "term": "city",
            "location_types": "city",
        }
        self.iata_code = ""
        self.city = ""
        self.country = ""

    def get_destination_code(self, city):
        url = f"{self.endpoint}/locations/query"
        self.params["term"] = city
        response = requests.get(url=url, params=self.params, headers=self.headers)
        data = response.json()["locations"]
        self.iata_code = data[0]["code"]
        return self.iata_code

    def search_flights(
        self, origin_city_code, destination_city_code, from_time, to_time
    ):
        url = f"{self.endpoint}/v2/search"
        params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP",
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0],
        )
        return flight_data
