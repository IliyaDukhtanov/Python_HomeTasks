# print('hello world')

#a = 123
#b = 1.23
#print(a)
#print(b)
#s = 'hello world'
#print(a, b, s)
#f = false 

#list = []
#print(list)

#print('Введите a')
#a = int(input())  # указать какой тип данных на входе
#print('Введите b')
#b = int(input())
#print(a, ' + ', b, ' = ', a + b)
#print('{} {}'.format(a, b))

#a = 123
#b = 321 
#c = a + b
#print(c) 

#Арифметические операции
# +, -, *, /, %, //, **

# Приоритет операций
# **, ⊕, ⊖, *, /, //, %, +, -
# ( ) Скобки меняют приоритет

# exp1 = 2**3 - 10 % 5 + 2*3
# exp2 = 2**3 - 10 / 5 + 2*3   (2**3) - (10 / 5) + (2*3)
# print(exp1) # 14.0 или 14
# print(exp2) # 12.0 или 12

# Сокращённые операции и операции присваивания
# Демонстрация
# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5  - целочисленное деление
# iter %= 5 # iter = iter % 5   - остаток от деления
# iter **= 5 # iter = iter ** 5 - возведение в степень

# (), Сокращенные операции
#a = 5
#a +=5

#Логические операции 
#>, >=, <, <=, ==, !=
#not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in

#f = [1,2,3,4]
#print(f)
#print(not 2 in f)
#is_odd = f[0] % 2 == 0
#is_odd = not f[0] % 2

# Управляющие конструкции: if, if-else 
#a = int(input('a = '))
#b = int(input('b = '))
#if a > b:
#    print(a)
#else:
#    print(b) 

#Управляющие конструкции: while

#original = 23
#inverted = 0
#while original != 0:
#    inverted = inverted * 10 + (original % 10)
#    original //= 10
#else: 
#    print('Пожалуй')
#    print('хватит )')
#print(inverted)

# Управляющие конструкции: for

# list = range (10)                    #[1,2,3,4,10,5,]
#for i in range (3, 10, 2):
#    print(i)

#Немного о строках
#text = 'съешь ещё этих мягких французских булок'
#print(len(text)) # 39
#print('ещё' in text) # True
#print(text.isdigit()) # False
#print(text.islower()) # True
#print(text.replace('ещё','ЕЩЁ')) #
#for c in text:
#    print(c)

# Срезы
#text = 'съешь ещё этих мягких французских булок'
#print(text[0]) # c
#print(text[1]) # ъ
#print(text[len(text)-1]) # к
#print(text[-5]) # б
#print(text[:]) # print(text)
#print(text[:2]) # съ
#print(text[len(text)-2:]) # ок
#print(text[2:9]) # ешь ещё
#print(text[6:-18]) # ещё этих мягких
#print(text[0:len(text):6]) # сеикакл
#print(text[::6]) # сеикакл
#text = text[2:9] + text[-5] + text[:2] # ...

# Списки: Введение 

#numbers = [1, 2, 3, 4, 5]
#print(numbers)                     # [1, 2, 3, 4, 5]
#numbers = list(range(1, 6))   # приведение типа range к типу list
#print(numbers)                     # [1, 2, 3, 4, 5]
#numbers[0] = 10
#print(numbers)                     # [10, 2, 3, 4, 5]
#for i in numbers:
#i *= 2
#print(i)                           # [20, 4, 6, 8, 10]
#print(numbers)                     # [10, 2, 3, 4, 5]

#colors = ['red', 'green', 'blue']
#for e in colors:
#    print(e) # red green blue
#for e in colors:
#    print(e*2) # redred greengreen blueblue
#colors.append('gray') # добавить в конец
#print(colors == ['red', 'green', 'blue', 'gray']) # True
#colors.remove('red') #del colors[0] # удалить элемент

# Функции
#Это фрагмент программы, используемый многократно

# def f(x):
#    return x**2
# def f(x):
#    if x == 1:
#        return 'Целое'
#    elif x == 2.3:
#       return 23
#    else:
#        return
# print(f(1)) # Целое
# print(f(2.3)) # 23
# print(f(28)) # None
# print(type(f(1))) # str
# print(type(f(2.3))) # int
# print(type(f(28))) # NoneType