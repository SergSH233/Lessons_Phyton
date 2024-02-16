# Цель: Создать программу генерирующую список чисел с помощью встроенных в нее условий, где вместо четных чисел
# ставим еденицу, а вместо не четных результат деления на 5 (%5).
# 1. Создать переменную для ввода длинны списка. Ввод осуществляется с консоли.
# 2. Создать список с необходимыми условиями внутри.
# 3. Вывод результата в консоль.

num = int(input("Введите длинну списка: "))
gen_num_list = [(x - (x - 1) if x % 2 == 0 or x == 0 else x % 5) for x in range(num)]
print("Генеративный список: ",gen_num_list)
