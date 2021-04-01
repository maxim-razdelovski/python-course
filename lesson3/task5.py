"""
Программа запрашивает у пользователя строку чисел, разделённых пробелом. 
При нажатии Enter должна выводиться сумма чисел. 
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter. 
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.

Если специальный символ введен после нескольких чисел, 
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

input_numbers = []
should_break = False

while True:
    current_input = input(f"input space separated numbers ('q' to exit) > ")
    split_input = current_input.split()
    should_break
    if 'q' in split_input:
        split_input.remove('q')
        should_break = True
    
    input_numbers.append(list(map(int, split_input)))
    # using list comprehension to flatten our list of lists
    flattened_list = [item for sublist in input_numbers for item in sublist]

    print(f"total = {sum(flattened_list)}")

    if should_break:
        break