# Цель: Программа должна подсчитать сколько слов в считалке и удалять элементы из списка в зависимости на ком
#       считалка завершилась.
# 1. Создать список участников, методом ввода элеменов пользователем.
# 2. Создать массив состоящий из слов в считалке.
# 3. Вывести кол-во слов в переменную.
# 4. Создать переменную для подсчета на ком остановилась считалка.
# 5. Создать метод для удаления элементов из списка.
# 6. Вывести оставшихся игроков.

def NewList_Str(size):
    print("Введите имена",size,"участников")
    list = []
    for _ in range(size):
        elem = input("Введите новые имя: ")
        list.append(elem)
    return list


# size = int(input("Введите количество участников: "))
# players = NewList_Str(size)
# players = ["Леня","Фима","Варя","Вася","Кирилл"]
players = ["1", "2", "3", "4", "5"]
counting = int(input("Введите кол-во слов в считалке: "))
calc = 0
while len(players) > 1:
    print("Debug Calc",calc)
    indPl = (calc + counting) % len(players)
    print("DeBug index",indPl)
    print("Выбывает:",players[indPl])
    players.remove(players[indPl])
    calc = calc + indPl
print("Последним остался: ",players)
