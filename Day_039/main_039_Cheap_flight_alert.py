import os
import smtplib
import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta

KIWI_API_KEY = os.environ.get("KIWI_API_KEY")
SHEETY_FLIGHT_DEALS_ENDPOINT = os.environ.get("SHEETY_FLIGHT_DEALS_ENDPOINT")
SHEETY_FLIGHT_AUTH_TOKEN = os.environ.get("SHEETY_FLIGHT_AUTH_TOKEN")

message_body = str()

def send_mail():
    sender_email = os.environ.get("TEST_MAIL_100DAYS")
    password = os.environ.get("TEST_MAIL_100DAYS_PASSWORD")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email,
            to_addrs=os.environ.get("PRIVATE_MAIL_1"),
            msg=f"Subject: Flight Offers!\n\n{message_body}")
    print("Mail sent.")

def destination_info():
    arrival_endpoint = SHEETY_FLIGHT_DEALS_ENDPOINT + "prices"
    departure_endpoint = SHEETY_FLIGHT_DEALS_ENDPOINT + "departures"

    headers = {
        "Content-Type": "application/json",
        "Authorization": SHEETY_FLIGHT_AUTH_TOKEN,
    }

    # get departure cities from "departures" sheet
    departure_response = requests.get(url=departure_endpoint, headers=headers)
    # for every departure city check prices for destination cities
    for location in departure_response.json()['departures']:
        departure_city = location['city']
        departure_iata = location['iataCode']
        # get destination cities from "prices" sheet
        arrival_response = requests.get(url=arrival_endpoint, headers=headers)
        for destination in arrival_response.json()['prices']:
            arrival_city = destination['city']
            arrival_iata = destination['iataCode']
            price = destination['lowestPrice']
            check_flights(arrival_city, arrival_iata, price, departure_city, departure_iata)

def check_flights(arrival_city, arrival_iata, price, departure_city, departure_iata):
    global message_body

    kiwi_search_endpoint = "https://tequila-api.kiwi.com/v2/search"

    # assign current date, and date after six months
    today = datetime.now()
    six_months_later = today + relativedelta(months=+6)

    # required Kiwi API headers
    headers = {
        "apikey": KIWI_API_KEY,
        "content-type": "application/json"
    }

    # search parameters
    search_data = {
        "fly_from": departure_iata,
        "fly_to": arrival_iata,
        "date_from": today.strftime("%d/%m/%Y"),
        "date_to": six_months_later.strftime("%d/%m/%Y"),
        "curr": "PLN",
        "adults": 2,
        "nights_in_dst_from": 2,
        "nights_in_dst_to": 6,
    }

    # API request
    response = requests.get(
        url=kiwi_search_endpoint,
        headers=headers,
        params=search_data,
    )

    # response processing
    data = response.json()['data']
    # for each found flight perform a number of test
    for flight in data:
        # checks if it's direct flight
        # when it is, only two dictionaries are in "route" list
        if len(flight['route']) == 2:
            # if trip price is lower than given value, send message with
            if flight['price'] <= price:
                # 1. Trip price
                # 2. Departure and destination city and IATA airport code
                message_body += f"From: {departure_city}\nTo: {arrival_city}\nFor: {flight['price']} zl\n"
                # 3. Departure and return dates
                message_body += f"Departure date: {flight['route'][0]['local_departure'].split('T')[0]}\n"
                message_body += f"Return date: {flight['route'][1]['local_departure'].split('T')[0]}\n"
                # 4. Booking link
                message_body += f"{flight['deep_link']}\n\n"
        # when there are no direct flights check for that ones which have one stop-over,
        # and list then with location name
        elif len(flight['route']) == 3:
            # if trip price is lower than given value, send message with
            if flight['price'] <= price:
                # 1. Trip price
                # 2. Departure and destination city and IATA airport code
                message_body += f"From: {departure_city}\nTo: {arrival_city}\nFor: {flight['price']} zl\n"
                # 3. Stop over city name
                # checking if stop over is at departure or arrival
                if flight['route'][0]['cityTo'] == arrival_city:
                    # if destination on first route is equal to main destination city
                    # it means that stop-over is at arrival
                    message_body += f"With stop-over on departure via {flight['route'][1]['cityTo']}\n"
                else:
                    message_body += f"With stop-over on arrival via {flight['route'][0]['cityTo']}\n"
                # 4. Departure and return dates
                message_body += f"Departure date: {flight['route'][0]['local_departure'].split('T')[0]}\n"
                message_body += f"Return date: {flight['route'][2]['local_departure'].split('T')[0]}\n"
                # 5. Booking link
                message_body += f"{flight['deep_link']}\n\n"
                # print(flight)

def main():
    destination_info()
    if len(message_body) != 0:
        # send_mail()
        print(message_body)
    else:
        print("No deals right now.")

if __name__ == "__main__":
    main()
