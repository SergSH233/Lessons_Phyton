import random
def MainMenu():
    print("Выберите игру:\n1 - Камень, ножницы, бумага\n2 - Откадай мое число\n0 - Выход")
    key = int(input("Введите команду: ")) #rock Paper Scissors
    if key == 1:
        RockPaperScissors()
        MainMenu()
    elif key == 2:
        GuessTheNumber()
        MainMenu()
    elif key == 0:
        print("Завершение работы программы")

def GuessTheNumber():
    print("Введите границы отгадываемого числа! Пример: от 1 до 100")
    min = int(input("От: "))
    max = int(input("До: "))
    while min > max:
        print("!!!Граница минимум больше максимальной!!! Введите иные значения!")
        min = int(input("От: "))
        max = int(input("До: "))

    n = (min + max)//2
    print("|n = |", n)
    while True:
        print("Вы загадали: ", n,"?")
        print("Для ответа введите:\n1 - Мое число больше\n2 - Мое число меньше\n3 - Это мое число")
        key = int(input("Введите команду: "))
        if key == 1:
            min = n
            n = (min + max)//2
        elif key == 2:
            max = n
            n = (min + max)//2
        elif key == 3:
            print("Загаданное число =", n)
            break
        else:
            print("Неверная команда!")

def RockPaperScissors():
    print("Введите команду:\n1 - Камень\n2 - Ножницы\n3 - Бумага")
    while True:
        key = int(input("Введите команду: "))
        key_ai = random.randrange(1,3)
        key_ai_st = ["Камень","Ножницы","Бумагу"]
        print(key_ai_st[1])
        if key == 1:
            if key_ai == 1:
                print("Ничья! Ваш соперник тоже выбрал " + key_ai_st[key_ai - 1] + "\nПереигровка!")
            elif key_ai == 2:
                print("Вы победили! Соперник выбросил " + key_ai_st[key_ai - 1])
                break
            elif key_ai == 3:
                print("Вы Проиграли! Соперник выбросил " + key_ai_st[key_ai - 1])
                break
        elif key == 2:
            if key_ai == 2:
                print("Ничья! Ваш соперник тоже выбрал " + key_ai_st[key_ai - 1] + "\nПереигровка!")
                continue
            elif key_ai == 3:
                print("Вы победили! Соперник выбросил " + key_ai_st[key_ai - 1])
                break
            elif key_ai == 1:
                print("Вы Проиграли! Соперник выбросил " + key_ai_st[key_ai - 1])
                break
        elif key == 3:
            if key_ai == 3:
                print("Ничья! Ваш соперник тоже выбрал " + key_ai_st[key_ai - 1] + "\nПереигровка!")
                continue
            elif key_ai == 1:
                print("ВЫ ПОБЕДИЛИ! Соперник выбросил " + key_ai_st[key_ai - 1])
                break
            elif key_ai == 2:
                print("Вы Проиграли! Соперник выбросил " + key_ai_st[key_ai - 1])
                break
        else:
            print("Неверная команда!!!")

MainMenu()
