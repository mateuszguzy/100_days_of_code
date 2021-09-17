import requests
from twilio.rest import Client

# CONSTANTS
# open_weather API key
API_KEY = ''
# position of weather check location
LAT = 50.26
LNG = 19.02
# weather API parameters
UNITS = 'metric'
EXCLUDE = 'current,minutely,daily,alerts'
HOURS_TO_CHECK = 20
# TWILIO (SMS API key and account number)
account_sid = 'AC9d4731984a10ed33c1bf235ebaef5478'
auth_token = ''

# get weather information
response = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?'
                        f'lat={LAT}&lon={LNG}&exclude={EXCLUDE}&appid={API_KEY}&units={UNITS}')
response.raise_for_status()
weather_data = response.json()
time = 0
weather_ids = list()

# define function for sending SMS
def send_sms():

    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                         body="Gonna rain!",
                         from_='+12406410917',
                         to=''
                     )
    print(message.status)

# check weather information for rain
# check for 12 hours forward if any status code for each hour is below 700 (APIs codes meaning rain)
for hour in weather_data['hourly']:
    if time < HOURS_TO_CHECK:
        for status in hour['weather']:
            # preparing a list of weather codes for HOURS_TO_CHECK hours
            weather_ids.append(status['id'])
    time += 1

# checking if any status code is below 700, if any is found send SMS alert and break the loop
for status_code in weather_ids:
    if status_code < 700:
        send_sms()
        break
