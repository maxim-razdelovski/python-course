"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: 
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

def set_persons_info(name, lastname, year_of_birth, city, email, phone):
    return { 'name': name, 'lastname': lastname, 'year_of_birth': year_of_birth, 'city': city, 'email': email, 'phone': phone }

def print_persons_info(info):
    formatted_data = (  
                        f'full personal data: {info.get("name")} {info.get("lastname")}, '
                        f'born {info.get("year_of_birth")}, lives in {info.get("city")}, ' 
                        f'email: {info.get("email")}, phone: {info.get("phone")}'
                    )

    print(formatted_data)


persons_info = set_persons_info(name='Jon', lastname='Doe', city='New York', email='joe_doe@somegmail.com', year_of_birth="1990",phone='7888999888')

print_persons_info(persons_info)