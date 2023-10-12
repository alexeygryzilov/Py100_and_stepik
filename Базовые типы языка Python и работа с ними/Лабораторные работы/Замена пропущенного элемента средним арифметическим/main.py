numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers1 = numbers[:4]
numbers2 = numbers[5:]
numbers3 = numbers1 + numbers2

number = sum(numbers3) / len(numbers)

numbers1.append(number)

numbers_correct = numbers1 + numbers2

# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers_correct)
