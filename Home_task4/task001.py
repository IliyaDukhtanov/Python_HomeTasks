# Вычислить число c заданной точностью d
# Пример:
# при $d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$
# Можно округлить пи из math, там точность 15 знаков

# Формула Лейбница для вычисления Пи:

# from cmath import pi

# def calc_pi(d):
#     k = 1      # знаменатель формулы Лейбница
#     my_pi = 0
#     for i in range (d):
#         if i % 2 == 0:      # определение чётного элемента для дальнейшего сложения 
#             my_pi += 4 / k
#         else:               # опредление нечётного элемента для вычитания
#             my_pi -= 4 / k
#         k += 2
#     return my_pi


# d = int(input("Введите требуемую точность: "))
# n = int(input("Введите количество знаков после запятой для вывода результата: "))
# print("Результат вычисления числа Пи:", calc_pi(d))
# print (f'Число Пи: {f"%.{len(str(int(calc_pi(d)))) + n + 1}s" % (calc_pi(d))}')
# print (f'Число Пи: {f"%.{len(str(int(pi))) + n + 1}s" % (pi)}')


# Варианты однокурсницы

# from math import pi
# from decimal import Decimal

# num = str(pi)                               # Можно использовать pi

# # num = input('Input the number: ')         # Можно использовать введенное число
# d = input('Input the necessary precision number d: ')

# # num = Decimal(num)
# # num = num.quantize(Decimal(str(d)))

# # num = Decimal(num).quantize(Decimal(d)) # 2 строки объединила.
# # print(num)

# print(Decimal(num).quantize(Decimal(d))) # еще 2 строки объединила.

# #==============================

# # Через функцию.

# # def num_precise(n_um, d_c):
# #     n_um = Decimal(n_um)
# #     n_um = n_um.quantize(Decimal(d_c))
    
# #     return n_um


# # num = input('Input the number: ')
# # d = input('Input the necessary precision number d: ')
# # print(num_precise(num, d))
