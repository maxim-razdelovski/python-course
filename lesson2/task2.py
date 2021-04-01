"""
Для списка реализовать обмен значений соседних элементов, т.е. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
При нечетном количестве элементов последний сохранить на своем месте. 
Для заполнения списка элементов необходимо использовать функцию input().
"""

my_list = []
input_val = True

while True:
    input_val = input("> ")
    if input_val == 'exit':
        break
    my_list.append(input_val)


print(my_list)

for i in range(len(my_list)):
    if i % 2 == 0 and i < len(my_list) - 1:
        tmp1, tmp2 = my_list[i], my_list[i+1]
        my_list[i], my_list[i+1] = tmp2, tmp1


print(my_list)