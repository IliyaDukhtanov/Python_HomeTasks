# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

#s = input("Введите строку: ")
#input_list = ["q1we", "asd3", "zxc4", "qw2e", "ert5qwe"]
input_list = [1, 3, 4, 2, 5]
m = int(input("Введите число: "))
#for i in input_list:
if m in input_list:
    print("true")
else:
    print("Число не входит в список")

