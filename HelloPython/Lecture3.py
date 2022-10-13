# Ускоренная обработка данных:
# lambda, filter, map, zip, enumerate, List Comprehension


# Анонимные, lambda функции

# sum = lambda x: x+10
# mult = lambda x: x**2
# sum(mult(2))
# f(g(x))
# def h(f, g, x): return f(g(x)) h = lambda f, g, x: f(g(x))
# h(sum, mult, 5)
# h(lambda x: x+10, lambda x: x**2, 5)
# sum1 = lambda x: x+22
# mult2 = lambda x: x**3
# sum1(mult2(2))
# sum4 = lambda x: x+242
# mult4 = lambda x: x**5
# sum3(mult2((2))

# f(g(x))
# def h(f, g, x): return f(g(x))h = lambda f, g, x: f(g(x))
# h(sum, mult, 5)
# h(lambda x: x+10, lambda x: x**2, 5)

# К чему это всё?
# В файле хранятся числа, нужно выбрать четные и составить список пар (число; квадрат числа).
# Пример:
# 1 2 3 5 8 15 23 38
# Получить:
# [(2, 4), (8, 64), (38, 1444)]

# f = open('f.txt', 'r')
# data = f.read() + ' '   # считываем всё, что есть в строке и добавляем пробем
# f.close()
# numbers = []
# while data != '':  # пробегаемся по всей строке с проверкой "Пока строка не пустая"
#     space_pos = data.index(' ')  # найти первую позицию пробела
#     numbers.append(int(data[:space_pos])) # взять всё, что находится от первой позиции до позиции первого пробела, превратить в число
#     data = data[space_pos+1:]   # добавить в список чисел

# out = []
# for e in numbers: # пробегаемя по списку
#     if not e % 2:
#         out.append((e, e **2))  # создаем кортеж чётных чисел
# print(out)


# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]
# data = '1 2 3 5 8 15 23 38'.split()
# data = select(int, data)
# data = where(lambda e: not e % 2, data)
# data = list(select(lambda e: (e, e**2), data))

data = '1 2 3 5 8 15 23 38'.split()
data = list(map(int, data))
data = list(filter(lambda e: not e % 2, data))
#data = list(map(lambda e: (e, e**2), data))
print(data)


# Функция map() применяет указанную функцию к каждому элементу итерируемого объекта и возвращает итератор с новыми объектами.


# Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для которых функция вернула True.


# Функция zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами из элементов входных данных.
# Количество элементов в результате равно минимальному количеству элементов входного набора


# Функция enumerate() применяется к итерируемому объекту и возвращает новый итератор с кортежами
# из индекса и элементов входных данных.