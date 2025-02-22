from generators import register_new_user


def modify_create_user_body_empty_fields(fields_to_check, generate_registered_user):
    modified_bodies = []
    for field in fields_to_check:
        user_data = {key: generate_registered_user.get(key) if key != field else "" for key in fields_to_check}
        modified_bodies.append(user_data)
    return modified_bodies



def generate_registered_user():
    user_data = register_new_user()
    return {
        "email": user_data["email"],
        "password": user_data["password"],
        "name": user_data["name"]
    }
