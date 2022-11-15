#Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел

import time
now = time.time()
print(now)
print(str(now).split('.')[1][0])


#Опровержение теоремы Эйлера
for a in range(1, 151):
    for b in range(a,151):
        for c in range(b, 151):
            for d in range(c, 151):
                sum_1 = a ** 5 + b ** 5 + c ** 5 + d ** 5
                e = int(sum_1 ** (1/5))
                if sum_1 == e ** 5:
                    print(a, b, c, d, e, "сумма", a+b+c+d+e)


