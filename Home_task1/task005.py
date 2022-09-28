# 5.Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве. 
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

import math

xa = int(input("Введите координату X точки A: "))
ya = int(input("Введите координату Y точки A: "))
xb = int(input("Введите координату X точки B: "))
yb = int(input("Введите координату Y точки B: "))

d = round(math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2), 2) # можно ** 0.5 - квадратный корень
print("Расстояние между точками A и В равно",d)


# Вариант 2
# ax = float(input('Enter the x coordinate of the point A: '))
# ay = float(input('Enter the y coordinate of the point A: '))

# bx = float(input('Enter the x coordinate of the point B: '))
# by = float(input('Enter the y coordinate of the point B: '))

# distance_2d = round(((bx - ax) ** 2 + (by - ay) ** 2) ** 0.5, 2)
# print(distance_2d)
