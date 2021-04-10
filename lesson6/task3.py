"""
Реализовать базовый класс Worker (работник).
 
- определить атрибуты: name, surname, position (должность), income (доход);

- последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, 
  например, {"wage": wage, "bonus": bonus};

- создать класс Position (должность) на базе класса Worker;

- в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);

- проверить работу примера на реальных данных: создать экземпляры класса Position, 
  передать данные, проверить значения атрибутов, вызвать методы экземпляров.

"""

class Worker:
    def __init__(self, name, surname, position_name, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = ""
        self._income = { "wage": wage, "bonus": bonus }


class Position(Worker):
    def __init__(self, name, surname, position_name, wage, bonus):
        super().__init__(name, surname, position_name, wage, bonus)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")

position = Position("Jon", "Doe", "Head of Department", 1000, 500)

full_name = position.get_full_name()
total_income = position.get_total_income()

print(f"Employee's info: \n - full name: {full_name} \n - total income ${total_income}")