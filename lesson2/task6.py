"""
Реализовать структуру данных «Товары». 

Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. 
В кортеже должно быть два элемента — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения). 
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}), 
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Необходимо собрать аналитику о товарах. 
Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, 
например список названий товаров.

Пример:

{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”]
}
"""

goods_list = []

while True:
    name = input("name > ")
    price = float(input("price > "))
    quantity = int(input("quantity > "))
    unit = input("unit > ")

    goods_list.append((len(goods_list), {"name": name, "price": price, "quantity": quantity, "unit": unit}))

    go_on = input("do you want to continue? (yes/no) > ")
    if go_on == 'no':
        break

print(goods_list)

goods_attributes = dict.fromkeys(goods_list[0][1].keys(), [])
    
for idx, key in enumerate(goods_attributes.keys()):
    for item in goods_list:
        values = goods_attributes[key].copy()
        values.append(item[1].get(key))
        goods_attributes[key] = values if key != 'unit' else list(set(values))

print(goods_attributes)