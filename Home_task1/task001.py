# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

a = int(input("Введите цифру, обозначающую день недели: "))
if a not in range(1,8):
    print("Такого дня недели нет") 
elif a in range(6,8): 
    print("Выходной :)")
else:
    print("Рабочий")


# Вариант 2
#   num = int(input('Input the number of the day: '))
# while num < 1 or num > 7:
#   num = int(input('Wrong input. Try again here: '))
#if num == 6 or num == 7:
#   print('Yes')
#else:
#   print('No')
