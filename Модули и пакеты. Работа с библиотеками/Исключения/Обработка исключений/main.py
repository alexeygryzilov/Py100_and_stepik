try:
    x = [1, 2, 3]# TODO Напишите input, чтобы запросить число
    result = 10 / A
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
except ValueError:
    print("Ошибка: Введено некорректное число!")
else:
    print("Результат: ", result)
finally:
    print("Конец программы")
