# 1. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.


def read_numbers(file):   # Получение данных из файла
    with open(str(file), 'r') as data:
        numbers = data.read()
    return [int(i) for i in numbers.split()]


file1 = "D:/Обучение/Практика/Python/Seminar5/numbers.txt"
temp_result = read_numbers(file1)
for i in range(1, len(temp_result)):
    if temp_result[i - 1] != temp_result[i] - 1:
        print(temp_result[i -1] + 1)

print(temp_result)
