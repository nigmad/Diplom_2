import allure
import pytest
import data
from data import DataForAuth
from methods.user_methods import UserMethods
from faker import Faker
fake = Faker()


class TestChangeUserData:

    @allure.title('Test change user data with authorization')
    @pytest.mark.parametrize(
        "field, new_value, expected_field_value", [
            ("email", fake.email(), "email"),  # Изменяем email
            ("name", fake.name(), "name"),  # Изменяем имя
        ]
    )
    def test_change_user_data_with_authorization(self, field, new_value, expected_field_value, register_user_fixture):
        user_data = register_user_fixture

        login_response = UserMethods().login_user(user_data)
        assert login_response.status_code == 200
        assert login_response.json().get("success") is True

        token = login_response.json().get("accessToken")
        assert token is not None

        update_data = {field: new_value}
        response = UserMethods().change_user_data(token, update_data)

        assert response.status_code == 200
        assert response.json().get("success") is True

        updated_user_data = response.json().get("user")
        assert updated_user_data.get(expected_field_value) == new_value

        delete_response = UserMethods().delete_user(token)
        assert delete_response.status_code == 202




    @allure.title('Test change user data without authorization')
    @pytest.mark.parametrize(
        "field, new_value, expected_field_value", [
            ("email", fake.email(), "email"),  # Изменяем email
            ("name", fake.name(), "name"),  # Изменяем имя
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

