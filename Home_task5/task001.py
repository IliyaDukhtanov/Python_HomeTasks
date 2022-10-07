# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


def string_edit(my_str, symbols):
    return (" ".join([word for word in my_str.split() if symbols not in word]))


input_str = input("Введите текст:\n")
text1 = input("Введите сочетание символов для удаления слов:\n")
print(string_edit(input_str, text1))
