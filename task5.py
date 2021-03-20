income = int(input("input your company's income in $: "))
costs = int(input("input your company's costs in $: "))

profitability = 0
total_profit = income - costs

if total_profit > 0:
    print("your company is profitable")
    profitability = (income - costs) / income * 100
    print(f"profitability is {profitability:.2f}%")

    employees_count = int(input("input your company's employees count: "))
    profitability_per_employee = total_profit / employees_count
    print(f"your company's profit per employees equals {profitability_per_employee:.2f}$")

elif total_profit == 0:
    print("your company broke even")
else:
    print("your company is unprofitable")





