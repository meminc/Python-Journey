# Automated Birthday Wisher
import pandas as pd
import datetime as dt
import smtplib
from random import randint
import os
from dotenv import load_dotenv


# ==================== Extra Hard Starting Project ==================== #
load_dotenv()

my_email = os.getenv("MY_EMAIL")
password = os.getenv("PASSWORD")

# 1. Update the birthdays.csv
birthday_data = pd.read_csv("./birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today_birthday = birthday_data[(birthday_data["month"] == now.month) & (birthday_data["day"] == now.day)]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
if len(today_birthday) > 0:
    for index, row in today_birthday.iterrows():
        template = ""
        with open(f"./letter_templates/letter_{randint(1, 3)}.txt") as letter_template:
            template = letter_template.read()
        with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
            # connection.starttls()  # -> encrypts the mail to make impossible to reached by others
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=row['email'],
                                msg=f"Subject:Happy Birthday\n\n{template.replace('[NAME]', row['name'])}"
                                )


# 4. Send the letter generated in step 3 to that person's email address.
