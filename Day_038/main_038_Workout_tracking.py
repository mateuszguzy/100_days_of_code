import os

import requests
import datetime as dt

NUTRITRIONIX_ID = os.environ.get("NUTRITRIONIX_ID")
NUTRITRIONIX_API_KEY = os.environ.get("NUTRITRIONIX_API_KEY")
SHEETY_WORKOUT_TRACKER_ENDPOINT = os.environ.get("SHEETY_WORKOUT_TRACKER_ENDPOINT")
SHEETY_WORKOUT_TRACKER_AUTH_TOKEN = os.environ.get("SHEETY_WORKOUT_TRACKER_AUTH_TOKEN")


def get_exercise_data():
    exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

    headers = {
        "x-app-id": NUTRITRIONIX_ID,
        "x-app-key": NUTRITRIONIX_API_KEY,
        "Content-Type": "application/json"
    }

    # ask user to provide training description i.e. "I ran 2km and walk for 40min"
    user_input = input("Describe your workout: ")

    # provide data necessary for API to calculate burnt calories and exercise duration
    exercise_data = {
        "query": user_input,
        "gender": "male",
        "weight_kg": 60,
        "height_cm": 165,
        "age": 25,
    }
    response = requests.post(url=f'{exercise_endpoint}', headers=headers, json=exercise_data)
    print(response.text)
    # for every made exercise apply new row into spreadsheet
    for exercise in response.json()['exercises']:

        exercise_name = exercise['name'].capitalize()
        duration = exercise['duration_min']
        calories = exercise['nf_calories']

        add_row_to_sheet(exercise_name, duration, calories)


def add_row_to_sheet(exercise, duration, calories):
    today = dt.datetime.now()
    sheet_endpoint = SHEETY_WORKOUT_TRACKER_ENDPOINT + 'arkusz1'

    headers = {
        "Content-Type": "application/json",
        "Authorization": SHEETY_WORKOUT_TRACKER_AUTH_TOKEN,
    }
    # data structure requested by the API, keys must match spreadsheet column names
    json_data = {
        'arkusz1': {
            "date": today.strftime('%d/%m/%Y'),
            "time": today.strftime('%H:%M:%S'),
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        },
    }

    response = requests.post(url=sheet_endpoint, headers=headers, json=json_data)
    print(response.text)


def main():
    get_exercise_data()


if __name__ == "__main__":
    main()
