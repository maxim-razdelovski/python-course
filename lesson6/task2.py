"""
Реализовать класс Road (дорога).
 
- определить атрибуты: length (длина), width (ширина);
- значения атрибутов должны передаваться при создании экземпляра класса;
- атрибуты сделать защищёнными;
- определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
- использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
- проверить работу метода.
 
Например: 20м * 5000м *25кг * 5 см = 12500 т.

"""

class Road:
    __weight_of_m2_1cm_thick = 25

    def __init__(self, length, width):
        self._length = length
        self._width = width
    
    def calculate_weight(self, thickness):
        '''
        Returns the weight in function of the layer thinkness.

                Parameters:
                        thinkness in cm (int): A decimal integer

                Returns:
                        calculate_weight (int): total weight in kg
        '''        
        weight = self._length * self._width * self.__weight_of_m2_1cm_thick * thickness        
        return weight


rd = Road(5000, 20)

total_weight = rd.calculate_weight(5)

print(f"total weight of the asphalt = {total_weight / 1000} tn")
