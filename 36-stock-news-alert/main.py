import os
from datetime import date, timedelta
from dotenv import load_dotenv
import requests


load_dotenv()
AV_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def fetch_stock_close_daily_diff() -> dict:
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "outputsize": "compact",
        "datatype": "json",
        "apikey": AV_API_KEY
    }
    
    url = "https://www.alphavantage.co/query"
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
    

def parse_stock_data(stock_info: dict) -> tuple[bool, float]:
    yesterday = str(date.today() - timedelta(days=1))
    previous_day = str(date.today() - timedelta(days=2))
    yesterday_close = float(stock_info["Time Series (Daily)"][yesterday]["4. close"])
    previous_close = float(stock_info["Time Series (Daily)"][previous_day]["4. close"])
    diff = abs(yesterday_close - previous_close)
    diff_percent = (diff / yesterday_close) * 100
    print(diff)
    print(diff_percent)
    return 50 >= yesterday_close * 0.05, diff_percent
 

def fetch_news() -> dict:
    params = {
        "q": COMPANY_NAME,
        "from": str(date.today() - timedelta(days=1)),
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY
    }
    url = "https://newsapi.org/v2/everything"
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["articles"][:3]
    

def parse_news(news: dict) -> NotImplemented:
    pass


def main():
    stock_close_data = fetch_stock_close_daily_diff()
    stock_is_changed, diff = parse_stock_data(stock_close_data)
    print(diff)
    if stock_is_changed:
        news_data = fetch_news()
        

if __name__ == "__main__":
    main()



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

