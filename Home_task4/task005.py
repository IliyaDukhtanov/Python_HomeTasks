# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# file1 = "D:\Обучение\Практика\Python\Home_task4\Polynomial_task005_1.txt"
# file2 = "D:\Обучение\Практика\Python\Home_task4\Polynomial_task005_2.txt"
# file_sum = "D:\Обучение\Практика\Python\Home_task4\Polynomials_sum.txt"

# def read_pol(file):   # Получение данных из файла
#     with open(str(file), 'r') as data:
#         pol = data.read()
#     return pol


# def polynomial_list(pol):
#     pol = pol.replace("= 0", "")
#     pol = pol.replace("+ ", "")
#     pol_list = pol.split()
#     return pol_list


# pol_sum_str = " + ".join(polynomial_list(read_pol(file1)) + polynomial_list(read_pol(file2)))
# pol_sum_str += " = 0" 
# with open(file_sum, 'a') as data:
#     data.write(pol_sum_str + "\n")


# Вариант препода

def get_coeffs(digits):
    digits = digits.strip().strip(' = 0')
    digits = digits.split(' + ')
    coeffs = {}
    for i in digits:
        a, *b = i.split(' * x ** ')    # (' * x ** ')
        if b:
            coeffs[int(b[0])] = int(a)
        else:
            if i.endswith('x'):
                a, *b = i.split(' * x')    # (' * x')
                coeffs[1] = int(a)
            else:
                coeffs[0] = int(i)
    return coeffs


def sum_coeffs(d, coeffs):
    for key in d:
        if not key in coeffs:
            coeffs[key] = 0
        coeffs[key] += d[key]
    return coeffs


with open('D:\\Обучение\\Практика\\Python\\Home_task4\\Polynomial_task004.txt') as f:
    digits1 = f.read()
    digits2 = digits1[:]
coeffs1 = get_coeffs(digits1)
coeffs2 = get_coeffs(digits2)
coeffs = {}
coeffs = sum_coeffs(coeffs1, coeffs)
coeffs = sum_coeffs(coeffs2, coeffs)
res = ''
max_num = max(coeffs.keys())
for i, j in coeffs.items():
    res += str(j)
    if i != 0 and j != 0 and i != 1:
        res += ' * x ** '     # ' * x ** '
        res += str(i)
        res += ' + '
    elif j == 0:
        continue
    elif i == 1:
        res += ' * x + '     # ' * x + '
    else:
        res += ' = 0'
print(res)
