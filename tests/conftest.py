import pytest

from hepler import generate_registered_user
from methods.user_methods import UserMethods





@pytest.fixture
def clean_up_user(request):
    user_data = generate_registered_user()

    yield
    login_response = UserMethods().login_user(user_data)
    token = login_response.json().get("accessToken")
    UserMethods().delete_user(token)

@pytest.fixture
def register_user_fixture():
    user_data = generate_registered_user()
    UserMethods().register_user(user_data)
    return user_data



@pytest.fixture
def login_user_fixture(register_user_fixture):
    user_data = register_user_fixture
    login_response = UserMethods().login_user(user_data)
    token = login_response.json().get("accessToken")

    yield token




