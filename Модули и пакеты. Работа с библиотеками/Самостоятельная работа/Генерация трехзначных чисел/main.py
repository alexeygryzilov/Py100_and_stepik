# TODO написать функцию, которая выдает трехзначное число
from string import digits
import random


def get_three_digit_number() -> int:
    str_numbers = '0123456789'
    three_digit_list = [random.choice(str_numbers) for _ in range(3)]
    three_digit_str = ''.join(three_digit_list)

    return int(three_digit_str)


print(f'{get_three_digit_number():03}')
