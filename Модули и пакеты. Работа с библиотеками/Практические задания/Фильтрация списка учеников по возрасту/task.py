# TODO Напишите функцию calculate_average_age
def calculate_average_age(list_):
    age_list = [record.get('age') for record in list_]
    average_age = sum(age_list) / len(age_list)
    return average_age

# TODO Напишите функцию filter_students_by_age
def filter_students_by_age(list_, avg_age):
    final_list = [record for record in list_ if record.get('age') <= avg_age]
    return final_list

if __name__ == '__main__':
    # Пример списка учеников
    students_list = [
        {
            "name": "Саша",
            "age": 27,
        },
        {
            "name": "Кирилл",
            "age": 52,
        },
        {
            "name": "Маша",
            "age": 14,
        },
        {
            "name": "Петя",
            "age": 36,
        },
        {
            "name": "Оля",
            "age": 43,
        },
    ]

    # Вычисление среднего возраста
    # TODO Вычислите средний возраст учеников
    print("Средний возраст учеников:", calculate_average_age(students_list))

    # Фильтрация учеников по возрасту
    # TODO Офильтруйте учеников
    avg_age = calculate_average_age(students_list)
    print("Список учеников с возрастом меньше среднего:")
    for current_student in filter_students_by_age(students_list, avg_age):
        print(current_student['name'])
