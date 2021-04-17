"""
Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
Об окончании ввода данных будет свидетельствовать пустая строка.
"""

file_obj = open("user-input.txt", "w")

while True:
    tmp_input = input("input text to save to a file > ")
    if tmp_input:
        file_obj.writelines(tmp_input + "\n")
    else:
        file_obj.close()
        break
