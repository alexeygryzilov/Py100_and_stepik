import random

def get_unique_list_numbers() -> list[int]:
      # TODO написать функцию для получения списка уникальных целых чисел
    list_numbers = []
    range_numbers = [number for number in range(-10, 11)]
    for _ in range(15):
        random_number  = random.choice(range_numbers)
        list_numbers.append(random_number)
        range_numbers.remove(random_number)

    return list_numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
