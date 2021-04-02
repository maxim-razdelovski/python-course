"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. 
Используйте в нём формулу: (выработка в часах*ставка в час) + премия. 
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv
from math import modf

script_name, hours, rate, bonus = argv

def calculate_pay(hours, rate, bonus):
    return float(hours) * float(rate) + float(bonus)

pay = calculate_pay(hours, rate, bonus)

cents, dollars = modf(pay)

print(f"worker's pay is {int(dollars)} dollars and {cents * 100:.2f} cents")