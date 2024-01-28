import os
import datetime as dt
import requests
from dotenv import load_dotenv


load_dotenv()
APP_ID = os.environ.get("APP_ID")
NT_APP_KEY = os.environ.get("NUTRITIONIX_API_KEY")
GENDER = os.environ.get("GENDER")
WEIGHT = os.environ.get("WEIGHT")
HEIGHT = os.environ.get("HEIGHT")
AGE = os.environ.get("AGE")

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")


def fetch_nlp_exercise() -> dict:
    url = "https://trackapi.nutritionix.com/v2/natural/exercise"
    exercises = input("Tell me which exercises you did: ")

    params = {
        "query": exercises,
        "gender": GENDER,
        "weight_kg": WEIGHT,
        "height_cm": HEIGHT,
        "age": AGE,
    }
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": NT_APP_KEY,
    }

    response = requests.post(url=url, json=params, headers=headers)
    return response.json()


def parse_exercises(exercises: dict) -> list[dict]:
    out_exercises = []
    for exercise in exercises["exercises"]:
        ex = {
            "date": dt.datetime.now().strftime("%d/%m/%Y"),
            "time": dt.datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
        out_exercises.append(ex)
    return out_exercises


def update_gsheet(data: list[dict]) -> None:
    url = "https://api.sheety.co/f9fdaf98474328d12f342ab85067a027/myWorkouts/workouts"
    for exc in data:
        workout = {
            "workout": {
                "date": exc["date"],
                "time": exc["time"],
                "exercise": exc["exercise"],
                "duration": exc["duration"],
                "calories": exc["calories"],
            }
        }
        headers = {
            "Authorization": f"Bearer {SHEETY_TOKEN}",
            "Content-Type": "application/json",
        }
        response = requests.post(url=url, json=workout, headers=headers)
        print(response.text)


def main():
    exercises = fetch_nlp_exercise()
    parsed_exercises = parse_exercises(exercises)
    update_gsheet(parsed_exercises)


if __name__ == "__main__":
    main()
