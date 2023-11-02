# TODO Запишите функцию `factorial`
def factorial(n):
    if n == 0:
        return 1
    else:
        f = 1
        for i in range(1, n + 1):
            f *= i
        return f


# TODO Вызовите функцию factorial и распечатайте результат 
print(f"Факториал числа 0 равен {factorial(0)}")
print(f"Факториал числа 5 равен {factorial(5)}")
