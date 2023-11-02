number = 2342354235235

list_digits = [int(digit) for digit in str(number)]
# TODO c помощью list comprehension получить список цифр числа

print(sum(list_digits))  # TODO найти сумму цифр числа
print(sum([digit for digit in list_digits if digit % 2 == 0]))  # TODO найти сумму всех четных чисел
print(len(list_digits))  # TODO найти количество цифр
print(min(list_digits))  # TODO найти минимальную цифру
print(list_digits[0] - list_digits[-1])  # TODO наllйти разность между первой и последней цифр
