"""
Создать класс TrafficLight (светофор).
 
- определить у него один атрибут color (цвет) и метод running (запуск);

- атрибут реализовать как приватный;

- в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;

- продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;

- переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);

- проверить работу примера, создав экземпляр и вызвав описанный метод.
 
- Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
import time

class TrafficLight:
    __color = None

    def running(self, color):
        # assuming that красный -> жёлтый -> зелёный -> желтый -> красный is the only expected order 
        assert ( self.__color is None 
        or (self.__color == 'red' and color == 'yellow') 
        or (self.__color == 'yellow' and color == 'green')  
        or (self.__color == 'green' and color == 'yellow')
        or(self.__color == 'yellow' and color == 'red') ) ,"Invalid color sequence!"

        self.__color = color

        print(self.__color)

        if(self.__color == 'red'):
            time.sleep(7)
        elif(self.__color == 'yellow'):
            time.sleep(2)
        else:
            time.sleep(5)

tr = TrafficLight()

tr.running('red')
tr.running('yellow')
tr.running('green')
tr.running('red')
# this is invalid as we expect 'yellow' to follow 'red', should throw error
tr.running('green')