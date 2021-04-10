"""
Реализуйте базовый класс Car.
 
- у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
  А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);

- опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;

- добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;

- для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) 
  должно выводиться сообщение о превышении скорости.
 
- Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

"""

class Car:
    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f"{self.__class__.__name__} is moving")
    
    def stop(self):
        print(f"{self.__class__.__name__} has stopped")

    def turn(self, direction):
        print(f"{self.__class__.__name__} has turned {direction}")

    def show_speed(self):
        print(f"current speed is \t{self.speed}")
class TownCar(Car):
    def __init__(self, name, speed, color):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f"current speed is {self.speed} - this speed is too high for this type of car!")
        else:
            print(f"current speed is {self.speed}")

class WorkCar(Car):
    def __init__(self, name, speed, color):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f"current speed is {self.speed} - this speed is too high for this type of car!")
        else:
            print(f"current speed is {self.speed}")
class SportCar(Car):
    def __init__(self, name, speed, color):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = False

class PoliceCar(Car):
    def __init__(self, name, speed, color):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = True

def show_full_car_info(car):
    print("info about car:")
    print(f"vehicle type:\t{car.__class__.__name__}")
    print(f"name:\t\t{car.name}")  
    print(f"color:\t\t{car.color}")
    print(f"status:\t\t{'a police car' if car.is_police else 'NOT a police car'}")
    car.show_speed()
    print("")
    

generic_car = Car("Just A Car", 55, "white", False)
show_full_car_info(generic_car)
generic_car.go()
generic_car.turn('left')
generic_car.stop()
print("")

town_car_slow = TownCar("Toyota Corolla", 50, "blue")
show_full_car_info(town_car_slow)
town_car_slow.go()
town_car_slow.turn('right')
town_car_slow.stop()
print("")

town_car_too_fast = TownCar("Toyota Corolla", 65, "blue")
show_full_car_info(town_car_too_fast)
town_car_too_fast.go()
town_car_too_fast.turn('right')
town_car_too_fast.stop()
print("")

sports_car = SportCar("Honda Civic Type R", 210, "red")
show_full_car_info(sports_car)
sports_car.go()
sports_car.turn("right")
sports_car.stop()
print("")

police_car = PoliceCar("Ford", 180, "white-blue")
show_full_car_info(police_car)
police_car.go()
police_car.turn("right")
police_car.stop()