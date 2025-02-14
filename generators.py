from faker import Faker



fake = Faker()

def register_new_user():
    return {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name()
    }
