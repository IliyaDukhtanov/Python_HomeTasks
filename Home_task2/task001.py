# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

#Вариант 1
numb = input("Введите число: ") 
sum1 = 0
for digit in numb:
    if digit.isdigit():
        sum1 += int(digit)
print(f"Сумма цифр числа {numb} равна:", sum1)

#Вариант 2
# number = input("Введите число: ")
# n = int(float((number).replace(",", ".")) * (10 ** (len(number) - 2)))
# sum1 = 0 
# while n != 0:
#     sum1 += n % 10
#     n = n // 10 
# print(f"Сумма цифр числа {number} равна:", sum1)