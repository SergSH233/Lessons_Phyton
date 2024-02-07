def NOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a %= b          # a = a % b - Пример работы кода
        else:
            b %= a
    return a + b


a = int(input("Введите число а: "))
b = int(input("Введите число в: "))
print("Наибольший общий делитель двух чисел = ", NOD(a, b))
