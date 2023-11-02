# Использование def функции


def square(x):
    return x ** 2


print(square)  # Объект функция square

print(square(30))

# Использование lambda функции
square_1 = lambda x: x ** 2
print(square_1)
print(lambda x: x ** 2)  # Объект lambda функция
print(square_1(30))

