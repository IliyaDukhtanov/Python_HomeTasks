# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

## Вариант 1
def negaFibonacci(n):
    list_negaFibonacci = [-1, 1, 0, 1, 1]
    fib1 = fib2 = 1
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        list_negaFibonacci.append(fib2)
        list_negaFibonacci.insert(0, (fib2 * (-1) ** i))
    return list_negaFibonacci
n = int(input("Введите число: "))
print((f"Список чисел (нега)Фибоначчи для k = {n}: {negaFibonacci(n)}"))


## Вариант 2
# n = int(input("Введите число: "))
# def fibonacci(n):
#     if n in [1, 2]:
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
# list_negaFibonacci = [0]
# for i in range(1, n + 1):
#     list_negaFibonacci.append(fibonacci(i))
#     list_negaFibonacci.insert(0, (fibonacci(i)*(-1)**(i + 1)))
# print(f"Список чисел (нега)Фибоначчи для k={n}: {list_negaFibonacci}")
