# Цель: В введенном пользователем слове развернуть часть слова между парными буквами.
# 1. Создать переменную введенного пользователем слова.
# 2. Спросить пользователя какая буква в слове парная
# 3. Выделить индексы повторяющихся букв в переменные.
#   -если индексы одинаковые попросить у пользователя ввести иное слово
# 4. Создать 3 переменных для разделения слова.
# 5. В переменной с дублирующимися буквами сделать разворот.
# 6. Создать переменную new_word для склейки слова и вывода его в консоль.
while True:
    word = input("Введите слово с повторяющимися буквами: ").lower()
    double_letter = input("Введите повторяющуюся букву: ").lower()
    while True:
        if double_letter in word:
            print("Буква: ",double_letter)
            break
        else:
            double_letter = input("Введите ИМЕЮЩУЮСЯ в слове букву: ").lower()
    start_point = word.index(double_letter)
    end_point = word.rindex(double_letter)
    if start_point == end_point:
        print("Введите иное слово!!!")
        continue
    else:
        break
start_NW = word[:start_point]
end_NW = word[end_point:]
revers_NW = word[start_point:end_point]
revers_NW = revers_NW[::-1]
new_word = start_NW + revers_NW + end_NW
print("Новое слово: ", new_word)