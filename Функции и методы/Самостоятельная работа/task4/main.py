# TODO реализовать функцию
def insert(list_, value, index = 0):
    list_1 = list_[:index]
    list_2 = [value]
    list_3 = list_[value:]
    list_result = list_1 + list_2 + list_3
    return list_result



print(insert([1], value=0))  # [0, 1]
print(insert([0, 2], value=1, index=1))  # [0, 1, 2]
print(insert([0, 1, 2], value=3, index=3))  # [0, 1, 2, 3]
