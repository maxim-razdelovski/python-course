"""
Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).

Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. 
Выполнить подсчёт средней величины дохода сотрудников.

Пример файла:
Иванов 23543.12
Петров 13749.32
"""

def parse_pay(str, line_number):
    try:    
        return float(str.split()[1])
    except:    
        raise Exception(f"failed to parse line #{line_number} - check file format and try again")

def analyze_pay(filename):
    # file_obj = open("task3-text.txt", "r")
    print(f"\nreading file '{filename}'\n\n")
    file_obj = open(filename, "r")

    count_employees = 0
    count_pay = 0
    underpayed_employees = []
    underpayment_mark = 20000.00

    try:
        for line in file_obj:
            count_employees += 1
            employees_pay = parse_pay(line, count_employees)
            count_pay += employees_pay

            if(employees_pay < underpayment_mark):
                underpayed_employees.append(line)

        if (len(underpayed_employees) > 0):
            print(f"employees having pay less than 20.000,00 roubles:\n")
            for employee_data in underpayed_employees:
                print(employee_data)

        print("--------------------------")
        print(f"average pay: {count_pay / count_employees:.2f} roubles")
    except Exception as exc:
        print(f"an error occurred running the program: \n {exc}")
    finally:
        file_obj.close

# run program with a file with supported format:
analyze_pay("task3-text.txt")

# try run a file containing some poorly formatted text:
analyze_pay("task3-text-bad.txt")