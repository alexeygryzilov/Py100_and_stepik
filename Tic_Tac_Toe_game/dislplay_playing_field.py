# print('\u250c \u2500 \u2510 \u2502 \u2514 \u2518') #┌  ┐ │ └ ┘

a = ('\u250c', '\u2500' * 11, '\u2510')
b = ('\u2502', " " * 11, '\u2502')
e = ('\u2514', '\u2500' * 11, '\u2518')


def print_top(n):
    f = [a * n, b * n]
    for i in f:
        print(*i, sep='')


def print_middle(symbols):
    c = [('\u2502', f'{sign:^11}', '\u2502') for sign in symbols]
    for i in c:
        print(*i, sep='', end='')
    print('')


def print_bottom(n):
    f = [b * n, e * n]
    for i in f:
        print(*i, sep='')


def print_row(n, symbols):
    print_top(n)
    print_middle(symbols)
    print_bottom(n)


def print_paying_field(n, symbols):
    for i in range(0, n * n, n):
        slice = symbols[i:i + n]
        print_row(n, slice)


if __name__ == '__main__':
    symbols = [i for i in range(1, 6 * 6 + 1)]
    print_paying_field(6, symbols)
