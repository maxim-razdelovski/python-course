# coding=UTF-8
"""
Начните работу над проектом «Склад оргтехники». 
Создайте класс, описывающий склад.

А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 

В базовом классе определите параметры, общие для приведённых типов. 

В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием. 
Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании. 
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру (например, словарь).

Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров, 
отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

"""

import itertools

DEVICE_TYPES = { "SCANNER": "scanner", "PRINTER": "printer", "COPIER": "copier" }
OFFICES = { "HRM":"HRM", "MARKETING":"MARKETING", "PR":"PR", "UNASSIGNED":"unassigned" }

def office_code_to_office_name(code):
    if code == 1:
        return OFFICES["HRM"]
    elif code == 2:
        return OFFICES["MARKETING"]
    elif code == 3:
        return OFFICES["PR"]
    else:
        return OFFICES["UNASSIGNED"]

class Warehouse:
    def __init__(self):
        self.devices = { "total_devices": 0, "shelf": []}

    def list_stored_devices(self):
        print(self)
    
    def assign_device_to_office(self, device, office_id):
        device.office_id = office_id

    def accept_item(self, item):
        self.devices["shelf"].append(item)
        self.devices["total_devices"] += 1

    def __str__(self):
        ret_val = f"warehouse is storing { self.devices['total_devices']} devices:\n"
        for device in self.devices['shelf']:
            ret_val += str(device) + "\n"
        return ret_val

class Device:
    class item_id:
        newid = itertools.count().__next__
        def __init__(self):
            self.id = item_id.newid()

    @staticmethod
    def validate_quantity(value):
        try:
            return int(value)
        except:
            print("only numbers are allowed for setting quantity")
            return None

    def __init__(self, office_id=OFFICES['UNASSIGNED']):
        print("creating device")
        self.id = Device.item_id.newid()
        self.office_id = office_id

    def store_device(self, warehouse):
        warehouse.accept_item(self)

    def get_device_type(self):
        return self.device_type

    def __str__(self):
        return f"Device ID: {self.id} | TYPE: {self.device_type} | MODEL: {self.model} | OFFICE: {self.office_id } |"

class Printer(Device):
    def __init__(self, model):
        super().__init__()
        self.device_type = "Printer"
        self.model = model

    def print(self):
        print(f"device id-{ self.id } is printing a page")

class Scanner(Device):
    def __init__(self, model):
        super().__init__()
        self.device_type = "Scanner"
        self.model = model

    def scan(self):
        print("scanning a page")
    
class Copier(Device):
    def __init__(self, model):
        super().__init__()
        self.device_type = "Copier"
        self.model = model

    def copy(self):
        print("copying a page")

wh = Warehouse()

printer1 = Printer("canon L800")
printer1.print()
printer2 = Printer("epson R80")
printer2.print()

print("\nDEVICE info:")
print(printer1)
print("\nDEVICE info:")
print(printer2)


scanner1 = Scanner("canon X333")
print("\nDEVICE info:")
print(scanner1)

xerox1 = Copier("Xerox X77")
print("\nDEVICE info:")
print(xerox1)

wh.assign_device_to_office(printer1, OFFICES["HRM"])
wh.assign_device_to_office(printer2, OFFICES["MARKETING"])
wh.assign_device_to_office(scanner1, OFFICES["PR"])
wh.assign_device_to_office(xerox1, OFFICES["MARKETING"])

printer1.store_device(wh)
printer2.store_device(wh)
scanner1.store_device(wh)
xerox1.store_device(wh)

print("\nWAREHOUSE STOCKS info:")
wh.list_stored_devices()

print("\ninput devices to be added to the Warehouse")

user_defined_devices = []

while True:
    yesno = input("do you want to create office devices? YES(Y) to continue, NO(N) to exit? > ")
    if yesno.lower() == "no" or yesno.lower() == "n":
        break
    device_type = input("device type (1 - SCANNER) (2 - PRINTER) (3 - COPIER) > ")
    model = input("name > ")
    office = input("office (1 - HRM) (2 - MARKETING) (3 - PR), (Enter - unassigned) > ")

    quantity = None
    while not quantity:
        quantity = Device.validate_quantity(input("quantity > "))
        if quantity:
            for i in range(1, quantity):
                if device_type == '1':
                    device = Scanner(model)                    
                elif device_type == '2':                    
                    device = Printer(model)
                else:
                    device = Copier(model)

                wh.assign_device_to_office(device, office_code_to_office_name(office))
                user_defined_devices.append(device)


for device in user_defined_devices:
    device.store_device(wh)

print("\nWAREHOUSE STOCKS info:")
wh.list_stored_devices()