"""
- Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), 
  который должен принимать данные (список списков) для формирования матрицы.

  Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
  Примеры матриц вы найдете в методичке.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

- Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). 
  Результатом сложения должна быть новая матрица.
  Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы 
  складываем с первым элементом первой строки второй матрицы и т.д
"""

class Matrix:
    def __init__(self, list_param, start=0):
        self.matrix = list_param

    def __str__(self):
        string_presentation = ""
        for row in self.matrix:
            for item in row:
                string_presentation += f" {item} " 
            string_presentation += "\n"

        return string_presentation

    def length(self, list_param):
        return len(self.matrix)

    def __add__(self, other):
        matrix_sum = []
        el_pos = 0

        flat_self = [item for sublist in self.matrix for item in sublist]
        flat_other = [item for sublist in other.matrix for item in sublist]

        min_length = len(flat_self) if len(flat_self) < len(flat_other) else len(flat_other)

        for row in self.matrix:
            new_row = []
            for val in row:
                if el_pos >= min_length:
                    break
                new_row.append(flat_self[el_pos] + flat_other[el_pos])
                el_pos += 1

            matrix_sum.append(new_row)        

        return Matrix(matrix_sum)

mtrx2clmn = [[6,5], [4, 3], [2, 1], [0, 0]]

mtrx3clmn_1 = [[1,2, 3], [4, 5, 6]]
mtrx3clmn_2 = [[1,1, 1], [1, 1, 1]]

mtx1 = Matrix(mtrx2clmn)
mtx2 = Matrix(mtrx3clmn_1)
mtx3 = Matrix(mtrx3clmn_2)


print("2 column matrix:")
print(mtx1)

print("3 column matrices:")
print(mtx2)
print(mtx3)

print("sum of two 3 column matrices")
new_matrix = mtx2 + mtx3
print(new_matrix)


print("sum of two non matching matrices")
new_matrix_2 = mtx1 + mtx3
print(new_matrix_2)