from string import ascii_letters, digits
import random


def get_random_password(n=8) -> list:
# TODO написать функцию генерации случайных паролей
    str_ = ascii_letters + digits
    password = random.sample(str_, n)
    return password

print(get_random_password())
