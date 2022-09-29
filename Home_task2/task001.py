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
# print(f"Сумма цифр числа {numb} равна:", summa)

#Вариант 2
number = input("Введите число: ")
n = int(float((number).replace(",", ".")) * (10 ** (len(number) - 2)))
summa = 0 
while (n != 0):
    summa += n % 10
    n = n // 10 
print(f"Сумма цифр числа {number} равна:", summa)