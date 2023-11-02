# TODO реализовать функцию count
def count(list_, item):
    count = 0
    for element in list_:
        if element == item:
            count += 1
    return count



list_items = [1, 2,  1]

print(count(list_items, 1) == list_items.count(1))  # True
print(count(list_items, 3) == list_items.count(3))  # True
