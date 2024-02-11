# Цель: Создать многомерный массив для учета товаров где [[0] - наименование товара [1] - цена товара]
# 1. Создать таблицу, с помощью цикла вввода где у пользавателя спрашивают название товара и его цену
#   - Доп. Создать проверку по наименованию товара дабы исключить идентичные элементы
# 2. С помощью цикла создать поиск по наименованию товара для получения хранящейся ячейки
# 3. Создать переменную количество тавара для подсчета.
# 4. Создать переменную check для суммы пакупок
# 5. Вывод чека(Наименование товара, количество, сумма, итог.


# Заполнение списка и проверка на наличие уникальности ввода

# shop_list = []
# for _ in range(int(input("Введите длинну списка товаров: "))):
#     a = input("Введите название товара: ").lower()
#     for i in range(len(shop_list)):
#         for j in range(len(shop_list[i])):
#             while shop_list[i][j] == a:
#                 print("Этот товар уже есть в списке! Введите иной")
#                 a = input("Введите название товара: ").lower()
#     b = int(input("Введите цену товара: "))
#     shop_list.append([a,b])
shop_list = [["картофель", 2], ["шоколад", 8], ["капуста", 3], ["морковь", 1], ["курица", 10], ["напиток", 4],
             ["чипсы", 6], ["масло", 9], ]

shop_total = 0
while True:
    print("Выберите команду:\n1 - Новый клиент\n2 - Сумма всех продаж за день\n0 - Выход")
    key = input("Ввод: ")
    if key == "1":
        new_client = []
        total_sum = 0
        while True:
            product = input("Введите наименование товара: ").lower()
            for i in range(len(shop_list)):
                for j in range(len(shop_list[i])):
                    if shop_list[i][j] == product:
                        product_name = shop_list[i][j]
                        price = int(shop_list[i][j + 1])
                        quantity = int(input("Введите кол-во товаров: "))
                        sum_price = quantity * price
                        new_client.append([product_name, quantity, sum_price])
                        total_sum = total_sum + sum_price
                        print("Добавлено:\n",
                              product_name, "x", quantity, "=", sum_price)
            print("Добавить еще товар в корзину?\n1 - Да\n2 - Нет")
            key = input("Ввод: ")
            while key != "1" and key != "2":
                key = input("Команда неверна! Ввод: ")
            if key == "1":
                continue
            elif key == "2":
                calc = 1

                for x in range(len(new_client)):
                    print(calc, new_client[x][0], "x", new_client[x][1],"\t", "сумма:", new_client[x][2])
                    calc += 1
                print("Итог:", total_sum,"руб")
                shop_total = shop_total + total_sum
                calc = 0
                break
    elif key == "2":
        print("Сумма всех продаж составляет:", shop_total, "руб")
    elif key == "0":
        print("Программа завершена")
        break
    else:
        print("Введенная команда неверная!")

