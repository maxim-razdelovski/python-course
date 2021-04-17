# coding=UTF-8
"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 

В рамках класса реализовать два метода. 

Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». 
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 

Проверить работу полученной структуры на реальных данных.
"""

class Date:
    date_string = ""

    def __init__(self, date_string):
        Date.date_string = date_string
    
    @classmethod
    def convert_date(cls, date_string=None):
        if date_string:
            day, month, year = date_string.split("-")
            return int(day), int(month), int(year)
        else:
            day, month, year = cls.date_string.split("-")
            return int(day), int(month), int(year)
    
    @staticmethod
    def validate_date(date_string):
        day, month, year = Date.convert_date(date_string)

        validation_result = { "date": f"{day}/{month}/{year}", "isValidDate": True, "message": list() }
        months_31_days = [1, 3, 5, 7, 8, 10, 12]

        if day < 1:
            validation_result["isValidDate"] = False 
            validation_result["message"].append("day value is not valid!")

        if month == 2:
            if Date.is_leap_year(year):
                if day > 29:
                    validation_result["isValidDate"] = False 
                    validation_result["message"].append("day value is not valid! max days in a leap year in February are 29")
            else:
                if day > 28:
                    validation_result["isValidDate"] = False 
                    validation_result["message"].append("day value is not valid! max days in February are 28")
        elif month in months_31_days:
            if month > 31:
                validation_result["isValidDate"] = False 
                validation_result["message"].append("day value is not valid!")
        else:
            if month > 30:
                validation_result["isValidDate"] = False 
                validation_result["message"].append("day value is not valid!")
            
        if month > 12 or month < 1:
            validation_result["isValidDate"] = False 
            validation_result["message"].append("month value is not valid!")

        if validation_result["isValidDate"]:
            validation_result["message"].append("date is valid!")

        return validation_result

    @staticmethod
    def is_leap_year(year):
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False


dt = Date("11-02-2021")

# second usage mode, same result, but using an object of a class initialized via constructor:
day, month, year = dt.convert_date()

print(f"day: {day}")
print(f"month: {month}" )
print(f"year: {year}")

# second usage mode, same result, but this time we are using class access and a provided explicit param to the method:

day, month, year = Date.convert_date("11-02-2021")

print(f"day: {day}")
print(f"month: {month}" )
print(f"year: {year}")

validation_result = Date.validate_date("31-12-2021")
for message in validation_result.get("message"):
    print(f"date you provided ({validation_result.get('date')}) --> {message}")


validation_result = Date.validate_date("11-22-2021")
for message in validation_result.get("message"):
    print(f"date you provided ({validation_result.get('date')}) --> {message}")

validation_result = Date.validate_date("30-02-2020")
for message in validation_result.get("message"):
    print(f"date you provided ({validation_result.get('date')}) --> {message}")


print("\nmultiple invalid messages example:")
validation_result = Date.validate_date("00-13-2020")

for message in validation_result.get("message"):
    print(f"date you provided ({validation_result.get('date')}) --> {message}")