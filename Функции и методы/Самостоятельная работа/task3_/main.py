def delete(list_, index=None):
    if index is None:
        index = -1
        list_1 = list_[:index]
        result = list_1
    else:
        list_1 = list_[:index]
        list_2 = list_[index + 1:]
        result = list_1 + list_2

    return result


# TODO реализовать функцию удаления элемента из списка по индексу


print(delete([0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
