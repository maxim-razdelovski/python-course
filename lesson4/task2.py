# coding=UTF-8
"""
Представлен список чисел. Необходимо вывести элементы исходного списка, 
значения которых больше предыдущего элемента.

Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.

Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].

Результат: [12, 44, 4, 10, 78, 123].
"""

my_array = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
expected = [12, 44, 4, 10, 78, 123]

larger_elements = [el for idx, el in enumerate(my_array) if idx != 0 and my_array[idx] > my_array[idx - 1]]

assert larger_elements == expected, "resulting array is incorrect! check your generator logic"

print(larger_elements)
