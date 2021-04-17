"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""
import functools as ft
import operator

output_file = open("task5-output.txt", "w+")

for i in range(5):
    output_file.write(f" {i} ")

output_file.seek(0)
numbers = output_file.read().split()

result = ft.reduce(operator.add, [int(item) for item in numbers])

print(f"sum = {result}")

output_file.close()