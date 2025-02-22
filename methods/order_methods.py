import random
import allure
import requests
import data
from urls import Url






class OrderMethods:
    @allure.step('Метод создания заказа')
    def create_order(self, ingredients):
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_ORDER}', json={"ingredients": ingredients}, headers=headers)
        return response

    @allure.step('Метод получения заказа от пользователя')
    def get_orders_from_user(self, token):
        headers = {
            "Authorization": f"{token}"
        }
        response = requests.get(f'{Url.BASE_URL}{Url.GET_ORDER_FROM_USER}', headers=headers)
        return response

    @allure.step('Метод получения ингредиентов')
    def get_ingedients(self):
        response = requests.get(f'{Url.BASE_URL}{Url.GET_INGREDIENTS}')
        return response.json().get("data", [])

    @allure.step('Метод получения рандомных id ингредиентов из листа')
    def get_random_ingredient_id_from_list(self):
        random_number = random.randint(1, len(data.Ingredients.INGREDIENTS_LIST))
        selected_ingredients = random.sample(data.Ingredients.INGREDIENTS_LIST, k=random_number)
        ingredient_id = [ingredient["_id"] for ingredient in selected_ingredients]
        return ingredient_id