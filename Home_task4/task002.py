# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def simple_factor(m):
    factor_list = []
    d = 2 # первый делитель
    while d * d <= m:
        if n % d == 0:
            factor_list.append(d)
            m //= d
        else:
            d += 1
    factor_list.append(m) # Добавим последнеё простое число
    return factor_list 


n = int(input("Введите натуральное число N: "))
print(f"Список простых множителей для натурального числа {n}: {simple_factor(n)}")