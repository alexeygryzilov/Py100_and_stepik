total = 0

while True:
    number = input('Ведите число: ')

    if number == "stop":
        break

    total += int(number)  # Суммируем число с общей суммой

print("Сумма чисел:", total)  # Выводим общую сумму
print("Конец программы")
