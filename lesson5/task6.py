"""
Сформировать (не программно) текстовый файл. 
В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету. 
Сюда должно входить и количество занятий. 
Необязательно, чтобы для каждого предмета были все типы занятий.

Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.

Примеры строк файла:

    Информатика:   100(л)   50(пр)   20(лаб).
    Физика:   30(л)   —   10(лаб)
    Физкультура:   —   30(пр)   —

Пример словаря: 
    {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

import re
import functools as ft
import operator

result_dic = {}

def extract_hours(str):
    match = re.search('([0-9])*', str)
    if match:
        return int(match.group() if match.group() else 0)
    
    return 0

def parse_line(line):
    subject, lectures, practical, lab = line.split()    
    return (subject.strip(":"), extract_hours(lectures), extract_hours(practical), extract_hours(lab))

def populate_dict(subject_info):
    subject, *rest = subject_info
    result_dic[subject] = ft.reduce(operator.add, rest)


with open("task6-text.txt","r") as input_file:
    for line in input_file:
        parsed = parse_line(line)
        populate_dict(parsed)
    
    print('total hours by subject: \n')
    print(result_dic)

