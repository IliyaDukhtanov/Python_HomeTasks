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