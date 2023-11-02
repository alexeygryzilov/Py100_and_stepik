# TODO написать функцию remove

from typing import Any


def remove(list_: list, item: Any) -> list:
    reversed_list = list_[::-1]
    reversed_list.remove(item)
    final_list = reversed_list[::-1]
    return final_list



print(remove([0, 1, 2, 0, 1, 2], 0))  # [0, 1, 2, 1, 2]
print(remove([0, 1, 2], 0))  # [1, 2]
print(remove([0, 1, 2, 3, 4], 4))  # [0, 1, 2, 3]
