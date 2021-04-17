"""
Реализовать класс Stationery (канцелярская принадлежность).
 
- определить в нём атрибут title (название) и метод draw (отрисовка). 
  Метод выводит сообщение «Запуск отрисовки»;

- создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);

- в каждом классе реализовать переопределение метода draw. 
  Для каждого класса метод должен выводить уникальное сообщение;

- создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("starting drawing")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    
    def draw(self):
        super().draw()
        print(f"using a {self.title}")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print(f"using a {self.title}")

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        super().draw()
        print(f"using a {self.title}")

st = Stationery("stationery item")
st.draw()

print("-----------------------------------")

pen = Pen("pen")
pen.draw()

print("-----------------------------------")

pencil = Pencil("pencil")
pencil.draw()

print("-----------------------------------")

handle = Handle("handle")
handle.draw()



