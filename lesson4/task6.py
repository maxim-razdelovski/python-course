"""
Реализовать два небольших скрипта:
- итератор, генерирующий целые числа, начиная с указанного;
- итератор, повторяющий элементы некоторого списка, определённого заранее.

Подсказка: используйте функцию count() и cycle() модуля itertools. 
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Предусмотрите условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3.
При достижении числа 10 — завершаем цикл.

Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.
"""

from itertools import count, cycle

################ count iterator ###################
start_number = 3
numbers = []

for number in count(start_number):
    if number > 10:
        break
    else:
        numbers.append(number)

print(numbers)

print('\n')

################ cycle iterator ###################
my_list = [1, "one", (1, 2), 4.99]

my_cycle_iterator = cycle(my_list)

number_of_cycles = 3
counter = 0

while True :
    print(next(my_cycle_iterator))
    counter += 1
    
    # we want to interrup after repeating the list the given number of times
    if counter >= len(my_list) * number_of_cycles:
        break      
