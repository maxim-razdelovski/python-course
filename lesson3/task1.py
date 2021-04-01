"""
 Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
 Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def div_func(a, b):
    if b == 0:
        return "division by 0 is not allowed"
    return a / b

arguments = []

while len(arguments) != 2:
    arguments.append(int(input(f"input argument #{len(arguments) + 1} > ")))

result = div_func(arguments[0], arguments[1])

print(result)