import os
from dotenv import load_dotenv
import requests

load_dotenv()
SHEETY_PRICES_ENDPOINT = (
    "https://api.sheety.co/f9fdaf98474328d12f342ab85067a027/flightDeals/prices"
)
headers = {"Authorization": f"Bearer {os.environ.get("SHEETY_TOKEN")}"}


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}", json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = (
            "https://api.sheety.co/f9fdaf98474328d12f342ab85067a027/flightDeals/users"
        )
        response = requests.get(url=customers_endpoint, headers=headers)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
