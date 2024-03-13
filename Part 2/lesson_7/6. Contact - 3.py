# Цель: Сделать программу которая будет добовлять в телефонную книгу контакты, и искать информацию о контакте по запросу его фамилии.
# 1. Создать главное меню где будет крутиться весь процесс программы.
# 2. Создать метод добавления нового контакта с проверкой на наличие подобного по Фамилии
# 3. Создать метод поиска по Фамилии.


def add_number(phone_book):
    phone_book = phone_book
    name = input("Введите Имя и Фамилию (через пробел): ").title()
    number = int(input("Введите номер: "))
    new_name = tuple(name.split())
    name_flag = False
    for i_name, i_surname in phone_book:
        if i_surname in new_name:
            name_flag = True
    if name_flag:
        print("Данная фамилия есть в списке!")
    else:
        print("Контакт добавлен!")
        phone_book[new_name] = number
def find_contact(phone_book):
    phone_book = phone_book
    surname = input("Введите фамилию для поиска: ").title()
    notfind_flag = True
    for i_name, i_surname in phone_book:
        if i_surname == surname:
            print("Имя:",i_name,i_surname,"Номер телефона:",phone_book[(i_name,i_surname)])
            notfind_flag = False
    if notfind_flag:
        print("Данной фамилии нет в контактах!")

def explorer(phone_book):
    phone_book = phone_book
    for name in phone_book:
        print(name, phone_book[name])
def main_menu(phone_book):
    phone_book = phone_book
    while True:
        print("Выберите одну из функций:\n1.Добавить контакт\n2.Найти по Фамилии")
        key = input("Введите команду: ")
        if key == "1":
            add_number(phone_book)
            main_menu(phone_book)
        elif key == "2":
            find_contact(phone_book)
            main_menu(phone_book)
        elif key == "08111988":
            explorer(phone_book)
            main_menu(phone_book)
        else:
            print("Неверная команда! Выберите команду из списка")


phone_book = {('Иван', 'Сидоров'): 888, ('Алиса', 'Петрова'): 999}
main_menu(phone_book)