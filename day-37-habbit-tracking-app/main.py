import requests
from datetime import datetime
from dotenv import load_dotenv
from ui import UI
import os


app = UI()

load_dotenv()

USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")

GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# POST request to create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_configuration = {
    "id": GRAPH_ID,
    "name": "Working Hours",
    "unit": "hour",
    "type": "float",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# POST Request to create new graph
# response = requests.post(url=graph_endpoint, json=graph_configuration, headers=headers)
# print(response.text)

graph_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

graph_update_configuration = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9.0"
}

# response = requests.post(url=graph_update_endpoint, json=graph_update_configuration, headers=headers)
# print(response.text)

update_date = datetime(year=2022, month=1, day=22).strftime("%Y%m%d")

graph_put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{update_date}"

graph_put_configuration = {
    "quantity": "5.5"
}

# response = requests.put(url=graph_put_endpoint, json=graph_put_configuration, headers=headers)
# print(response.text)

delete_date = datetime(year=2022, month=1, day=22).strftime("%Y%m%d")

graph_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{delete_date}"

# response = requests.delete(url=graph_delete_endpoint, headers=headers)
# print(response.text)