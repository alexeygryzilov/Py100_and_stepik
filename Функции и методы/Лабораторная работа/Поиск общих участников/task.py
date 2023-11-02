# TODO Напишите функцию find_common_participants
def find_common_participants(str_1, str_2, sep=','):
    set_1 = set(str_1.split(sep))
    set_2 = set_1.intersection(str_2.split(sep))
    result = list(set_2)
    result.sort()
    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common_participants = find_common_participants(participants_first_group,
                                               participants_second_group,
                                               sep='|')

print(common_participants)
