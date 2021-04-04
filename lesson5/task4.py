"""
Создать (не программно) текстовый файл со следующим содержимым: 
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
"""

rus_dict = { "1": "Один", "2": "Два", "3": "Три", "4": "Четыре" }

def russian_replace(original):
        number = original[2]
        original[0] = rus_dict.get(number)
        return " ".join(original)

with open("task4-text.txt","r") as input_file:
    replaced = []

    for line in input_file:
        replaced_line = russian_replace(line.split())
        replaced.append(replaced_line)

    with open("task4-output.txt", "w") as output_file:
        output_file.writelines(str +  "\n" for str in replaced)
