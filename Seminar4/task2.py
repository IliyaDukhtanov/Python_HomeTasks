# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# - с помощью математических формул нахождения корней квадратного уравнения
# - с помощью дополнительных библиотек Python (например, numpy.roots)


# a = float(input("Введите число A: "))
# b = float(input("Введите число B: "))
# с = float(input("Введите число C: "))
# discr = (b ** 2) - (4 * a * с)
# print(discr)
# if discr > 0: 
#     x1 = round((-b + ((discr) ** 0.5)) / (2 * a), 2)
#     x2 = round((-b - ((discr) ** 0.5)) / (2 * a), 2)
#     print(x1, x2)
# elif discr == 0:
#     x1 = round(-b / (2 * a), 2)
#     print(x1)
# elif discr < 0: 
#     print('Нет корней')

import numpy as np

p = [1, 5, 6]
a, b = np.roots(p)
print(a, b)

