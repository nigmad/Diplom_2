import random
import requests

import data
from data import Url





class OrderMethods:
    def create_order(self, ingredients):
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_ORDER}', json={"ingredients": ingredients}, headers=headers)
        return response



    def get_orders_from_user(self, token):
        return requests.get(f'{Url.BASE_URL}{Url.GET_ORDER_FROM_USER}', headers={"Authorization": f"Bearer {token}"})



    def get_ingedients(self):
        response = requests.get(f'{Url.BASE_URL}{Url.GET_INGREDIENTS}')
        return response.json().get("data", [])


    def get_random_ingredient_id_from_list(self):
        random_number = random.randint(1, len(data.Ingredients.INGREDIENTS_LIST))
        selected_ingredients = random.sample(data.Ingredients.INGREDIENTS_LIST, k=random_number)
        ingredient_id = [ingredient["_id"] for ingredient in selected_ingredients]
        return ingredient_id