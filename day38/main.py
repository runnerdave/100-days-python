from datetime import datetime
import os
import requests
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Your personal data. Used by Nutritionix to calculate calories.
GENDER = "male"
WEIGHT_KG = 63
HEIGHT_CM = 173
AGE = 47

NUTRITIONIX_URL = "https://www.nutritionix.com/business/api"
NATURAL_EXERCISE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
APPLICATION_ID_NUTRITIONIX = os.environ.get("NUTRITIONIX_APP_ID")
API_KEY_NUTRITIONIX = os.environ.get("NUTRITIONIX_API_KEY")

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
WORKOUT_SHEET_URL = os.environ.get("SHEETY_END_POINT")

def call_exercise_api(exercise):
    '''
    Sample response:
    {
    "exercises": [
        {
        "tag_id": 63,
        "user_input": "swam",
        "duration_min": 60,
        "met": 6,
        "nf_calories": 420,
        "photo": {
            "highres": "https://d2xdmhkmkbyw75.cloudfront.net/exercise//63_highres.jpg",
            "thumb": "https://d2xdmhkmkbyw75.cloudfront.net/exercise//63_thumb.jpg",
            "is_user_uploaded": false
        },
        "compendium_code": 18310,
        "name": "swimming",
        "description": null,
        "benefits": null
        }
    ]
    }
    '''
    params = {
        "query": exercise,
        "gender": GENDER,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
    }

    headers = {
        "x-app-id": APPLICATION_ID_NUTRITIONIX,
        "x-app-key": API_KEY_NUTRITIONIX
    }

    # exercise call
    response = requests.post(url=NATURAL_EXERCISE_URL, json=params, headers=headers, verify=False)
    response.raise_for_status()
    # print(response.text)
    data = response.json()
    exercise = {
        "name": data["exercises"][0]["name"],
        "calories": data["exercises"][0]["nf_calories"],
        "duration": data["exercises"][0]["duration_min"]
    }
    # print(exercise)
    return exercise

def get_workout_spreadsheet():
    headers = {
        "Authorization": f"Bearer {SHEETY_TOKEN}",
    }
    response = requests.get(url=WORKOUT_SHEET_URL, headers=headers, verify=False)
    response.raise_for_status()
    print(response.text)

def post_workout(exercise):
    today = datetime.now()
    today_formatted = today.strftime("%d/%m/%Y")
    time_formatted = today.strftime("%X")
    params = {
        "workout": {
            "date": today_formatted,
            "time": time_formatted,
            "duration": exercise["duration"],
            "calories": exercise["calories"],
            "exercise": exercise["name"].title()
        }
    }

    headers = {
        "Authorization": f"Bearer {SHEETY_TOKEN}",
    }

    response = requests.post(url=WORKOUT_SHEET_URL, json=params, headers=headers, verify=False)
    response.raise_for_status()
    # print(response.text)


if __name__ == '__main__':
    exercise = input("What exercise you want to record: ")
    post_workout(call_exercise_api(exercise))
    get_workout_spreadsheet()
    
