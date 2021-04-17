# coding=UTF-8
"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
Проверьте его работу на данных, вводимых пользователем. 
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class MyZeroDivisionException(Exception):
    def __init__(self, message):
        self.message = message

number_to_divide = 77

while True:
    try:
        input_val = input("input number, 'q' to exit >> ")
        if input_val == 'q':
            break   
        input_number = int(input_val)     
        if input_number == 0:
            raise MyZeroDivisionException("can't divide by zero!")
        result = number_to_divide / input_number
    except ValueError:
        print("only integers are allowed as user input")
    except MyZeroDivisionException as exc:
        print(exc.message)        
    else:
        print(f"{number_to_divide} divided by {input_val} = { result }")