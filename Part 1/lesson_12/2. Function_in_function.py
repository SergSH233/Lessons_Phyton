def test():
    num = int(input("Введите целое число: "))
    if num > 0:
        positive()
        test()
    elif num < 0:
        negative()
        test()


def positive():
    print("Число положительное")


def negative():
    print("Число отрицательное")


test()
