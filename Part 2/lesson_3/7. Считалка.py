# Цель: Программа должна подсчитать сколько слов в считалке и удалять элементы из списка в зависимости на ком
#       считалка завершилась.
# 1. Создать список участников, методом ввода элеменов пользователем.
# 2. Создать массив состоящий из слов в считалке.
# 3. Вывести кол-во слов в переменную.
# 4. Создать переменную для подсчета на ком остановилась считалка.
# 5. Создать метод для удаления элементов из списка.
# 6. Вывести оставшихся игроков.

def NewList_Str():
    print("Введите имена участников! Для завершения ввода введите команду end")
    new_list = []
    while True:
        print("Для завершения заполнения списка введите команду end")
        name = input("Введите имя участника: ")
        if name == "end":
            break
        else:
            new_list.append(name)
    return new_list

players = NewList_Str()
print("Участники: ",players)
counting = int(input("Введите кол-во слов в считалке: "))
calc = 0
indPl = 0
while len(players) > 1:
    calc = calc + indPl
    indPl = (calc + counting - 1) % len(players)
    print("Выбывает:",players[indPl])
    players.remove(players[indPl])
    calc = 0
print("Последним остался: ",players)
