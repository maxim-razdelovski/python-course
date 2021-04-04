"""
Создать вручную и заполнить несколькими строками текстовый файл, 
в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки. 

Пример строки файла: firm_1   ООО   10000   5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 

Если фирма получила убытки, в расчёт средней прибыли её не включать.

Далее реализовать список. 
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить её в словарь (со значением убытков). 

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.

Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
"""

import functools as ft
import json

result_list = []
parsed_data = []

def parse_line(line):
    company, _, income, expenses = line.split()    
    return (company, float(income), float(expenses))

with open("task7-text.txt","r") as input_file:
    for line in input_file:
        parsed_data.append(parse_line(line))

profit = ft.reduce((lambda x, y: x + y), [(item[1] - item[2]) for item in parsed_data if item[1] > item[2] ])
profitable_companies_count = len([ item for item in parsed_data if item[1] > item[2] ])
average_profit = profit / profitable_companies_count

for data in parsed_data:
    result_list.append({ data[0] : data[1] - data[2] })

result_list.append({"average_profit": float("{:.2f}".format(average_profit)) })

print(result_list)

with open("task7-out.json","w", encoding='utf-8') as output_file:
    json.dump(result_list, output_file, ensure_ascii=False)