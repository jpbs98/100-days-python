import random
import smtplib
import datetime as dt
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")


dates = pd.read_csv("birthdays.csv")
today = dt.datetime.today().date().strftime("%m-%d")


for index, row in dates.iterrows():
    date = (
        dt.datetime(year=row["year"], month=row["month"], day=row["day"])
        .date()
        .strftime("%m-%d")
    )
    if today == date:
        letter = random.choice(os.listdir("letter_templates"))
        with open(f"letter_templates/{letter}", "r", encoding="utf-8") as file:
            letter = file.read()
            letter = letter.replace("[NAME]", row["name"])
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)  # type: ignore
            connection.sendmail(
                from_addr=EMAIL,  # type: ignore
                to_addrs=row["email"],
                msg=f"Subject:Happy Birthday\n\n{letter}",
            )
