# Цель: Переформатировать меню.
# 1. Получить на вход данные которые разделены между собою символом ";"
# 2. Сделать проверку на наличие этого символа (;) в данных
# 3. Создать массив из данных
# 4. Вывести полученные данные через запятую (,)
while True:
    text_data = input("Введите данные разделенные между собой симвалом(;): ")
    if ";" in text_data:
        break
format_menu = text_data.split(";")
print(format_menu)
new_menu = ", ".join(format_menu)
# new_menu = [",".join(x) for x in format_menu]
print(new_menu)
