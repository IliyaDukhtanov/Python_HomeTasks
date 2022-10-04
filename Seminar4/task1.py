# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

input_list = list(map(int, input("Введите числа через пробел:\n").split()))
print(max(input_list), min(input_list))



#nums = list(map(int, input('Введите числа через пробел: ').split()))

#nums = input('Введите числа через пробел: ').split()
#l_ist = [int(nums[i]) for i in range(len(nums))]
#l_ist = [int(i) for i in nums]
#print(l_ist)

# # alt - shift - f

# nums = [int(i) for i in input('Введите числа через пробел: ').split()] # list comprehension
# print(nums)
# # print(max(nums), min(nums)) 
# # print(max(nums), min(nums), sep= '+') 
# # print(str(max(nums)) + ' ' + str(min(nums)))
# print(f'{max(nums)} {min(nums)}')
