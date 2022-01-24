# SMTP -> Simple Mail Transfer Protocol
# TLS -> Transport Layer Security: it's a way of securing our connection to all email server
import smtplib


my_email = "cinaliogluemin@gmail.com"
password = "Muh4mm3t61.!"
with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
    # connection.starttls()  # -> encrypts the mail to make impossible to reached by others
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="cinaliogluemin@yahoo.com",
                        msg="Subject:Hello\n\nThis is the body of my email."
                        )
