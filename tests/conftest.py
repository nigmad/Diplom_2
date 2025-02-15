import pytest

from generators import register_new_user
from methods.user_methods import UserMethods


@pytest.fixture
def generate_registered_user():
    user_data = register_new_user()
    return {
        "email": user_data["email"],
        "password": user_data["password"],
        "name": user_data["name"]
    }



@pytest.fixture
def clean_up_user(request, generate_registered_user):
    user_data = generate_registered_user

    def delete_user_after_test():
        login_response = UserMethods().login_user(user_data)
        token = login_response.json().get("accessToken")
        print(f"Generated Token: {token}")
        delete_response = UserMethods().delete_user(token)
        assert delete_response.status_code == 202

    request.addfinalizer(delete_user_after_test)



@pytest.fixture
def register_user_fixture(generate_registered_user):
    user_data = generate_registered_user
    response = UserMethods().register_user(user_data)
    assert response.status_code == 200
    assert response.json().get("success") is True
    return user_data








