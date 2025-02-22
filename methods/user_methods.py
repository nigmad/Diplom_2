import allure
import requests
from urls import Url

class UserMethods:
    @allure.step('Метод регистрации пользователя')
    def register_user(self, user_data):
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_USER}' , json=user_data)
        return response

    @allure.step('Метод логина пользователя')
    def login_user(self, user_data):
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_USER}', json=user_data)
        return response

    @allure.step('Метод удаления пользователя')
    def delete_user(self, token):
        return requests.delete(f'{Url.BASE_URL}{Url.DELETE_USER}', headers={"Authorization": f"{token}"})

    @allure.step('Метод обновления данных пользователя')
    def change_user_data(self, token, update_data):
        return  requests.patch(f'{Url.BASE_URL}{Url.CHANGE_USER_DATA}', json=update_data, headers={"Authorization": f"{token}"})



