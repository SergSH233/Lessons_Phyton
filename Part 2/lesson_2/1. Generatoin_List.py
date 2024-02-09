# Цель: Добавить в список количество чисел от 1 до N заданное пользователем.
# Числа в списке должны быть нечетные
numbers_list = []
num = int(input("Введите до кого числа выводить список: "))
for i in range(num):
    if i % 2 != 0:
        numbers_list.append(i)
print("Список чисел = ", numbers_list, end=" ")
