#3. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# input_str = input()
# text1 = "абв"
# input_list = input_str.split()
# result_list = []
# for word in input_list: 
#     if text1 not in word: 
#         result_list.append(word)
# print(" ".join(result_list))


input_str = input("введите текст: ")
text1 = "абв"
output_str = " ".join(list(filter(lambda x: "абв" not in x, input_str.split())))
print(output_str)