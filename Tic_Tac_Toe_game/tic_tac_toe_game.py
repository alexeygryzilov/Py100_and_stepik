from random import choice
from time import sleep
import dislplay_playing_field as display

header = 'Игра "крестики-нолики".'
players = ['игрок 1', 'игрок 2']
spare_squares = [1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = spare_squares[:]
count = 0
p1_moves = set()
p2_moves = set()
signs = ['X', 'O']
end = 'Игра окончена.'


def wincomb(n):
    a = [i for i in range(1, n * n + 1)]
    row = [set(a[i:i + n]) for i in range(0, n * n, n)]
    column = [set(a[i:n * n:n]) for i in range(n)]
    diag_1 = [set(a[n - 1: n * n - 1 : n - 1])]
    diag_2 = [set(a[:: n + 1])]
    wincomb_list = row + column + diag_1 + diag_2
    return wincomb_list

wincomb = wincomb(4)
spare_squares = [i for i in range(1, 4 * 4 + 1)]
symbols = spare_squares[:]

def validation(player_moves):
    list_ = [set_ <= player_moves for set_ in wincomb]
    return any(list_)


def congratulation(player):
    print(f'{player.capitalize()} выиграл!')
    print(f'{end:_^40}')


def request(player):
    print(f'{player.capitalize()}, Ваш ход. Свободны квадраты: ', end='')
    print(*spare_squares)


def input_check(inp, list_):
    ver_list = []
    ver_list.append(inp.isdigit())
    list_s = [str(i) for i in list_]
    ver_list.append(inp in list_s)
    return ver_list


def player_move(player, sign, player_moves, symbols, spare_squares):
    request(player)
    player_choice = input('Введите номер квадрата: ')
    input_check(player_choice, spare_squares)
    while not all(input_check(player_choice, spare_squares)):
        if not input_check(player_choice, spare_squares)[0]:
            print('-----')
            print(f'Неправильный ввод: "{player_choice}" это не число.')
            print('-----')
        else:
            print('-----')
            print(f'Квадрат с номером {player_choice} не существует или он уже занят.')
            print('-----')
        request(player)
        player_choice = input('Введите номер квадрата: ')

    player_choice_int = int(player_choice)
    player_moves.add(player_choice_int)
    symbols[symbols.index(player_choice_int)] = sign
    spare_squares.pop(spare_squares.index(player_choice_int))
    display.print_paying_field(4, symbols)


def draw():
    print(f"{' Ничья :( ' :_^40}")
    print(f'{end:_^40}')


print(f'{header:_^40}')
print()

print('Полагаю, что правила игры Вам известны. Первыми ходят "крестики".')

print('Бросим жребий, кому начинать...', end='    ')
sleep(1)
draw_ = choice(players)
if draw_ == players[0]:
    p1, p2 = players
else:
    p2, p1 = players
print(f'Начинает {draw_}')
print()

while len(spare_squares) > 0:
    player_move(p1, signs[0], p1_moves, symbols, spare_squares)
    count += 1
    if count > 4:
        validation(p1_moves)
        if validation(p1_moves):
            congratulation(p1)
            break
        if count == 9:
            draw()
            break

    player_move(p2, signs[1], p2_moves, symbols, spare_squares)
    count += 1
    if count > 5:
        validation(p2_moves)
        if validation(p2_moves):
            congratulation(p2)
            break
        if count == 9:
            draw()
            break
