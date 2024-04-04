# Цель:
# Реализуйте программу — чат, в котором могут участвовать сразу несколько человек,
# то есть программу, которая может работать одновременно для нескольких пользователей.
# При запуске запрашивается имя пользователя. После этого он выбирает одно из действий:
#   1.Посмотреть текущий текст чата.
#   2.Отправить сообщение (затем вводит сообщение).
#   - Действия запрашиваются бесконечно.
import os()


def main_menu(name):
    name = name
    print("Выберите одну из команд:\n1. Посмотреть сообщения\n2. Написать сообщение")
    key = input("Введите команду: ")
    if key == "1":
        read_message()
        main_menu(name)
    elif key == "2":
        write_message(name)
        main_menu(name)
    else:
        print("Неверная команда!")
        main_menu(name)


def read_message():
    try:
        with open("chat.txt", 'r') as chat:
            if not os.path.exists("chat.txt"):
                raise FileNotFoundError("Файл не найден")
            for i_message in chat:
                print(i_message,end="")
    except FileNotFoundError:
        print("Сообщений нет! Файл не найден!")


def write_message(name):
    try:
        with open("chat.txt", 'a') as chat:
            massage = input("Введите сообщение: ")
            chat.write("{name}: {massage}\n".format(name=name,massage=massage))
    finally:
        print("Сообщение добавлено!")


name = input("Введите ваше имя: ")
main_menu(name)