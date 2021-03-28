"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента 
и возвращает сумму наибольших двух аргументов.
"""

def sum_biggest_two(arg1, arg2, arg3):
    arguments = [arg1, arg2, arg3]
    sorted_arguments = sorted(arguments, reverse=True)
    return sorted_arguments[0] + sorted_arguments[1]

result = sum_biggest_two(7, 2, 3)

print(result)