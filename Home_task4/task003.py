# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from collections import Counter
from random import randint

def create_list(k, m, n):    # создание списка случайных чисел указанного диапазона в соответствии с указанным количеством элементов
    return [randint(m, n) for i in range(k)]


k = int(input("Введите количество чисел в списке: "))
m = int(input("Введите нижнюю границу чисел: "))
n = int(input("Введите верхнюю границу чисел: "))
input_list = create_list(k, m, n)
output_list = [k for k, v in Counter(input_list).items() if v == 1]
print("Исходная последовательность чисел: ", input_list)
print("Неповторяющиеся числа: ", output_list)


# Вариант со словарём

# dict_new = {}
# for i in item_set: 
#     if not i in dict_new:
#         dict_new[i] = 0
#     dict_new[i] += 1
# res_list = []
# for i in dict_new:
#     if dict_new[i] == 1:
#         res_list.append(i)
# print(res_list)           

