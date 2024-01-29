confines_x = int(input("Введите границы по длинне: "))
confines_y = int(input("Введите границы по высоте: "))
print("Введите ряд и позицию для преземления Марсахода")
axis_y = int(input("Введите ряд: "))
axis_x = int(input("Введите позицию: "))
x_plan = "-"
rover = "X"
plan = ""
while axis_x > confines_x or axis_y > confines_y:
    print("Координаты больше радиуса действия!!! Введите новые")
    print("Радиус действия: x =",confines_x,"y =",confines_y)
    axis_y = int(input("Введите ряд: "))
    axis_x = int(input("Введите позицию: "))

print("Для движение Марсохода вводите данные команды: ")
print("A - движение влево\nD - движение вправо\nW -движение вверх\nS-движение вниз\nP - Отключение программы")
while True:
    key = input("Введите команду: ")
    if key == "a" or key == "A":
        if axis_x > 1:
            axis_x = axis_x - 1
        else:
            print("Марсоход выходит из зоны видимости. Введите иную команду")
            continue
    elif key == "d" or key == "D":
        if axis_x < confines_x:
            axis_x = axis_x + 1
        else:
            print("Марсоход выходит из зоны видимости. Введите иную команду")
            continue
    elif key == "w" or key == "W":
        if axis_y > 1:
            axis_y = axis_y - 1
        else:
            print("Марсоход выходит из зоны видимости. Введите иную команду")
            continue
    elif key == "s" or key == "S":
        if axis_y < confines_y:
            axis_y = axis_y + 1
        else:
            print("Марсоход выходит из зоны видимости. Введите иную команду")
            continue
    elif key == "p" or key == "P":
        print("Связь с марсоходом завершена.\nПрограмма отключена!")
        break

    for y in range(1,confines_y+1):
        if y == axis_y:
            for x in range(1,confines_x+1):
                if x == axis_x:
                    plan = plan + rover
                else:
                    plan = plan + x_plan
            plan = plan + "\n"
        else:
            plan = plan + (x_plan * confines_x) + "\n"
    print("=====================================")
    print(plan,"\n=====================================")
    print("axis x =", axis_x)
    print("axis_y =", axis_y)
    plan = ""



