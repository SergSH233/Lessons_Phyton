# Цель: Написать программу, которая рассчитывает общую стоимость позиций для каждого товара на складе
#       и выводит эту информацию на экран.
# 1. Взять два имеющихся списка из задания
# 2. Создать две переменные для подсчета количества товаров и их общей стоимости.
# 3. Создать цикл для поиска товаров по значению первого списка с внутренним подсчетам и выводом информации в кансоль.

# Первый список из задания
goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Второй список из задания
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Переменные для подсчета
sum_goods = 0
count = 0

# Цикл поиска
for y in goods.keys():  # Проходим по ключам списка
    for x in store[goods[y]]:  # Берем значения из списка
        tot = 0  # Переменная для подсчета товаров
        count = count + x["quantity"]  # Подсчет товара в каждой позиции товара
        tot = tot + (x["quantity"] * x["price"])  # Подсчет общей стоимости на каждом складе
        sum_goods = sum_goods + tot  # Подсчет общей стоимости всей продукции
    print(y, "- Количество:", count, "Сумма:", sum_goods)
    count = 0   # Обнуление счетчика
