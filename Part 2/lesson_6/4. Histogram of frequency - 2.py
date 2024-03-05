# Цель: Написать программу для подсчета количества букв в тексте.
#       Прим.(key "б" - буква, values: "2" - количество повторений)
#       Затем итерировать этот словарь в новый где ключ и значения меняются местами.
# 1. Создаем переменную для ввода текста.
# 2. Содаем два пустых словаря count_text1 и count_text2.
# 3. Делаем цикл для разделения текста на символы и заполняя им словарь count_text1.
# 4. Вывод в консоль получившегося словаря.
# 5. Итерируем словарь count_text1 в словарь count_text2 следуя условиям.
# 6. Вывод в консоль словаря count_text2.

text = input("Введите текст: ").lower()
count_text1 = {}
count_text2 = {}

for x in text:
    if x not in count_text1:
        count_text1[x] = text.count(x)

for num in count_text1:
    print("'",num,"'", count_text1[num])

for x in count_text1.keys():
    if count_text1[x] not in count_text2:
        count_text2[count_text1[x]] = [x]
    else:
        count_text2[count_text1[x]].append(x)

for num in count_text2:
    print(num,":", count_text2[num])