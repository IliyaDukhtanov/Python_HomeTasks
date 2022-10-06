# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.


def calculate_lcm(x, y): 
    if x > y: 
        greater = x 
    else: greater = y 
    while(True): 
        if greater % x == 0 and greater % y == 0:
            lcm = greater 
            break 
        else: 
            greater += 1 
    return lcm


num1 = int(input("Введите первое число: ")) 
num2 = int(input("Введите второе число: ")) 
print("Наименьшим общим кратным для", num1,"и", num2,"является число", calculate_lcm(num1, num2))
