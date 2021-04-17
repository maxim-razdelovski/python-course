# coding=UTF-8
"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. 
Запрашивать у пользователя данные и заполнять список необходимо только числами. 
Класс-исключение должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, 
введя, например, команду «stop». 
При этом скрипт завершается, сформированный список с числами выводится на экран.

Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. 
Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента. 
Вносить его в список, только если введено число. 
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. 
При этом работа скрипта не должна завершаться.
"""

class MyOnlyNumbersList():
    class MyTypeErrorException(Exception):
        def __init__(self, message):
            self.message = message

    def __init__(self):
        self.list = list()

    def append(self, value):
        self.list.append(self.check_parse(value))
    
    def check_parse(self, value):
        try:
            parsed = float(value)
            return parsed
        except:
            raise self.MyTypeErrorException(f"'{ value }' is not allowed value type")
        
        try:
            parsed = int(value)
            return parsed
        except:
            raise self.MyTypeErrorException(f"'{ value }' is not allowed value type")

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n > len(self.list) - 1:
            raise StopIteration            
        else:
            item = self.list[self.n]
            self.n += 1
            return item

    def __str__(self):
         return " ".join([str(el) for el in self.list])

my_typed_list = MyOnlyNumbersList()

while True:
    try:
        input_val = input("input number, 'q' to exit >> ")
        if input_val == 'q':
            break 
        my_typed_list.append(input_val)    
    except Exception as exc:
        print(exc)
    else:
        print(f"added {input_val} to list")

print(my_typed_list)