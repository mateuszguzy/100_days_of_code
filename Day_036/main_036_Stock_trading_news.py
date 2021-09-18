import os
import requests
import datetime as dt
from newsapi import NewsApiClient
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
news_dict = dict()
message_body = ""

def stock_compare():
    """Gets close stock values from day before and two days before and checks change percentage."""
    # stock API parameters
    alpha_vantage_api_key = os.environ.get("ALPHA_VANTAGE_API_KEY")
    stock_api_params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': STOCK,
        'interval': '60min',
        'apikey': alpha_vantage_api_key
    }
    stock_response = requests.get(url='https://www.alphavantage.co/query?', params=stock_api_params)
    stock_data = stock_response.json()['Time Series (60min)']
    # check today's date to check day before and two days before
    today = dt.datetime.now()
    first_day = f"2021-09-{today.day - 1} 20:00:00"
    second_day = f"2021-09-{today.day - 2} 20:00:00"
    # dictionary with close stock values of two consecutive days
    close_values = {
        'first_day': float(stock_data[first_day]["4. close"]),
        'second_day': float(stock_data[second_day]["4. close"]),
    }
    # percentage calculations
    change = ((close_values['first_day'] - close_values['second_day']) * 100) / close_values['second_day']
    return change


def get_news():
    """Gets top news articles on stock tracked company."""
    # news API parameters
    news_api_key = os.environ.get("NEWS_API_KEY")
    newsapi = NewsApiClient(api_key=news_api_key)
    top_headlines = newsapi.get_top_headlines(q=COMPANY_NAME,
                                              category='business',
                                              language='en')
    # check first three headlines and make dictionary out of headline and description
    for article in top_headlines['articles'][:3]:
        news_dict[article['title']] = article['description']

def send_mail():
    sender_email = ""
    password = os.environ.get("")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs='',
            msg=f"Subject:{COMPANY_NAME} Stock Info\n\n{message_body}")

def main():
    global message_body
    change = stock_compare()
    # if stock percentage change is higher than 5% (up or down) get news about company and send email with info
    if change <= -5 or 5 <= change:
        get_news()
        # starting message body with company name and stock change percentage
        message_body += f"{COMPANY_NAME} {round(change, 2)}%\n"
        # rest of message body contain top articles headlines and brief description
        for key, value in news_dict.items():
            message_body += f"Headline: {key}:\nBrief:{value}\n\n"
        send_mail()
        print("Message sent!")

if __name__ == "__main__":
    main()
