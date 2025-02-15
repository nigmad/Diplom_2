import data
import allure

from hepler import modify_create_user_body_empty_fields
from methods.user_methods import UserMethods




class TestCreateUser:
    @allure.title('Test user creation')
    def test_create_user_success(self, generate_registered_user, clean_up_user):
        user_data = generate_registered_user
        response = UserMethods().register_user(user_data)
        assert response.status_code == 200
        assert response.json().get("success") is True



    @allure.title('Test user creation with already existing email')
    def test_create_user_existing_email(self, generate_registered_user):
        user_data_1 = generate_registered_user
        create_response_1 = UserMethods().register_user(user_data_1)
        assert create_response_1.status_code == 200
        assert create_response_1.json().get("success") is True

        # Повторная попытка с тем же email
        user_data_2 = user_data_1.copy()
        create_response_2 = UserMethods().register_user(user_data_2)
        assert create_response_2.status_code == 403
        assert create_response_2.json().get("message") == data.ErrorMessages.ERROR_MESSAGES["user_exists"]





    @allure.title('Test user creation with missing field')
    def test_create_user_missing_fields(self, generate_registered_user):
        fields_to_check = ['email', 'password', 'name']
        modified_bodies = modify_create_user_body_empty_fields(fields_to_check, generate_registered_user)
        user_data_1 = modified_bodies[0]  # Данные с пустым email
        login_response_1 = UserMethods().register_user(user_data_1)
        assert login_response_1.status_code == 403
        assert login_response_1.json().get("message") == data.ErrorMessages.ERROR_MESSAGES["missing_fields"]

        user_data_2 = modified_bodies[1] # Данные с пустым password
        login_response_2 = UserMethods().register_user(user_data_2)
        assert login_response_2.status_code == 403
        assert login_response_2.json().get("message") == data.ErrorMessages.ERROR_MESSAGES["missing_fields"]

        user_data_3 = modified_bodies[2] # Данные с пустым name
        login_response_3 = UserMethods().register_user(user_data_3)
        assert login_response_3.status_code == 403
        assert login_response_3.json().get("message") == data.ErrorMessages.ERROR_MESSAGES["missing_fields"]



