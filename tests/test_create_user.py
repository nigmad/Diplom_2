import pytest
import data
import allure
from hepler import modify_create_user_body_empty_fields, generate_registered_user
from methods.user_methods import UserMethods




class TestCreateUser:
    @allure.title('Test user creation')
    def test_create_user_success(self, clean_up_user):
        user_data = generate_registered_user()
        response = UserMethods().register_user(user_data)
        assert response.status_code == 200
        assert response.json().get("success") is True



    @allure.title('Test user creation with already existing email')
    def test_create_user_existing_email(self, register_user_fixture, clean_up_user):
        user_data_1 = register_user_fixture


        # Повторная попытка с тем же email
        user_data_2 = user_data_1.copy()
        create_response_2 = UserMethods().register_user(user_data_2)
        assert create_response_2.status_code == 403
        assert create_response_2.json().get("message") == data.ErrorMessages.ERROR_MESSAGES["user_exists"]





    @allure.title('Test user creation with missing field')
    @pytest.mark.parametrize(
        "field, expected_message",
        [
            ('email', data.ErrorMessages.ERROR_MESSAGES["missing_fields"]),
            ('password', data.ErrorMessages.ERROR_MESSAGES["missing_fields"]),
            ('name', data.ErrorMessages.ERROR_MESSAGES["missing_fields"])
        ]
    )
    def test_create_user_missing_fields(self, field, expected_message):
        modified_user_data = modify_create_user_body_empty_fields([field], generate_registered_user)[0]
        login_response = UserMethods().register_user(modified_user_data)
        assert login_response.status_code == 403
        assert login_response.json().get("message") == expected_message



