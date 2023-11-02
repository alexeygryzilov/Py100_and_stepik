
from typing import List
# TODO написать функцию index
def index(list_, item) -> list[int]:
    index = 0
    result = []
    for value in list_:
        if value == item:
            result.append(index)
        index += 1
    if result:
        return result
    else:
        raise ValueError('Такого элемента в списке нет!')




if __name__ == '__main__':
    list_items = [1, 2, "3", 1]
    print(index(list_items, 1) == [0, 3])  # True
