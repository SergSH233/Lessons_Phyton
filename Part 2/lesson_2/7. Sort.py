# !!!Важный модуль который можно использовать в последующих заданиях
# Цель написать Фунуцию сортировки списка от меньшего к большему
# Создать список чисел методом ввода пользвателя:
#   - Размер списка, его значения
# Внести в функцию список
# Вывести отсортированный список в консоль

# Функции сортировки
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



new_list_size = int(input("Введите размер списка: "))
new_list = []
for _ in range(new_list_size):
    element = int(input("Введите значение элемента списка: "))
    new_list.append(element)
sort_min_to_max(new_list)
print("Отсортированный лист: ", new_list)
