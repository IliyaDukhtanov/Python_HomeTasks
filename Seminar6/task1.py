# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный. 
#     *Пример:* 
#     2+2 => 4;    
#     1+2*3 => 7;  
#     1-2*3 => -5;  
#     - Добавьте возможность использования скобок, меняющих приоритет операций.    
#         *Пример:*   
#         1+2*3 => 7;      
#         (1+2)*3 => 9;
# Обратная польская запись

input_list = input("Введите выражение: ").split()
output = []
stack_list = []
for elem in input_list:
    if elem.isdigit(): 
        output.append(elem)
    elif elem == "(": # помещаем в стек (первый вошел, последний вышел)
        stack_list.append(elem)
    elif elem == ")":
        while stack_list and stack_list[-1] != "(":
            output.append(stack_list.pop())  # забираем последний элемент из stack и помещаем в output
        if not stack_list:
            print("Несогласованные скобки")
            exit() 
        stack_list.pop()
    elif elem in ["*", "/"]:
        while stack_list and stack_list[-1] in ["*", "/"]:
            output.append(stack_list.pop()) 
        stack_list.append(elem)
    elif elem in ["+", "-"]: 
        while stack_list and stack_list[-1] in ["*", "/", "+", "-"]:
            output.append(stack_list.pop()) 
        stack_list.append(elem)
    else: 
        print("Нераспознанный знак")
        exit()
while stack_list: 
    if stack_list[-1] not in ["*", "/", "+", "-"]:
        print("Несогласованные скобки")
        exit() 
    output.append(stack_list.pop())
print(output)
res = []
for elem in output: 
    if elem.isdigit():
        res.append(int(elem))
    else: 
        b = res.pop()
        a = res.pop()
        if elem == "+":
            res.append(a + b)
        elif elem == "-":
            res.append(a - b)
        elif elem == "*": 
            res.append(a * b)
        elif elem == "/": 
            res.append(a / b)

print(res[0])

