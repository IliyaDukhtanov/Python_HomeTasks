# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# input_list = input("Введите список чисел, разделенных пробелом: ").split()
# odd_sum = 0
# for i in range(1, len(input_list), 2):
#     if input_list[i].isdigit():
#         odd_sum += int(input_list[i])
#     else:
#         continue
# print("\nИсходный список элементов:",input_list)
# print("Сумма элементов, находящихся на нечётных позициях:",odd_sum)


# Вариант написания кода выше с использованием List Comprehension

input_list = input("Введите список чисел, разделенных пробелом: ").split()
print(sum([int(input_list[i]) for i in range(1, len(input_list), 2) if input_list[i].isdigit()]))
