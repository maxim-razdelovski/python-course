"""
Реализовать программу работы с органическими клетками, состоящими из ячеек. 

Необходимо создать класс Клетка. 

В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). 

В классе должны быть реализованы методы перегрузки арифметических операторов: 
- сложение (__add__()) 
- вычитание (__sub__()) 
- умножение (__mul__()) 
- деление (__truediv__()) 

Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.


В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. 

Данный метод позволяет организовать ячейки по рядам.

Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. 
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.

Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.

"""

class Organism:
    def __init__(self, cells_number):
        
        self.cells_number = cells_number
    
    def __add__(self, other):
        return Organism(self.cells_number + other.cells_number)
    
    def __sub__(self, other):
        if (self.cells_number - other.cells_number) > 0:
            return Organism(self.cells_number - other.cells_number)
        else:
            print("the other Organism is bigger than this one, substraction can't proceed!")

    def __mul__(self, other):
        return Organism(self.cells_number * other.cells_number)

    def __truediv__(self, other):
        return Organism(self.cells_number // other.cells_number)

    def __del__(self):
        print('Destructor called, Organism died')

    
    def make_order(self, cells_per_row):
        arrangement  = ''
        for idx, cell in enumerate(range(0, self.cells_number)):
            arrangement += "*"
            if idx > 0 and (idx +1) % cells_per_row == 0:
                arrangement += "\n"
        print(arrangement)

def check_organism_status(organism, cells_per_row=10):
    organism_name = hash(organism)
    print()
    print(f"organism '{organism_name}' is made of {organism.cells_number} cells")
    print(f"and they are arranged in the following structure: ")
    organism.make_order(cells_per_row)
    
    

organism_1 = Organism(6)
organism_2 = Organism(10)
organism_3 = Organism(3)

new_one_from_addition = organism_1 + organism_2

check_organism_status(organism_1, 2)
check_organism_status(organism_2, 5)
check_organism_status(new_one_from_addition, 5)


new_one_from_substraction = organism_2 - organism_1

check_organism_status(new_one_from_substraction, 2)

organism_1 - organism_2

new_from_multiplication = organism_1 * organism_2

check_organism_status(new_from_multiplication)

new_from_division_1 = organism_1 / organism_3
new_from_division_2 = organism_2 / organism_3

check_organism_status(new_from_division_1)
check_organism_status(new_from_division_2)