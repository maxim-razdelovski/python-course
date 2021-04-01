"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. 
У пользователя необходимо запрашивать новый элемент рейтинга. 
Если в рейтинге существуют элементы с одинаковыми значениями, 
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

my_list = [7, 5, 3, 3, 2]
user_input = None

while True:
    user_input = input("add number ('q' to exit) > ")
    if user_input == "q":
        break
    number_to_insert = int(user_input)

    # find last occurence of this number in the list and insert it after 
    reversed_list = list(reversed(my_list))
    idx_of_last = reversed_list.index(number_to_insert) if number_to_insert in reversed_list else -1

    if idx_of_last != -1:
        reversed_list.insert(idx_of_last, number_to_insert)
        my_list = list(reversed(reversed_list))        
    else: # when not in the list - find index of an item smaller than our number to insert
        found_smaller = False
        
        for idx, el in enumerate(my_list):
            if el < number_to_insert:
                found_smaller = True
                my_list.insert(idx, number_to_insert)
                break
        
        if not found_smaller:
            my_list.append(number_to_insert)


print(my_list)