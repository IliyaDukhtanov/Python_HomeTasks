# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def simple_factor(m):
    factor_list = []
    d = 2 # первый делитель
    while d * d <= m:
        while m % d == 0:
            factor_list.append(d)
            m = m // d
        d = d + 1
    if m > 1: 
        factor_list.append(m) # Добавим последнее простое число
    return factor_list 


n = int(input("Введите натуральное число N: "))
print(f"Список простых множителей для натурального числа {n}: {simple_factor(n)}")


# Вариант однокурсницы

# import math


# def prime_factors(n):
#     l_ist = []
#     while n % 2 == 0:
#         l_ist.append(2)
#         n = n / 2   
#     for i in range(3, int(math.sqrt(n)) + 1, 2):    # 
#         while(n % i == 0):
#             l_ist.append(i)
#             n = n / i            
#     if n > 1:
#         l_ist.append(int(n))
#     return l_ist
        
        
# num = int(input('Enter the number N for calculation: '))
# print(*prime_factors(num))    # знак * переводит списко в строку