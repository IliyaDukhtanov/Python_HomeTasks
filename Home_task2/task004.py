# Реализуйте алгоритм перемешивания списка.
import random 

n = int(input("Введите количество элементов: "))
input_list = [i for i in range(n)]
result_list = input_list[:]
for i in range(n):
    index_random = random.randint(0, n - 1)
    temp = result_list[i]
    result_list[i] = result_list[index_random]
    result_list[index_random] = temp
print("Исходный список",input_list)
print("Перемешанный список",result_list)
