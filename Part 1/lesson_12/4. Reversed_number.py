def RevercedNumber():
    revers = ""
    nums = int(input("Введите кол-во чисел в последовательности (ряду): "))
    for x in range(nums):
        num = input("Введите число для разворота: ")
        for y in num:
            revers = y + revers
            # print("|отладка|","num =",num, "revers=",revers)
        if revers[0] == "0":
            print("Ваше перевернутое число содержит 0 в начале.\nХотите ли вы его убрать?\nНажмите: Y - Да/Любая другая кнопка - Нет")
            key = input("Ввод: ")
            if key == "y" or key == "Y"or key == "Н" or key == "н":
                new_revers = ""
                point_1 = 0
                point_2 = 0
                for z in revers:
                    if z == "0" and (point_1 - point_2) == 0:
                        # print("|отладка x|", point_1 - point_2)
                        # print("|отладка x1|", point_1)
                        # print("|отладка x2|", point_2)
                        new_revers = new_revers
                        point_1 += 1
                        point_2 += 1
                    else:
                        # print("|отладка y|", point_1 - point_2)
                        # print("|отладка y1|", point_1)
                        new_revers = new_revers + z
                        point_1 += 1
                revers = new_revers
                print("Перевернутое число = ",revers)
                revers = ""
                point_1 = 0
                point_2 = 0
            else:
                print("Перевернутое число = ", revers)
                revers = ""
RevercedNumber()