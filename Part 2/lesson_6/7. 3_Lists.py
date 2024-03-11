# Цель: Имея 3 готовых списка из задания поэксперементировать с множемтвами (set).
# 1. Найти элементы, которые есть в каждом списке
# 2. Найти элементы из первого списка, которых нет во втором и третьем списках.
# ! Все задачи нужно выполнить двуми спосабами: С использованием множиств и без них

# Списки
array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]


# Преобразование списков в словари для работы со множествами
nums_1 = set(array_1)
nums_2 = set(array_2)
nums_3 = set(array_3)

# Задача 1.
# Множество

print("# Задача 1. Множества:",nums_1.intersection(nums_2).intersection(nums_3))

# Без использования множества
array_4 = []
if len(array_1) > len(array_2)  and len(array_1)  > len(array_3) :
    for num in array_1:
        if num in array_2:
            if num in array_3:
                array_4.append(num)
elif len(array_2) > len(array_1)  and len(array_2)  > len(array_3) :
    for num in array_2:
        if num in array_1:
            if num in array_3:
                array_4.append(num)
else:
    for num in array_3:
        if num in array_1:
            if num in array_2:
                array_4.append(num)
print("# Задача 1. Без использования множества:",array_4)

# Задача 2.
# Множество

print("# Задача 2. Множества:", nums_1.difference(nums_2).difference(nums_3))

# Без использования множества
array_5 = []
for num in array_1:
    if num not in array_2:
        if num not in array_3:
            array_5.append(num)
print("# Задача 2. Без использования множества:",array_5)