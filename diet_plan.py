import requests
from flask import Flask, render_template, request, redirect, url_for

EDAMAM_APP_ID = "64aefe96"
EDAMAM_API_KEY = "68dee8a219f452d2dde6e6f707328a6a"


class DietPlan:

    def __init__(self):
        self.meals = "meal_name",
        self.total_calories = [],
        self.macronutrients = []

    def fetch_nutritional_info(self, meal):
        """Fetches nutritional data for the meals using an API."""
        url = f"https://api.edamam.com/api/nutrition-data?app_id={EDAMAM_APP_ID}&app_key={EDAMAM_API_KEY}&ingr={meal}"
        response = get(url=url)
        response.raise_for_status()
        data = response.json()
        calories = data["totalNutrients"]["ENERC_KCAL"]
        self.macronutrients.append(calories)
        fat = data["totalNutrients"]["FAT"]
        self.macronutrients.append(fat)
        protein = data["totalNutrients"]["PROCNT"]
        self.macronutrients.append(protein)
        carbs = data["totalNutrients"]["CHOCDF"]
        self.macronutrients.append(carbs)
        # print(self.macronutrients)


    def calculate_totals(self):
        """Calculates total calories and macronutrients (protein, fat, carbs)."""
        for item in self.macronutrients:
            print(f"{item["label"]}: {item["quantity"]} g")

d = DietPlan()
d.fetch_nutritional_info(meal="beef 100g")
d.calculate_totals()