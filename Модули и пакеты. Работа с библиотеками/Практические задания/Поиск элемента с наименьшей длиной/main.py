# TODO  Напишите функцию get_shortest_word
def get_shortest_word(list_) -> str:
    result = min(list_, key = lambda i: len(i))
    return result


if __name__ == "__main__":
    words_list = ["apple", "banana", "orange", "grapefruit", "kiwi"]
    shortest_word = get_shortest_word(words_list)  # TODO Найдите самое короткое слово
    print(shortest_word)  # kiwi
