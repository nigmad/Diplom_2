import allure
import pytest
import data
from data import DataForAuth
from generators import register_new_user
from methods.user_methods import UserMethods



class TestChangeUserData:

    @allure.title('Test change user data with authorization')
    @pytest.mark.parametrize(
        "field, new_value, expected_field_value", [
            ("email", register_new_user()["email"], "email"),  # Изменяем email
            ("name", register_new_user()["name"], "name"),  # Изменяем имя
        ]
    )
    def test_change_user_data_with_authorization(self, field, new_value, expected_field_value, login_user_fixture, clean_up_user):
        token = login_user_fixture

        update_data = {field: new_value}
        response = UserMethods().change_user_data(token, update_data)
        assert response.status_code == 200
        assert response.json().get("success") is True
        updated_user_data = response.json().get("user")
        assert updated_user_data.get(expected_field_value) == new_value





    @allure.title('Test change user data without authorization')
    @pytest.mark.parametrize(
        "field, new_value, expected_field_value", [
            ("email", register_new_user()["email"], "email"),  # Изменяем email
            ("name", register_new_user()["name"], "name"),  # Изменяем имя
        ]
    )
    def test_change_user_data_without_authorization(self, field, new_value, expected_field_value):

        token = DataForAuth.EMPTY_TOKEN
        update_data = {
            field: new_value
        }
        response = UserMethods().change_user_data(token, update_data)
        assert response.status_code == 401
        assert response.json().get("success") is False
        assert response.json().get("message") == data.ErrorMessages.ERROR_MESSAGES["non_authorized"]




