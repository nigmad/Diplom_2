import allure

import data
from data import DataForAuth
from methods.user_methods import UserMethods
import pytest


class TestLoginUser:
    @allure.title('Test successful login')
    def test_login_success(self, register_user_fixture, clean_up_user):
        user_data = register_user_fixture

        login_response = UserMethods().login_user(user_data)
        assert login_response.status_code == 200
        assert login_response.json().get("success") is True





    @allure.title('Test login with wrong email or password')
    @pytest.mark.parametrize("user_data", [DataForAuth.LOGIN_DATA_WRONG_PASSWORD,
    DataForAuth.LOGIN_DATA_WRONG_EMAIL])
    def test_login_with_wrong_email_and_password(self, user_data):
        response = UserMethods().login_user(user_data)
        assert response.status_code == 401
        assert response.json().get("message") == data.ErrorMessages.ERROR_MESSAGES["invalid_credentials"]