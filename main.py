import os
import requests
from datetime import datetime

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
BEARER_TOKEN = os.environ['BEARER_TOKEN']

GENDER = "male"
WEIGHT = 80
HEIGHT_IN_CM = 167.23
AGE = 32

user_input = input(f'Tell me which exercises you did today?: ')

WORKOUT_ENDPOINT = os.environ['WORKOUT_ENDPOINT']
SHEET_ENDPOINT = os.environ['SHEET_ENDPOINT']

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

workout_params = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT_IN_CM,
    "age": AGE
}

results = requests.post(url=WORKOUT_ENDPOINT, json=workout_params, headers=header)
data = results.json()

today = datetime.now()
time = today.strftime('%H:%M:%S')
date = today.strftime('%d/%m/%Y')

# user_activities = len(data['exercises'])

# print
# activity_details = [new_item for item in list]
for activity in data['exercises']:
    row_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": activity['name'].title(),
            "duration": activity['duration_min'],
            "calories": activity['nf_calories'],
        }
    }

    sheet_response = requests.post(url=SHEET_ENDPOINT, json=row_params, headers=header, )
    print(sheet_response.text)
