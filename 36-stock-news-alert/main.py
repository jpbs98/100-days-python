import os
from datetime import date, timedelta
from dotenv import load_dotenv
import requests
from twilio.rest import Client


load_dotenv()
AV_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER")
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")

STOCK = "TSLA"
COMPANY_NAME = "Tesla"


def fetch_stock_close_daily_diff() -> dict:
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "outputsize": "compact",
        "datatype": "json",
        "apikey": AV_API_KEY,
    }

    url = "https://www.alphavantage.co/query"
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def parse_stock_data(stock_info: dict) -> tuple[bool, float, str]:
    yesterday = str(date.today() - timedelta(days=1))
    previous_day = str(date.today() - timedelta(days=2))
    yesterday_close = float(stock_info["Time Series (Daily)"][yesterday]["4. close"])
    previous_close = float(stock_info["Time Series (Daily)"][previous_day]["4. close"])
    diff = yesterday_close - previous_close
    if diff > 0:
        icon = "🔺"
    else:
        icon = "🔻"
    abs_diff = abs(yesterday_close - previous_close)
    diff_percent = (abs_diff / yesterday_close) * 100
    return abs_diff >= yesterday_close * 0.05, diff_percent, icon


def fetch_news() -> list:
    params = {
        "qInTitle": COMPANY_NAME,
        "from": str(date.today() - timedelta(days=1)),
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY,
    }
    url = "https://newsapi.org/v2/everything"
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["articles"][:3]


def parse_news(news: list) -> list[dict]:
    processed_news = []
    for article in news:
        processed_article = {
            "title": article["title"],
            "description": article["description"],
        }
        processed_news.append(processed_article)
    return processed_news


def notify(info_to_send: list[dict], percent_diff: float, icon: str) -> None:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    for article in info_to_send:
        message = client.messages.create(
            body=f"{COMPANY_NAME}: {icon} {int(percent_diff)}%\n"
            f"Headline: {article["title"]}.\n"
            f"Brief: {article["description"]}.",
            from_=TWILIO_PHONE_NUMBER,
            to=PHONE_NUMBER,
        )
        print(message.status)


def main():
    stock_close_data = fetch_stock_close_daily_diff()
    stock_is_changed, diff, icon = parse_stock_data(stock_close_data)
    if stock_is_changed:
        news_data = fetch_news()
        condensed_news = parse_news(news_data)
        notify(condensed_news, diff, icon)


if __name__ == "__main__":
    main()
