"""
Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и dict. 
"""

month_number = int(input("input month number: "))

months_catalogue_list = [
                            ["January", "winter"],
                            ["February", "winter"], 
                            ["March", "spring"], ["April", "spring"], ["May", "spring"], 
                            ["June", "summer"], ["July", "summer"], ["August", "summer"],
                            ["September", "fall"], ["October", "fall"],[ "November", "fall"],
                            ["December", "winter"]
                        ]

months_catalogue_dict = {
                            1: {"month":"January", "season": "winter"}, 
                            2: {"month":"February", "season": "winter"}, 
                            3: {"month": "March", "season":"spring"},
                            4: {"month": "April", "season":"spring"},
                            5: {"month": "May", "season":"spring"},
                            6: {"month": "June", "season":"summer"},                            
                            7: {"month": "July", "season":"summer"},
                            8: {"month": "August", "season":"summer"},
                            9: {"month": "September", "season":"fall"},
                            10: {"month": "October", "season":"fall"},
                            11: {"month": "November", "season":"fall"},
                            12: {"month": "December", "season":"winter"}
                        }


user_month = months_catalogue_list[month_number - 1]

print("we found this out using List:\n")
print(f"- your month is {user_month[0]} and it is in {user_month[1]}")

print("\n\n")

user_month = months_catalogue_dict.get(month_number)

print("we found this out using Dictionary:\n")
print(f"- your month is {user_month.get('month')} and it is in {user_month.get('season')}")