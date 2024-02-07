# Функция для подсчета запрашиваемых цифр и букв в тексе
def count_letters():
    total_letter = 0
    total_numbers = 0
    text = input("Введите текст:\n").lower()
    letter = input("Введите букву для поиска в тексте: ").lower()
    while True:
        if "0" <= letter <= "9":
            print("Ошибка! Неверны ввод! Ввод от А(a) до Z(я)")
            letter = input("Введите букву для поиска: ")
        else:
            break

    num = int(input("Введите цифру для поиска: "))
    while True:
        if 0 <= num <= 9:
            break
        else:
            print("Ошибка! Неверны ввод! Ввод от 0 до 9")
            num = int(input("Введите цифру для поиска: "))
    num = str(num)
    #print("|отладка нум|",num)
    for x in text:
        if x == letter:
            total_letter += 1
        elif x == num:
            total_numbers += 1
    print("Количество цифр",num,"=",total_numbers,"\nКоличество букв",letter.upper(),"=",total_letter)

count_letters()


