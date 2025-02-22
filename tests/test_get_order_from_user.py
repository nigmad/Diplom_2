import allure

import data
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods
from tests.conftest import login_user_fixture


class TestGetOrderFromUser:
    @allure.title('Test get order from authorized user')
    def test_get_order_from_auth_user(self, login_user_fixture, clean_up_user):
        token = login_user_fixture
        response = OrderMethods().get_orders_from_user(token)

        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "orders" in response.json()



    @allure.title('Test get order from unauthorized user')
    def test_get_order_from_unauthorized_user(self):
        token = data.DataForAuth.EMPTY_TOKEN
        response = OrderMethods().get_orders_from_user(token)
        assert response.status_code == 401
        assert response.json().get("success") is False
        assert response.json().get("message") == data.ErrorMessages.ERROR_MESSAGES["non_authorized"]



