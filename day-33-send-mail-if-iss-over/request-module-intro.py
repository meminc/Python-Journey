# API -> Application Programming Interface
# An Application Programming Interface (API) is a set of commands, functions, protocols, and objects that programmers
# can use to create software or interact with an external system

# Your System -> API -> External System

# Status codes: 1XX : Hold On
#               2XX : Here You Go
#               3XX : Go Away
#               4XX : You Screwed Up
#               5XX : I Screwed Up (server down etc.)

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# if response.status_code == 404:
#     raise Exception("That resource does not exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorized to access this data.")
# # https://httpstatuses.com/ -> You can look at all HTTP request status.

response.raise_for_status()  # by the help of this method, we don't need to type raise exception for each error type

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = (longitude, latitude)

print(iss_position)
