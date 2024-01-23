import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client


load_dotenv()
OPEN_WEATHER_API_KEY = os.environ.get("API_KEY")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")
LONDON_LAT = 51.507351
LONDON_LONG = -0.127758


def fetch_forecast(lat: float, long: float) -> dict:
    params = {
        "lat": lat,
        "lon": long,
        "appid": OPEN_WEATHER_API_KEY,
        "units": "metric",
        "cnt": 4,
    }
    response = requests.get(
        url="https://api.openweathermap.org/data/2.5/forecast", params=params
    )
    response.raise_for_status()
    return response.json()


def will_rain(forecast: dict) -> bool:
    for hour_interval in forecast["list"]:
        if hour_interval["weather"][0]["id"] < 700:
            return True
    return False


def notify_sms() -> None:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_=TWILIO_PHONE_NUMBER,
        to=PHONE_NUMBER,
    )
    print(message.status)


weather_forecast = fetch_forecast(LONDON_LAT, LONDON_LONG)
if will_rain(weather_forecast):
    notify_sms()
