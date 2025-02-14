import requests
from data import Url

class UserMethods:
    def register_user(self, user_data):
        response = requests.post(f'{Url.BASE_URL}{Url.CREATE_USER}' , json=user_data)
        return response


    def login_user(self, user_data):
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_USER}', json=user_data)
        return response


    def delete_user(self, token):
        return requests.delete(f'{Url.BASE_URL}{Url.DELETE_USER}', headers={"Authorization": f"Bearer {token}"})



    def change_user_data(self, token, update_data):
        return  requests.patch(f'{Url.BASE_URL}{Url.CHANGE_USER_DATA}', json=update_data, headers={"Authorization": f"Bearer {token}"})



