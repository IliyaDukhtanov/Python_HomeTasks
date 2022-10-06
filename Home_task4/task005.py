# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

file1 = "D:\Обучение\Практика\Python\Home_task4\Polynomial_task005_1.txt"
file2 = "D:\Обучение\Практика\Python\Home_task4\Polynomial_task005_2.txt"
file_sum = "D:\Обучение\Практика\Python\Home_task4\Polynomials_sum.txt"

def read_pol(file):   # Получение данных из файла
    with open(str(file), 'r') as data:
        pol = data.read()
    return pol


def polynomial_list(pol):
    pol = pol.replace("= 0", "")
    pol = pol.replace("+ ", "")
    pol_list = pol.split()
    return pol_list


pol_sum_str = " + ".join(polynomial_list(read_pol(file1)) + polynomial_list(read_pol(file2)))
pol_sum_str += " = 0" 
with open(file_sum, 'a') as data:
    data.write(pol_sum_str + "\n")
