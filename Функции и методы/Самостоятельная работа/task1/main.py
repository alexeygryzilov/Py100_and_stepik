# TODO реализовать функцию
def remove_whitespace(str_):
    list_ = str_.split(' ')
    while '' in list_:
        list_.remove('')
    new_str = ' '.join(list_)
    return new_str


str_with_space = """123.    test bks
print   test11"""  # исходная строка
print(remove_whitespace(str_with_space))
