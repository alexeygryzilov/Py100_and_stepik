from random import choice
from time import sleep
from typing import Union, Optional
import dislplay_playing_field as display

players_list = ['игрок 1', 'игрок 2']  # имена игроков
signs_list = ['- X -', '- O -']  # список символов "крестик" и "нолик"


def check_size(a: str) -> list[bool]:
    """
    Проверяет пользовательский ввод, размер поля -
    1.игрок должен ввести число - размер поля
    2.размер поля должен быть не меньше 3-х.
    Возвращает список из логических переменных

    :param a: строковый литерал, размер поля a x a
    :return: отображение списка из логических переменных
    """
    check_list = []
    check_list.append(a.isdigit())
    if a.isdigit():
        check_list.append(int(a) >= 3)
    return (check_list)


def preface(players: list[str], signs: list[str]) -> tuple[str, list, list]:
    """
    Выводит на печать начало игры: заголовок, условия игры,
    игровое поле 3 x 3 в качестве примера.
    В списке players случайным образом определяются I и II игроки.
    Список players обновляется согласно случайному выбору [I игрок,II игрок].
    Запрашивает у I игрока ввод предпочитаемого символа: 'крестик' или 'нолик'.
    В бесконечном цикле проверяет правильность ввода.
    Список signs обновляется согласно выбору I игрока.
    Запрашивает у II игрока ввод желаемого размера игрового поля.
    В бесконечном цикле проверяет правильность ввода: 1. это
    должно быть натуральное число 2. число должно быть не меньше 3-х.
    Возвращает кортеж: размер игрового поля, список игроков, список символов
    'крестик' и 'нолик'.

    :param players: список имён игроков 'игрок 1', 'игрок 2'
    :param signs: символы '- X -', '- O -'
    :return: ортеж: размер игрового поля, список игроков, список символов
    """

    header = 'Игра "крестики-нолики".'  # заголовок начала игры
    print(f'{header:_^40}')
    print()
    print('   В нашей игре участвуют 2 человека: Игрок 1 и Игрок 2. Игроки ходят по очереди.\n' \
          'Игра заканчиватся либо победой одного из игороков либо ничьёй.\n' \
          'В игре можно выбрать размер игрового поля. Вот так будет выглядеть поле 3 x 3.')
    sleep(1)
    print()
    display.print_paying_field(3, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    sleep(1)
    print()
    print('Бросим жребий, кому начинать...', end='    ')
    sleep(1)

    draw_1_2 = choice(players)
    if draw_1_2 == players[0]:
        p1, p2 = players
    else:
        p2, p1 = players
        players = players[::-1]
    print(f'Начинает {p1}')
    print()

    x_or_o = input(
        f'{p1.capitalize()}, какой символ Вы будете использовать : "крестики" или "нолики"? Введите "X" или "O" ')
    print('-----')
    while not (x_or_o.upper() in ['X', 'Х'] or x_or_o.upper() in ['O', 'О', str(0)]):
        print('Неправильный ввод. Повторите ввод.')
        print('-----')
        x_or_o = input(
            f'{p1.capitalize()}, какой символ Вы будете использовать : "крестик" или "нолик"? Введите "X" или "O" ')
        print('-----')
    if x_or_o.upper() in ['O', 'О', str(0)]:
        signs = signs[::-1]
        print(f'{p1.capitalize()} выбрал "нолик".\n{p2.capitalize()} будет играть "крестиками"')
    else:
        print(f'{p1.capitalize()} выбрал "крестик".\n{p2.capitalize()} будет играть "ноликами"')

    print('-----')
    n = input(
        f'{p2.capitalize()}, выберите размер игрового поля: минимальный размер 3 x 3. В ведите целое число не меньше 3.')
    check_size(n)
    while not all(check_size(n)):
        if not check_size(n)[0]:
            print('-----')
            print(f'Неправильный ввод: вы ввели: "{n}" - это не число.')
        else:
            print('-----')
            print(f"Число {n} слишком маленькое, оно должно быть не меньше 3.")
            print('-----')
        n = input(
            f'{p2.capitalize()}, выберите размер игрового поля: минимальный размер 3 x 3. В ведите целое число не меньше 3.')

    return n, players, signs


def check_winner(n, player, player_moves: set) -> bool:
    """
    Проверяет ходы игрока на выигрыш.
    Возвращает логическую переменную -
    результат проверки.

    :param player_moves: ходы игрока - множество из натуральных чисел
    :return: True или False
    """
    end = 'Игра окончена.'
    a = [i for i in range(1, n * n + 1)]
    row = [set(a[i:i + n]) for i in range(0, n * n, n)]
    column = [set(a[i:n * n:n]) for i in range(n)]
    diag_1 = [set(a[n - 1: n * n - 1: n - 1])]
    diag_2 = [set(a[:: n + 1])]
    wincomb_list = row + column + diag_1 + diag_2
    list_ = [set_ <= player_moves for set_ in wincomb_list]
    if any(list_):
        print()
        print(f'\u2605\u2605\u2605    {player.capitalize()} выиграл!  \u2605\u2605\u2605')
        print(f'{end:_^30}')
    return any(list_)


def tie() -> None:
    """
    Выводит на печать ничейный пезультат.
    Выводит на печать завершение игры.
    :return: None
    """
    end = 'Игра окончена.'
    print()
    print(f"{' Ничья :( ' :_^30}")
    print(f'{end:_^30}')


def input_check(inp: str, list_: list[int]) -> list[bool]:
    """
    Проверяет пользовательский ввод, ход игрока -
    1.игрок должен ввести число - номер квадрата
    2.этот квадрат должен быть свободным.
    Возвращает список из логических переменных

    :param inp: строковый литерал, номер квадрата
    :param list_: список квадратов, свободных на аднный момент
    :return: отображение списка из логических переменных
    """
    ver_list = []
    ver_list.append(inp.isdigit())
    list_s = [str(i) for i in list_]
    ver_list.append(inp in list_s)
    return ver_list


def request(player: str, sign: str, spare_squares: list) -> None:
    """
    Выводит на печать приглашение игроку сделать ход.
    Выводит на печать список свободных квадратов.

    :param player: имя игрока
    :param sign: символ, который использует игрок - 'крестик' или 'нолик'
    :return: None
    """

    print(f'{player.capitalize()}  {sign}, Ваш ход. Свободны квадраты: ', end='')
    print(*spare_squares)


def player_move(player: str, sign: str, player_moves: set, symbols: list, spare_squares: list, n) -> None:
    """
    Приглает игорока сделать ход, проверят ход игрока
    в бесконечном цикле:если ход игрока невернй -
    выводит на печать соответствующие комментарии
    и снова прилашает сделать ход.
    Если ход игрока правильный:
    -ход игрока добавляется в множество ходов игрока
    -в списке символов для вывода на игровое поле
    номер квадрата(ход игрока) меняется на символ, который использует игро
    -в списке свободных квадратов удаляется номер - ход игрока
    Выводит на печать обновлённое игровое поле

    :param player: имя игрока
    :param sign: символ, который использует игрок - 'крестик' или 'нолик'
    :param player_moves: множество ходов игрока
    :param symbols: символы для отображения на игровом поле
    :param spare_squares: список из номеров свободных квадратов
    :return: None
    """

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
        request(n, player, sign)
        player_choice = input('Введите номер квадрата: ')

    player_choice_int = int(player_choice)
    player_moves.add(player_choice_int)
    symbols[symbols.index(player_choice_int)] = sign
    spare_squares.pop(spare_squares.index(player_choice_int))
    display.print_paying_field(n, symbols)
    return (player_moves, spare_squares)


def main():
    n, players, signs = preface(players_list, signs_list)
    n = int(n)
    spare_squares = [i for i in range(1, n * n + 1)]
    symbols = spare_squares[:]
    player_moves = [set(), set()]
    count = 0
    idx = 0
    print('-----')
    print(f'Начимаем игру, размер игрового поля {n} x {n}.')
    print('-----')
    sleep(1)
    display.print_paying_field(n, symbols)

    while len(spare_squares) > 0:
        request(players[idx], signs[idx], spare_squares)
        player_move(players[idx], signs[idx], player_moves[idx], symbols, spare_squares, n)
        count += 1
        if count >= 2 * n - 1:
            if check_winner(n, players[idx], player_moves[idx]):
                break
        idx = 1 - idx

    if not spare_squares:
        tie()


if __name__ == '__main__':
    main()
