""" Только для python >= 3.9 """


def get_tuple() -> tuple[int, str]:  # кортеж из двух элементов
    return 1, "two"
print(get_tuple())

def get_tuple_ints() -> tuple[int, ...]:  # кортеж произвольной длины
    return 1, 2, 3
print(get_tuple_ints())

def get_list() -> list[int]:  # внутри все значения типа int
    return [1, 2, 3, 4, 5]
print(get_list())

def get_dict() -> dict[int, list]:  # пара тип ключа - тип значения
    return {1: [2],3:['alfa',12, True]}
print(get_dict())