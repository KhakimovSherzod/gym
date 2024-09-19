from typing import Tuple, Any


class User:
    height: float
    weight: int

    def __init__(self, username: str, age: int, weight: int, height: float, goal: str, diet_plan: str, fitness_plan: str):
        self.username = username,
        self.age = age,
        self.weight = weight
        self.height = height
        self.goal = goal,
        self.diet_plan = diet_plan,
        self.fitness_plan = fitness_plan


    def calculate_BMI(self):
        """Calculates the Body Mass Index."""
        BMI = self.weight / (self.height ** 2)
        if BMI < 18.5:
            return "Underweight"
        elif 18.5 <= BMI < 24.9:
            return "Normal weight"
        elif 25 <= BMI < 29.9:
            return "Overweight"
        else:
            return "Obesity"

    def suggest_plan(self, BMI_category):
        """Suggests diet and fitness plans based on user data."""
        print(f"Result is {BMI_category}!")
        if BMI_category == "Underweight":
            print(
                "Focus on consuming nutrient-rich foods, including lean proteins, "
                "whole grains, healthy fats, and fruits and vegetables. Consider "
                "increasing calorie intake with healthy snacks between meals and "
                "engage in strength training exercises to build muscle mass."
            )
        elif BMI_category == "Normal weight":
            print(
                "Maintain your current weight by following a balanced diet rich in "
                "fruits, vegetables, whole grains, and lean proteins. Stay hydrated, "
                "exercise regularly with a mix of cardio and strength training, and "
                "monitor your weight to maintain this healthy range."
            )
        elif BMI_category == "Overweight":
            print(
                "Focus on reducing calorie intake by choosing lower-calorie foods, "
                "avoiding sugary drinks, and practicing portion control. Incorporate "
                "more fruits, vegetables, and whole grains into your diet, and engage "
                "in regular physical activity such as cardio exercises and strength "
                "training."
            )
        else:
            print(
                "It's important to significantly reduce calorie intake, especially from "
                "high-calorie, low-nutrient foods. Focus on eating vegetables, lean proteins, "
                "and whole grains. Avoid sugary drinks, processed foods, and excessive carbs. "
                "Increase water intake, and engage in regular physical activity, including "
                "both cardio and strength training exercises."
            )

weight = 92
height = 1.75
user_health = User(username="offline", weight=weight, height=height, age=25, goal="cc", diet_plan="df", fitness_plan="do")

user_health.suggest_plan(user_health.calculate_BMI())
