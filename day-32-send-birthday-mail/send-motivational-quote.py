import smtplib
import random
import datetime as dt

my_email = "cinaliogluemin@gmail.com"
password = "Muh4mm3t61.!"

now = dt.datetime.now()

if now.weekday() == 6:
    with open("./quotes.txt", "r") as f:
        quotes = [line.replace("\n", "") for line in f.readlines()]
    random_quote = random.choice(quotes)
    with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
        # connection.starttls()  # -> encrypts the mail to make impossible to reached by others
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="cinaliogluemin@yahoo.com",
                            msg=f"Subject:Daily Quote\n\n{random_quote}"
                            )
