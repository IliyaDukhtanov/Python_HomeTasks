# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
from random import randint, choice

def play_game0(a, b, pl, mes):   # игра человек против человека
    count = choose_first_move()
    print(f'\nПервый ход достаётся игроку {pl[count % 2]}')
    while a > 0:
        print(f'\n{pl[count % 2]}, {random.choice(mes)}')   # циклы перехода хода и попытки взять конфеты
        move = int(input())
        if move > a or move > b:
            print(f'Не пытайтесь взять слишком много конфет, можно взять не более {b}, текущее количество конфет: {a}')
            attempt = 3
            while attempt > 0:
                if a >= move <= b:
                    break
                print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                move = int(input())
                attempt -= 1
            else: 
                return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        a -= move
        if a > 0: 
            print(f'Количество оставшихся конфет: {a}')
        else: 
            print('Все конфеты разобраны.')
        count += 1
    return pl[not count % 2]


def play_game1(a, b, pl, mes):   # игра с ботом
    count = choose_first_move()
    print(f'\nПервый ход достаётся игроку {pl[count]}!')
    while a > 0:
        if count % 2:
            move = randint(1, b)
            print(f'\nБот-сластёна забрал {move}')
        else:
            print(f'\n{pl[0]}, {choice(mes)}')
            move = int(input())
            if move > a or move > b:
                print(f'Не пытайтесь взять слишком много конфет, можно взять не более {b}, текущее количество конфет: {a}')
                attempt = 3
                while attempt > 0:
                    if a >= move <= b:
                        break
                    print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        a -= move
        if a > 0:
            print(f'Количество оставшихся конфет: {a}')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return pl[count % 2]


def play_game2(a, b, pl, mes):    # игра со смарт-ботом
    count = choose_first_move()
    print(f'\nПервый ход достаётся игроку {pl[count]}!')
    while a > 0:
        if count % 2:
            move = a % (b + 1)
            if move == 0:
                move = randint(1, b)
            print(f'\nБот-сластёна забрал {move}')
        else:
            print(f'\n{pl[0]}, {choice(mes)}')
            move = int(input())
            if move > a or move > b:
                print(f'Не пытайтесь взять слишком много конфет, можно взять не более {b}, текущее количество конфет: {a}')
                attempt = 3
                while attempt > 0:
                    if a >= move <= b:
                        break
                    print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        a -= move
        if a > 0:
            print(f'Количество оставшихся конфет: {a}')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return pl[not count % 2]


def choose_first_move():   #  определение игрока, делающего ход первым
    return randint(0, 1)


def introduce_players(d):
    if d == 0:
        player1 = input('\nДавайте познакомися. Первый игрок, как к Вам можно обращаться?\n')
        player2 = input('\nВторой игрок, и Вы представьтесь, пожалуйста\n')
        return [player1, player2]
    else: 
        player1 = input('\nДавайте познакомися. Как Вас зовут?\n')
        player2 = 'Бот-сластёна'
        print(f'\nЗа компьютер играет {player2}')
        return [player1, player2]


def game(d):
    if d == 0: 
        winner = play_game0(n, m, players, messages)
    elif d == 1:
        winner = play_game1(n, m, players, messages)
    elif d == 2:
        winner = play_game2(n, m, players, messages)

    if not winner:
        print('У нас нет победителя.')
    else: print(f'Поздравляю! В этот раз победил {winner}! Ему достаются все конфеты!')

    
greeting = ('\nЗдравствуйте! Это игра "Забери все конфеты!" '
    '\nОсновные правила игры: '
    '\nНам будет дано некоторое количество конфет, '
    'за один ход мы можем взять не более определённого количества, '
    'о котором мы с вами договоримся.'
    '\nПраво первого хода будет определено случайным образом'
    '\nИтак, начнём!\n')
            
messages = ['Ваша очередь брать конфеты', 'возьмите конфеты', 
            'сколько конфет возьмёте?', 'берите конфеты, не стесняйтесь', 'Ваш ход', 'берите конфетки', 'пора брать конфетки']

print(greeting)

n = int(input('Сколько конфет будем разыгрывать?\n'))
m = int(input('Сколько максимально будем брать конфет за один ход?\n'))
lvl = int(input('Выберите уровень сложности: '
        '\n0 - Игра человек против человека'
        '\n1 - Игра с компьютером'
        '\n2 - Играс с компьютером, который любит конфеты\n'))

players = introduce_players(lvl)
winner = game(lvl)
