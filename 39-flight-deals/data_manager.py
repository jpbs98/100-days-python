import os
from dotenv import load_dotenv
import requests


load_dotenv()
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")


class DataManager:
    def __init__(self):
        self.headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}",
            "Content-Type": "application/json",
        }

    def get_flights(self):
        url = (
            "https://api.sheety.co/f9fdaf98474328d12f342ab85067a027/flightDeals/prices"
        )

        response = requests.get(url=url, headers=self.headers)
        return response.json()

    def update_iata_code(self, id, iata_code):
        url = (
            "https://api.sheety.co/f9fdaf98474328d12f342ab85067a027/flightDeals/prices/"
            + str(id)
        )
        body = {
            "price": {
                "iataCode": iata_code,
            }
        }
        response = requests.put(url=url, json=body, headers=self.headers)
        response.raise_for_status()
