# Цель: Напишите программу, которая инициализирует список из 10 случайных целых чисел,
#       а затем делит эти числа на пары кортежей внутри списка.

import random

info_1 = [random.randint(1,100) for _ in range(0,10)]

info = enumerate(info_1)
first_element = 0
new_list = []
for index, x in info:
    if index % 2 == 0:
        first_element = x
    else:
        second_element = x
        new_list.append((first_element, second_element))
        first_element = 0
print(new_list)

