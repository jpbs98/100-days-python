import requests


def fetch_data(amount=10, _type="boolean"):
    params = {
        "amount": amount,
        "type": _type,
    }
    url = "https://opentdb.com/api.php"
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return data["results"]
