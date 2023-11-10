def merge_single(list_1: list[int], list_2: list[int]) -> list[int]:
    """Функция принимает список из натуральных чисел 'list_1',
    отсортированный по возрастанию и список 'list_2', состоящий из одного натурального числа,
    возвращает отсортированный список 'list_1' с добавленным числом из второго списка"""
    for i in range(len(list_1)):
        if list_2[0] <= list_1[i]:
            list_1 = list_2 + list_1
            return list_1
        elif list_1[i] < list_2[0] < list_1[i + 1]:
            list_1 = list_1[:i + 1] + list_2 + list_1[i + 1:]
            return list_1
        elif list_2[0] >= list_1[len(list_1) - 1]:
            list_1 = list_1 + list_2
            return list_1


def merge_multy(list_1: list[int], list_2: list[int]) -> list[int]:
    """Функция принимает список из натуральных чисел 'list_1',
    отсортированный по возрастанию и список 'list_2', состоящий натуральных чисел, отсортированный по
    возрастанию. Функйия  возвращает отсортированный список 'list_1' с добавлением всех элементов
     из списка 'list_2 ."""
    for j in range(len(list_2)):
        list_1 = merge_single(list_1, list_2[j:j + 1])
    list_2 = []
    return list_1

if __name__ == '__main__':
    test = merge_multy([1,3,6],[-4,2,7])
    print(test) # [-4, 1, 2, 3, 6, 7]

