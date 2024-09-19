import requests
import datetime as dt


class FitnessPlan:
    def __init__(self):
        self.workout_list = [],
        self.total_duration = 0,
        self.calories_burned = 0

    def suggest_workouts(self):
        """Suggests workouts based on user goals."""
        body_part = {0: "back",
        1: "cardio",
        2: "chest",
        3: "lower arms",
        4: "lower legs",
        5: "neck",
        6: "shoulders",
        7: "upper arms",
        8: "upper legs",
        9: "waist",
        }
        print(body_part)
        target = input("Which body part do you want to train? ")
        url = f"https://exercisedb.p.rapidapi.com/exercises/bodyPart/{target}"

        querystring = {"limit": "4", "offset": "0"}

        headers = {
            "x-rapidapi-key": "7e1d4dbf93msh06ac762ba3398e3p1fc18cjsn309d268f4c4b",
            "x-rapidapi-host": "exercisedb.p.rapidapi.com",
            "X-RapidAPI-Mock-Response": "200"
        }

        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()
        workout_list = []
        num = 0
        for workout in data:
            body_part = workout["bodyPart"]
            workout_list.append(body_part)
            equipment = workout["equipment"]
            workout_list.append(equipment)
            name = workout["name"]
            workout_list.append(name)
            target = workout["target"]
            workout_list.append(target)
            instructions = workout["instructions"]
            workout_list.append(instructions)
            gif = workout["gifUrl"]
            workout_list.append(gif)
            num += 1
            print(f"Here is the exercise number {num}:\n"
                  f"Body part: {body_part},\n"
                  f"Equipment: {equipment},\n"
                  f"Name: {name},\n"
                  f"Target: {target},\n"
                  f"Gif: {gif}"
                  f"Instructions:")
            for instruction in instructions:
                print(f"* {instruction}")

    def track_progress(self, exercise_text):
        """Tracks and updates the user’s fitness progress."""
        url = "https://trackapi.nutritionix.com/v2/natural/exercise"
        app_id = "9bba4f36"
        app_key = "f5b982e12cac48150ddebc0468a6e01e"
        headers = {
            "x-app-id": app_id,
            "x-app-key": app_key
        }
        parameters = {
            "query": exercise_text,
            "gender": "male",
            "weight_kg": 72,
            "height_cm": 174,
            "age": 25
        }
        response = requests.post(url, json=parameters, headers=headers)
        response.raise_for_status()
        return response.json()

    def log_to_sheet(self, data):
        today_time = dt.datetime.now().strftime("%d/%m/%Y")
        now_time = dt.datetime.now().strftime("%X")
        sheet_endpoint = "https://api.sheety.co/1478fa165d411ff182e37dc93fb4e640/projectApp/workouts"
        for item in data["exercises"]:
            sheet_input = {
                "workout": {
                    "date": today_time,
                    "time": now_time,
                    "exercise": item["name"].title(),
                    "duration": item["duration_min"],
                    "calories": item["nf_calories"]
                }
            }
            sheet_response = requests.post(sheet_endpoint, json=sheet_input)
            sheet_response.raise_for_status()
            return sheet_response.json()


    def get_workout_logs(self):
        """Retrieves all workout logs from Sheety."""
        sheet_endpoint = "https://api.sheety.co/1478fa165d411ff182e37dc93fb4e640/projectApp/workouts"
        response = requests.get(sheet_endpoint)
        response.raise_for_status()
        return response.json()





