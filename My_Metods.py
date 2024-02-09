# Создание простых списков:
# Создание строчного списка:
def NewList_Str(size):
    print("Введите",size,"элементов")
    list = []
    for _ in range(size):
        elem = input("Введите новый строчный элемент списка: ")
        list.append(elem)
    return list
# Создание целочисленного списка
def NewList_Int(size):
    print("Введите", size, "элементов")
    list = []
    for _ in range(size):
        elem = int(input("Введите новый целочисленный элемент списка: "))
        list.append(elem)
    return list

# Числовая сортировка
# От минимального к максимальному
def sort_min_to_max(list):
    for _ in range(len(list) - 1):
        for i in range(len(list) -1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]

# От максимального к минимальному
def sort_max_to_min(list):
    for _ in range(len(list) - 1):
        for i in range(len(list) -1):
            if list[i] < list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]

# Сортировка 2-х спиков по их уникальности
def UniqueCombinatonSortList(list_1, list_2):
    list_1.extend(list_2)
    list_1.sort()
    duble = []
    for x in range(len(list_1) - 1):
        elem_1 = list_1[x]
        elem_2 = list_1[x + 1]
        if elem_1 == elem_2:
            duble.append(elem_2)
    for x in range(len(duble)):
        list_1.remove(duble[x])
    return list_1