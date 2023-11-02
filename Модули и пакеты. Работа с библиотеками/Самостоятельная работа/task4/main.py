import random
from random import choice


EAGLE = "Орел"
TAILS = "Решка"

coin = [EAGLE, TAILS]  # монета, для которой нужно выбрать случайную сторону
counts = [10, 100, 1000, 100000, 1000000]  # различное количество подбрасываний
list_freq = []  # список, где будем хранить отношение количества выпавших орлов к решке

for count in counts:
    toss_dict = {}
    for _ in range(count):
        choice = random.choice(coin)
        toss_dict[choice] = toss_dict.get(choice, 0) +1

    eagle = toss_dict['Орел']
    tail = toss_dict['Решка']
    frequency = min(eagle, tail) / max(eagle, tail)
    list_freq.append(frequency)

    # TODO разделить минимальное число среди орлов и решек на максимальное число и сохранить результат

print(list_freq)
