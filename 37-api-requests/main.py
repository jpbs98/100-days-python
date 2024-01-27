import os
import datetime as dt
from dotenv import load_dotenv
import requests

load_dotenv()
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
PIXELA_USER = os.environ.get("PIXELA_USERNAME")


# pixela_graph_endpoint = f"https://pixe.la/v1/users/{PIXELA_USER}/graphs"
# graph_config = {
#     "id": "graph1",
#     "name": "Running Graph",
#     "unit": "km",
#     "type": "float",
#     "color": "sora",
# }
# headers = {
#     "X-USER-TOKEN": PIXELA_TOKEN,
# }
#
# response = requests.post(url=pixela_graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# === POST ===
# pixela_pixel_graph_endpoint = f"https://pixe.la/v1/users/{PIXELA_USER}/graphs/graph1"
# pixela_pixel_config = {
#     "date": dt.datetime.now().strftime("%Y%m%d"),
#     "quantity": "7.2",
# }
# headers = {
#     "X-USER-TOKEN": PIXELA_TOKEN,
# }
#
# response = requests.post(url=pixela_pixel_graph_endpoint, json=pixela_pixel_config, headers=headers)
# print(response.text)


# === PUT ===
update_pixela_endpoint = f"https://pixe.la/v1/users/{PIXELA_USER}/graphs/graph1/{dt.datetime.now().strftime('%Y%m%d')}"
# update_pixela_config = {
#     "quantity": "8.2",
# }
# headers = {
#     "X-USER-TOKEN": PIXELA_TOKEN,
# }
# response = requests.put(url=update_pixela_endpoint, json=update_pixela_config, headers=headers)
# print(response.text)


# === DELETE ===
headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}
response = requests.delete(update_pixela_endpoint, headers=headers)
print(response.text)
