# Цель: Напишисать функцию, которая сортирует по возрастанию кортеж, состоящий из целых чисел,
#       и возвращает его отсортированным. Если хотя бы один элемент не является целым числом,
#       то функция возвращает исходный кортеж.

# Function
def tpl_sort(tpl):
    type_flag = False
    for x in tpl:
        if type(x) != int:
            type_flag = True
            break
    if type_flag:
        return tpl
    else:
        return sorted(tpl)

# Data example
tpl = (6, 3,-1, 8, 4, 10, 9)

# Result
print(tpl_sort(tpl))