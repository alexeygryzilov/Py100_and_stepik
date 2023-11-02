numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_none = numbers.index(None)

numbers_mod = numbers[:index_none] + numbers[index_none + 1:]

average = sum(numbers_mod) / len(numbers)

numbers[index_none] = round(average, 2)

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
