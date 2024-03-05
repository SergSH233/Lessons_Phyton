# Цель: Написать программу которая будет вести базу клиентов и выводить при запросе данные о них и их заказах за все
#       время.
# 1. Создать базу с наименованием имеющихся в наличии товаров.
# 2. Создать переменную с вводом номера телефона клиента, и при отсутствии данного дабовлять его в базу.
#    - создать переменную с именем.
# 3. Сделать список с выбором всех имеющихся товаров.
# 4. Создать метод для занесения заказа в базу и подсчета имеющихся.
# 5. Сделать вывод имеющихся в базе элементов:
#    - Сумма заказов по имени, Сумма по имени конкретных видов, Сумма всех товаров, Сумма всех конкретных товаров.
client_base = {
    "447247892": {"Шведов Сергей Андреевич": [{"Мексиканская": 1, "4 Сезона": 1}]}}

goods_base = [["Мексиканская", 15],
              ["4 Сезона", 25],
              ["Барбекю", 20],
              ["Студенческая", 10],
              ["Гавайская", 30,],
              ["По Нью-йоркски", 53]]


def client_order(goods_base, client_base):
    goods_base = goods_base
    client_base = client_base
    for x in range(len(goods_base)):
        print("Номер заказа:", (x + 1), ":", goods_base[x][0], "-", goods_base[x][1], "рублей")
    order = []
    while True:
        while True:
            print("Выберите номер заказа!")
            key = input("Введите номер заказа: ")
            if key.isdigit():
                if int(key) > (len(goods_base)):
                    print("Введите номер заказа из списка!")
                    continue
                else:
                    break
            else:
                print("Просьба заказ ввести цифрой из списка!")
                print()
                continue
        order.append(goods_base[(int(key) - 1)])
        for x in range(len(order)):
            print("Ваш заказ", (x + 1), ":", order[x][0], "-", order[x][1], "рублей")
        print("Хотите добавить еще в ваш заказ?\n1.Да\n2.Нет")
        num = input("Введите команду: ")
        if num == "1":
            continue
        elif num == "2":
            break
        else:
            print("Введите команду из списка!")
    coast = 0
    for x in range(len(order)):
        coast = coast + order[x][1]
        print("Ваш заказ", (x + 1), ":", order[x][0], "-", order[x][1], "рублей")
        # Нужно записать данные о заказе в словарь клиента
    print("Итог:", coast, "руб")



def mainMenu(goods_base, client_base):
    goods_base = goods_base
    client_base = client_base
    print("Добро пожаловать в cafe 'Pizza Time'\nВведите ваш номер телефона для накопления и получения бонусов!")
    while True:
        phone_number = input("Введите номер: ")
        if len(phone_number) < 9 or not phone_number.isdigit():  # Добавить проверку на правильность кода! (см прим. 5 Files)
            print("Неверно указан номер! Пожалуйста проверте правильно ли он введен! (xx)xxx-xx-xx")
            continue
        else:
            break
    if client_base.get(phone_number) == None:
        print("Debug! Name",client_base.get(phone_number))
        print("Вы у нас впервые!? Представтесь пожалуйста что бы мы знали как к вам обращатся!")
        while True:
            name = input("Введите вашу Фамилию и Имя: ")
            if len(name) < 5:  # Доработать при возможности
                print("Введите корректное имя!!!")
                continue
            else:
                client_base[phone_number] = {name:[]}
                break
    for x in client_base[phone_number].keys():
        client = x
    print("Мы рады видеть вас",client)
    client_order(goods_base,client_base)




mainMenu(goods_base, client_base)
# for x in range(len(goods_base)):
#     print("Номер заказа:", (x + 1), ":", goods_base[x][0], "-", goods_base[x][1], "рублей")
# order = []
# while True:
#     while True:
#         print("Выберите номер заказа!")
#         key = input("Введите номер заказа: ")
#         if key.isdigit():
#             if int(key) > (len(goods_base)):
#                 print("Введите номер заказа из списка!")
#                 continue
#             else:
#                 break
#         else:
#             print("Просьба заказ ввести цифрой из списка!")
#             print()
#             continue
#     order.append(goods_base[(int(key) - 1)])
#     for x in range(len(order)):
#         print("Ваш заказ", (x + 1), ":", order[x][0], "-", order[x][1], "рублей")
#     print("Хотите добавить еще в ваш заказ?\n1.Да\n2.Нет")
#     num = input("Введите команду: ")
#     if num == "1":
#         continue
#     elif num == "2":
#         break
#     else:
#         print("Введите команду из списка!")
# coast = 0
# for x in range(len(order)):
#     coast = coast + order[x][1]
#     print("Ваш заказ", (x + 1), ":", order[x][0], "-", order[x][1], "рублей")
# print("Итог:",coast,"руб")
# print(order)

