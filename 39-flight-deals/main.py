from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

gsheet = DataManager()
sheet_data = gsheet.get_flights()["prices"]
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA_CODE = "LON"

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        gsheet.update_iata_code(row["id"], row["iataCode"])


tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.search_flights(
        ORIGIN_CITY_IATA_CODE, destination["iataCode"], tomorrow, six_month_from_today
    )
    if flight.price < destination["lowestPrice"]:
        notification_manager.notify(
            message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to"
            f" {flight.destination_city}-{flight.destination_airport}, "
            f"from {flight.out_date} to {flight.return_date}."
        )
