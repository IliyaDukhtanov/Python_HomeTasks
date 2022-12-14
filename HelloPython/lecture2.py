# Файлы

# Как работать с файлами:
# Связать файловую переменную с файлом,
# определив модификатор работы
# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных
# w+, r+

# with open('D:\\Обучение\\Практика\\Python\\HelloPython\\file.txt', 'a') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors) # разделителей не будет
# data.write("LINE 2\n")
# data.write("LINE 3\n")
# data.close()

#exit()

# path = 'D:\\Обучение\\Практика\\Python\\HelloPython\\file.txt'  # чтение данных из файла. Все данные хранятся в текстовом представлении
# data = open(path, 'r')
# list_file = []
# for line in data:
#     list_file.append(line.replace("\n", ""))
# print(list_file)
# data.close()


# Функции

# Это фрагмент программы, используемый
# многократно
# def function_name(x):
# body line 1
# . . .
# body line n
# optional return


# def new_string(symbol, count = 3):
#   return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!!
# print(new_string(4)) # 12

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1', 'd', '2')) # a1d2
# print(concatenatio(1, 2, 3, 4)) # TypeError: ...


# Рекурсия
#Функции
# def fib(n):
# if n in [1, 2]:
# return 1
# else:
# return fib(n-1) + fib(n-2)
# list = []
# for e in range(1, 10):
# list.append(fib(e))
# print(list) # 1 1 2 3 5 8 13 21 34


# Кортеж – это неизменяемый “список”
# t = ()
# print(type(t)) # tuple
# t = (1,)
# print(type(t)) # tuple
# t = (1)
# print(type(t)) # int
# t = (28, 9, 1990)
# print(type(t)) # tuple
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')

# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# # print(t[10]) # IndexError: tuple index out of range
# print(t[-2]) # green
# # print(t[-200]) # IndexError: tuple index out of range
# for e in t:
#     print(e) # red green blue
# t[0] = 'black' #

# a = (3, 4, 5)
# print(a)
# print(a[0])
# for item in a: 
#     print(item)
    
# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue))
# #r:red g:green b:blue


# Словари - Неупорядоченные коллекции произвольных объектов с доступом по ключу
# dictionary = {}
# dictionary = \
# {
# 'up': '↑',
# 'left': '←',
# 'down': '↓',
# 'right': '→'
# }
# # print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# # print(dictionary['left']) # ←
# # # типы ключей могут отличаться

# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# #print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
#     print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# down: ↓
# right: →


# Множества - Неупорядоченная совокупность элементов - достоинство - мгновенный поиск элементов
# a = {1, 2, 3, 5, 8}
# b = {'2', '5', 8, 13, 21}
# print(type(a)) # set
# print(type(b)) # set

# a = {1, 2, 3, 5, 8}
# b = set([2, 5, 8, 13, 21])
# c = set((2, 5, 8, 13, 21))
# print(type(a)) # set
# print(type(b)) # set
# print(type(c)) # set
# a = {1, 1, 1, 1, 1}
# print(a) # {1}

# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# # colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# print(a)
# b = {2, 5, 8, 13, 21}
# print(b)
# c = a.copy() # c = {1, 2, 3, 5, 8}
# print(c)
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
# print(u)
# i = a.intersection(b) # i = {8, 2, 5}
# print(i)
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q = a \
# .union(b) \
# .difference(a.intersection(b))
# {1, 21, 3, 13}


# Неизменяемое множество 
# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

# Списки
# list1 = [1, 2, 3, 4, 5]
# list2 = list1  # копирование спика
# list1[0] = 123 # при изменении элемента в одном из списков, такой же элемент меняется во втором списке
# list2[1] = 333

# for e in list1: 
#     print(e)
# print()
# for e in list2: 
#     print(e)

# list1 = [1, 2, 3, 4, 5]

# print(len(list1))
# print(list1.pop(2)) # удалние последнего элемента списка или конкретного элемента, указав аргумент в pop
# print(list1)

# print(list1.insert(2, 11))  # добавление элемента по индексу
# print(list1)

# print(list1.append(11))   # добавление элемента в конец списка
# print(list1)
