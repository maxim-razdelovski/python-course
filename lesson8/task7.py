"""
Реализовать проект «Операции с комплексными числами». 

Создайте класс «Комплексное число». 

Реализуйте перегрузку методов сложения и умножения комплексных чисел. 
Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа), 
выполните сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.

"""

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary, self.real * other.imaginary + self.imaginary * other.real)

    def __str__(self):
        return str(complex(self.real, self.imaginary))

cn1 = ComplexNumber(2, -3)
cn2 = ComplexNumber(1, 2)

print(cn1)
print(cn2)

print(f"addition result: {cn1 + cn2}")  

print(f"multiplication result: {cn1 * cn2}")
