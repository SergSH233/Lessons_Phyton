print("Программа Дишефратор.\nВыбирите необходимую функцию из предлагаемого списка:")
word_list = []
while True:
    print("Команды для ввода:\n1 - Зашивровать слово\n2 - Дешивровать слово\n0 - Выход из программы")
    key = (input("Введите номер команды: "))
    # Шифрование слова
    if key == "1":
        word = input("Введите слова для шифрования: ")
        print(len(word))
        new_word = ""
        min = 0
        max = (len(word) - 1)
        calc = len(word)
        while calc > 0:
            new_word = new_word + word[min]
            min = min + 1
            calc = calc - 1
            if max != (min -1):
                new_word = new_word + word[max]
                max = max - 1
                calc = calc - 1
        new_word = new_word.lower()
        print(new_word)
        while True:
            print("Сохранить ваше слова в список шифрованных слов?\nY(Д) - да, N(Н) - нет")
            key = input("Ввод: ")
            if key == "Y" or key == "y" or key == "Д" or key == "д":
                word_list.append(new_word)
                print("шифр сохранен")
                break
            elif key == "N" or key == "n" or key == "Н" or key == "н":
                print("Ваш шифр:", new_word,"не был сохранен")
                break
            else:
                print("Неверный символ!")
    elif key == "2":
        word = ""
    #Расшифровка слова
        while True:
            print("1 - Взять слово из имеющегося списка слов\n2 - Ввести новое слово")
            key = input("Ввод: ")
            if key == "1":
                calc_1 = 1
                print("list = ",len(word_list))
                if len(word_list) > 0:
                    for x in word_list:
                        print(calc_1," - ",x)
                        calc_1 += 1
                    num = int(input("Введите номер слова для расшифровки: "))
                    num = num - 1
                    word = word_list[num]
                    break
                else:
                    print("!!!!Список пуст!!!!!\n==========")
                    word = input("Введите новое слово для расшифровки:")
                    break
            else:
                word = input("Введите слова для расшифровки: ")
                break
        #Процесс расшифроки
        word = word.lower()
        new_word = ""
        word_1 = ""
        word_2 = ""
        calc = 1
        for x in word:
            if calc%2 == 0:
                word_2 = x + word_2
                calc += 1
            else:
                word_1 = word_1 + x
                calc += 1
            new_word = word_1 + word_2
        print("Расшифрованное слово: ", new_word)
    elif key == "0":
        print("При выходе из программы все данные будут удалены\nВы уверены что хотите выйти из программы?\nY(Д) - да, N(Н) - нет")
        key = input("Ввод: ")
        if key == "Y" or key == "y" or key == "Д" or key == "д":
            print("Программа отключена")
            break
        elif key == "N" or key == "n" or key == "Н" or key == "н":
            continue
    else:
        print("Неверная команда! Вводить можно лишь то что указано!")
