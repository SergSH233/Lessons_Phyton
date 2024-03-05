# Цель: Создать программу которая будет из мебя состовлять словарь синонимов.
#       Структура программы должна состоять из главного меню в котором будет:
#       1) Проверка слова на наличие синонимов
#       2) Добавление пары синонимов
#       3) Выход
# 1. Написать программу методами в котором основным будет главное меню.
# 2. Написать метод для проверки слова
# 3. Написать метод для добавления слова в словарь.

def mainMenu(data_base):
    print("Словарь Синонимов!\nВыберите команду:\n1.Проверка слова на наличие синонимов.\n"
          "2.Добавление новой пары слов\n"
          "3.Показать весь словарь\n"
          "0.Выход из программы")
    data_base = data_base
    while True:
        key = input("Введите команду: ")
        if key == "1":
            synonym_check(data_base)
            print()
            mainMenu(data_base)
        elif key == "2":
            word = input("Введите первое слово для добавления в словарь: ").lower()
            synonyms_set_base(data_base,word)
            print()
            mainMenu(data_base)
        elif key == "3":
            for x in data_base:
                print(x, "-", data_base[x])
            print()
            mainMenu(data_base)
        elif key == "0":
            print("Программа завершена!")
            break

        else:
            print("Неверная команда!")


def synonym_check(deck_base):
    word = input("Введите слово для проверки: ").lower()
    flag = True
    deck_base = deck_base
    for x in deck_base:
        if word == x:
            print("Синоним слова", word, "-", deck_base[x])
            flag = False
            break
        elif word == deck_base[x]:
            print("Синоним слова", word, "-", x)
            flag = False
            break
    if flag:
        print("Слова", word, "нет в данном списке\nХотите добавить это слово и его синоним в словарь?\n1.Да\n2.Нет")
        while True:
            key = input("Введите команду из списка: ")
            if key == "1":
                synonyms_set_base(deck_base,word)
                break
            elif key == "2":
                break
            else:
                print("Неверная команда!")


def synonyms_set_base(deck_base, word):
    print("Первое слово: ", word)
    word2 = input("Введите слова синоним к слову: ").lower()
    flag = False
    for x in deck_base:
        if word == x or word2 == x or word == deck_base[x] or word == deck_base[x]:
            flag = True
    if flag:
        print("Одно из слов уже есть в списке!\nПара не будет сохранена!")
    else:
        deck_base[word] = word2
        print("Пара синонимов сохранена")


data_syn_base = {
    "вагон": "контейнер",
    "привет": "здравствуй",
    "весело": "радостно",
    "солнце": "светило",
    "дорога": "путь"
}

mainMenu(data_syn_base)
