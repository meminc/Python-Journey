import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')
OWM_Endpoint = os.getenv('OWM_ENDPOINT')
account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
from_number = os.getenv('FROM_NUMBER')
to_number = os.getenv('TO_NUMBER')

parameters = {
    "lat": 39.886601,
    "lon": 32.804042,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella ☂",
        from_=from_number,
        to=to_number
    )

    print(message.sid)
