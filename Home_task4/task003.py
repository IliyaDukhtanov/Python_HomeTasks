# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from collections import Counter

input_list = list(map(int, input("Введите последовательность чисел через пробел:\n").split()))
output_list = [k for k, v in Counter(input_list).items() if v == 1]
print("Исходная последовательность чисел: ", input_list)
print("Неповторяющиеся числа: ", output_list)
