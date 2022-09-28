# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

#Вариант 1
# numb = input("Введите число: ") 
# summa = 0
# for digit in numb:
#     if digit.isdigit():
#         summa += int(digit)
#print(f"Сумма цифр числа {numb} равна:", summa)

#Вариант 2
numb = input("Введите число: ")
n = len(numb)
number = int(numb) * 10 ** n
summa = 0 
for i in range(n):
    summa += number % 10
    number // 10 
    print(summa)