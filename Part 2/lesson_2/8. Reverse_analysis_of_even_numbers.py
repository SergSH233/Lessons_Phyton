# Цель:
# 1. Создать список целочисленных элементов(Лабораторных исследований)
# 2. Сделать сортировку по убыванию (max - min)
# 3. Убрать из списка числа не кратные 2-ум

def sort_max_to_min(list):
    for _ in range(len(list) - 1):
        for i in range(len(list) -1):
            if list[i] < list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]

lab_list = []
lab_list_size = int(input("Введите размер списка данных: "))
for _ in range(lab_list_size):
    num = int(input("Введите данные в список: "))
    lab_list.append(num)
for x in lab_list:
    if x % 2 != 0:
        lab_list.remove(x)
sort_max_to_min(lab_list)
print("Данные иследования =",lab_list)