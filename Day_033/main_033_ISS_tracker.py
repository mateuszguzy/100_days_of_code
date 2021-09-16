import time
import requests
import datetime as dt
import smtplib

SENDER_EMAIL = 'testd3369@gmail.com'
PASSWORD = ''
# set parameters of current position
MY_LAT = 34
MY_LNG = 3

def get_iss_position():
    # get ISS parameters
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    iss_lat = float(response.json()['iss_position']['latitude'])
    iss_lng = float(response.json()['iss_position']['longitude'])
    iss_pos = {
        'lng': iss_lng,
        'lat': iss_lat
    }
    return iss_pos

def check_if_night():
    # prepare parameters of current location dictionary to pass into .get() function
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0
    }
    # get sunrise and sunset info on given localization
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response.raise_for_status()
    # prepare data to only show sunrise/sunset hour
    sunrise = int(response.json()['results']['sunrise'].split("T")[1].split("+")[0].split(":")[0])
    sunset = int(response.json()['results']['sunset'].split("T")[1].split("+")[0].split(":")[0])
    time_now = dt.datetime.now()

    if sunset < time_now.hour < 24 or 0 < time_now.hour < sunrise:
        return True

def send_mail():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs='',
            msg="Subject:Look UP!\n\nThe ISS is here.")

def main():
    # first check if it's night
    is_night = check_if_night()
    # if it is night check ISS position
    if is_night:
        iss_pos = get_iss_position()
        print(iss_pos)
        # check if ISS position is somewhere near your current position, if yes send yourself an email
        if (iss_pos['lng'] - 5) < MY_LNG < (iss_pos['lng'] + 5) or (iss_pos['lat'] - 5) < MY_LAT < (iss_pos['lat'] + 5):
            send_mail()
    time.sleep(60)
    main()

if __name__ == "__main__":
    main()
