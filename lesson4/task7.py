"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. 
При вызове функции должен создаваться объект-генератор. 

Функция вызывается следующим образом: for el in fact(n). Она отвечает за получение факториала числа. 
В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.

Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""

import operator

def fact(n):
    factorial = 1
    for number in range(1, n + 1):
        factorial = number * factorial
        yield factorial

for f in fact(9):
    print(f)