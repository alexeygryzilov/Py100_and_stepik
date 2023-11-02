# TODO реализовать функцию
def get_unique_words(text):
    list_1 = text.split(' ')
    set_ = set(list_1)
    list_2 = list(set_)
    list_2.sort()
    return list_2


print(get_unique_words("Здесь много разных слов. Возможно и много повторений."))
