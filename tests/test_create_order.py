import allure

import data
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods


class TestCreateOrder:
    @allure.title('Test creation order with authorization')
    def test_create_order_with_auth(self, register_user_fixture):
        user_data = register_user_fixture
        login_response = UserMethods().login_user(user_data)
        assert login_response.status_code == 200

        token = login_response.json().get("accessToken")
        assert token is not None

        ingredient_id = OrderMethods().get_random_ingredient_id_from_list()

        order_response = OrderMethods().create_order(ingredient_id)

        assert order_response.status_code == 200
        assert order_response.json().get("success") is True
        assert "order" in order_response.json()




    @allure.title('Test creation order without authorization')
    def test_create_order_without_auth(self):
        ingredient_id = OrderMethods().get_random_ingredient_id_from_list()
        order_response = OrderMethods().create_order(ingredient_id)

        assert order_response.status_code == 401
        assert order_response.json().get("success") is False

    @allure.title('Test creation order with ingredients')
    def test_create_order_with_ingredients(self, register_user_fixture):
        user_data = register_user_fixture
        login_response = UserMethods().login_user(user_data)
        assert login_response.status_code == 200

        token = login_response.json().get("accessToken")
        assert token is not None

        ingredient_id = OrderMethods().get_random_ingredient_id_from_list()

        order_response = OrderMethods().create_order(ingredient_id)

        assert order_response.status_code == 200
        assert order_response.json().get("success") is True
        assert "order" in order_response.json()

    @allure.title('Test creation order with ingredients')
    def test_create_order_without_ingredients(self, register_user_fixture):
        user_data = register_user_fixture
        login_response = UserMethods().login_user(user_data)
        assert login_response.status_code == 200

        token = login_response.json().get("accessToken")
        assert token is not None

        ingredient_id = data.DataForOrder.NO_INGREDIENTS
        order_response = OrderMethods().create_order(ingredient_id)

        assert order_response.status_code == 400
        assert order_response.json().get("success") is False
        assert order_response.json().get("message") == data.ErrorMessages.ERROR_MESSAGES["empty_order"]

    @allure.title('Test creation order with wrong ingredient id')
    def test_create_order_with_wrong_ingredient_id(self, register_user_fixture):
        user_data = register_user_fixture
        login_response = UserMethods().login_user(user_data)
        assert login_response.status_code == 200

        token = login_response.json().get("accessToken")
        assert token is not None

        ingredient_id = data.DataForOrder.WRONG_INGREDIENT_ID
        order_response = OrderMethods().create_order(ingredient_id)

        assert order_response.status_code == 400
        assert order_response.json().get("success") is False
        assert order_response.json().get("message") == data.ErrorMessages.ERROR_MESSAGES["empty_order"]




