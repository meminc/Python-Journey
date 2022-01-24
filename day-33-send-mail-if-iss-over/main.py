import requests
import smtplib
from datetime import datetime
import time
import os
from dotenv import load_dotenv

load_dotenv()


MY_LAT = 39.933365  # Your latitude
MY_LONG = 32.859741  # Your longitude


def is_iss_over():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5:
        return True


# Your position is within +5 or -5 degrees of the ISS position
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if (sunrise > time_now.hour >= 0) or (sunset < time_now.hour <= 24):
        return True


my_email = os.getenv("MY_EMAIL")
password = os.getenv("PASSWORD")

while True:
    time.sleep(60)
    if is_night() and is_iss_over():
        with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject:LOOK UP\n\nLOOK UP to see ISS"
                                )
