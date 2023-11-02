num = 27  # Число для проверки гипотезы Коллатца
count = 0  # Количество операций над числом

while num > 1:
    if num % 2 == 0:
        num //= 2
        count += 1
    else:
        num = num * 3 + 1
        count += 1

print("Количество действий:", count)
