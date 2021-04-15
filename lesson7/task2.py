"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. 

Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название. 
К типам одежды в этом проекте относятся пальто и костюм. 

У этих типов одежды существуют параметры: 

- размер (для пальто) 
- рост (для костюма)

Это могут быть обычные числа: V и H, соответственно. 

Для определения расхода ткани по каждому типу одежды использовать формулы: 
- для пальто (V/6.5 + 0.5) 
- для костюма (2*H + 0.3). 

Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. 

Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod

class Clothes(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def calculate_cloth_usage(self):
        pass

class Coat(Clothes):
    name = ''

    def __init__(self, name):
        self.name = name

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 36:
            print("size can't be so small! setting the minimum size")
            self.__size = 36
        elif size > 56:
            print("size can't be so large! setting the max size")
            self.__size = 56
        else:
            self.__size = size

    def calculate_cloth_usage(self):
        return self.__size / 6.5 + 0.5

class Suit(Clothes):
    name = ''

    def __init__(self, name):
        self.name = name

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 1.50:
            print("height can't be so small! setting the minimum height")
            self.__height = 1.50
        elif height > 2.00:
            print("height can't be so big! setting the max height")
            self.__height = 2.00
        else:
            self.__height = height

    def calculate_cloth_usage(self):
        return self.__height * 2 + 0.3

coat_1 = Coat("elegant")
coat_1.size = 46

suit_1 = Suit("formal")
suit_1.height = 1.75

print(f"{coat_1.name} {coat_1.__class__.__name__} needs {coat_1.calculate_cloth_usage():.02f} m2 of cloth" )
print(f"{suit_1.name} {suit_1.__class__.__name__} needs {suit_1.calculate_cloth_usage():.02f} m2 of cloth" )

clothes_produced = [suit_1, coat_1]
clothes_needed = 0

for item in clothes_produced:
    clothes_needed += item.calculate_cloth_usage()

print(f"total cloth needed: {clothes_needed:.02f} m2")