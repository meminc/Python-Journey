import smtplib
import ssl
import requests
import os
from dotenv import load_dotenv

load_dotenv()


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

FROM_EMAIL = os.getenv('FROM_EMAIL')
PASSWORD = os.getenv('PASSWORD')
TO_EMAIL = os.getenv('TO_EMAIL')
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")


smtp_server = "smtp.gmail.com"
PORT = 465  # For SSL
context = ssl.create_default_context()

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]

yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

difference = abs(float(day_before_yesterday_closing_price) - float(yesterday_closing_price))

diff_percent = 100 * (difference / float(yesterday_closing_price))

is_get_news = False

if diff_percent >= 5:
    is_get_news = True

if is_get_news:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    articles = response.json()["articles"]
    three_articles = articles[:3]

    mail_body = f"{STOCK} 🔺{diff_percent:.2f}% \n\n" if float(day_before_yesterday_closing_price) - float(
        yesterday_closing_price) >= 0 else f"{STOCK} 🔻{diff_percent:.2f}% \n\n"

    for article in three_articles:
        mail_body = mail_body + "\tHeadline: " + article["title"] + "\n\nBrief: " + article["description"] + "\n\n"
    message = f"Subject: DAILY STOCK MAIL\n\n{mail_body}"
    print(message)

    with smtplib.SMTP_SSL(smtp_server, PORT, context=context) as server:
        server.login(FROM_EMAIL, PASSWORD)
        server.sendmail(FROM_EMAIL, TO_EMAIL, message.encode('utf-8'))
