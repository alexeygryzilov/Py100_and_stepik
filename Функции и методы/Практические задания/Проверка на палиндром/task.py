# TODO Напишите функцию `is_palindrome`
def is_palindrome(str_1):
    list_1 = str_1.lower().split()
    str_2 =''.join(list_1)
    str_3 = str_2[::-1]
    return str_2 == str_3





