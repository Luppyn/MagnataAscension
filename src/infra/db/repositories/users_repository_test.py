from random import random
from .users_repository import UsersRepository


def test_insert_user():
    mocked_name = 'my_name'
    mocked_email = 'email'
    mocked_age = int(random()*10)

    users_repository = UsersRepository()
    users_repository.insert_user(mocked_name, mocked_email, mocked_age)



