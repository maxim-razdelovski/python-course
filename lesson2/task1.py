"""
Создать список и заполнить его элементами различных типов данных. 
Реализовать скрипт проверки типа данных каждого элемента. 
Использовать функцию type() для проверки типа. 
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

my_list = [1, 0.5, True, None, [1,3], 'text', b'text', bytearray(b"some text"), (1,2,3)]

for el in my_list:
    print(type(el))

