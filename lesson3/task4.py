"""
Программа принимает действительное положительное число x и целое отрицательное число y. 
Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y). 
При решении задания нужно обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами. 
Первый — возведение в степень с помощью оператора **. 
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""

def power_func_simple(base, exponent):
    return base ** exponent

def power_func_loop(base, exponent):    
    result = base
    for i in range(abs(exponent) - 1):
        result = result * base
    return 1 / result  

base = int(input(f"input positive base > "))
exponent = int(input(f"input a negative exponent > "))

result1 = power_func_simple(base, exponent)
result2 = power_func_loop(base, exponent)

print(f"result simple func: {result1}")
print(f"result loop func: {result2}")
