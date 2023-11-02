# TODO Распечатать таблицу умножения
for i in range(2,10):
    for j in range(2,10):
        if j != 9:
            print(f'{i*j:2}', end=' ')
        else:
            print(f'{i*j:2}')