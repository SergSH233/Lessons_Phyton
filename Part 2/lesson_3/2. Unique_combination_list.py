# Цель: Создать метод который при объединении и сортировке отставляет в списке только уникальные значения(Без повтора
# элементов)
# 1. Создать 2 списка (Числовой или строчный не имеет значения)(Ввод с элементов с консоли, но для теста
#       создать два готовых списка)
# 2. Объединить их в один и отсортировать по возрастанию (для строк в алфавитном порядке)
# 3. Сделать проверку на уникальность слов в котором повторяющиеся слова удаляются.
# 4. Вывести получившийся список на экран

# Методы содания списка:
def NewList_Str(size):
    print("Введите", size, "элементов")
    list = []
    for _ in range(size):
        elem = input("Введите новый строчный элемент списка: ")
        list.append(elem)
    return list


def NewList_Int(size):
    print("Введите", size, "элементов")
    list = []
    for _ in range(size):
        elem = int(input("Введите новый целочисленный элемент списка: "))
        list.append(elem)
    return list

# Готовые примеры для проверки Метода

# Числовые листы
list_1 = [12,89,9,135,19,109,135,76]
list_2 = [90,31,30,87,19,109,14,34,98,15]

# Введенные с консоли
# print("list 1")
# list_1 = NewList_Int(5)
# print("list 2")
# list_2 = NewList_Int(3)

# Строчные листы
# list_1 = ["Форд","Фольцваген","Вольво","Фиат","Рено"]
# list_2 = ["Тойота","Хонда","Хендай","Вольво","Форд","Ситроен"]

# Введенные с консоли
# list_1 = NewList_Str(5)
# list_2 = NewList_Str(3)


# Пустой лист
# list_2 = []


def UniqueCombinatonSortList(List_1, List_2):
    List_1.extend(List_2)
    List_1.sort()
    duble = []
    for x in range(len(List_1) - 1):
        elem_1 = List_1[x]
        elem_2 = List_1[x + 1]
        if elem_1 == elem_2:
            duble.append(elem_2)
    for x in range(len(duble)):
        List_1.remove(duble[x])
    return List_1


# Решение задачи
print("Cписок 1:", list_1, "\nСписок 2: ", list_2)
sort_list = UniqueCombinatonSortList(list_1, list_2)
print("Уникальны список: ", sort_list)
