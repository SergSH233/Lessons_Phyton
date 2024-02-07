def UpCalculator():
    print("Выберите необходимую функцию из списка\n1 - Сумма (+)\n2 - Разность (-)\n3 - Умножение (*)\n"
          "4 - Деление (/)\n5 - Минимальное число (min)\n6 - Максимальное число (max)\n0 - Выход ")
    key = input("Введите номер команды: ")
    if key == "1":
        Sum_n()
        UpCalculator()
    elif key == "2":
        Difference()
        UpCalculator()
    elif key == "3":
        Multiplication()
        UpCalculator()
    elif key == "4":
        Division()
        UpCalculator()
    elif key == "5":
        MinNumRow()
        UpCalculator()
    elif key == "6":
        MaxNumRow()
        UpCalculator()
    elif key == "0":
        print("Завершение работы!")
    else:
        print("Ошибка! Неверная команда")
        UpCalculator()

def Sum_n():
    a = int(input("Введите первое слагаемое: "))
    b = int(input("Введите второе слогаемое: "))
    result = a + b
    print("Сумма",a,"и",b,"=",result)
    print()

def Difference():
    a = int(input("Введите первое слагаемое: "))
    b = int(input("Введите второе слогаемое: "))
    result = a - b
    print("Разность",a,"и",b,"=",result)
    print()

def Multiplication():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    result = a * b
    print("Умножение",a,"и",b,"=",result)
    print()

def Division():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    result = a / b
    print("Деление",a,"и",b,"=",result)
    print()

def MinNumRow():
    nums = int(input("Введите количество чисел в искомом ряду: "))
    result = 0
    for x in range(nums):
        y = int(input("Введите число для проверки: "))
        if y <= result:
            result = y
    print("Минимальное число в ряду =",result)
    print()

def MaxNumRow():
    nums = int(input("Введите количество чисел в искомом ряду: "))
    result = 0
    for x in range(nums):
        y = int(input("Введите число для проверки: "))
        if y >= result:
            result = y
    print("Минимальное число в ряду =",result)
    print()

UpCalculator()



