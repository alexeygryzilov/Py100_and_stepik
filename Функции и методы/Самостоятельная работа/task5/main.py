# TODO реализовать функцию
def get_sentences_list(text):
    list_ = text.split('.')
    result = []
    for line in list_:
        line_mod = line.strip()

        if line_mod:
            result.append(line_mod)
    return result


print(get_sentences_list("Здесь много разных слов  . Возможно и много повторений..."))
