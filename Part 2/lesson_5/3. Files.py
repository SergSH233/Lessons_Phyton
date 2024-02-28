# Цель: Сделать проверку при сохранении файла в определенном формате (txt, docx)
# 1. Создать переменную для ввода названия файла.
# 2. Сделать проверку в начале названия на наличие запрещенных для ввода символов (@,#,$,%,^,&,*,/)
# 3. Создать проверку в конце название на наличие формата (txt, docx)

print("Введите название файла с окончанием его формата (.txt, .docx)")
start_word = ["@","№","$", "^", "&", "*", "/","%"]
format_file = [".txt",".docx"]
while True:
    file_name = input("Ввод: ")
    start_flag = False
    format_flag = False

    for x in range(len(start_word)):
        if file_name.startswith(start_word[x]):
            start_flag = True
            break
    for x in range(len(format_file)):
        if file_name.endswith(format_file[x]):
            format_flag = True
            break
    if start_flag:
        print("Некоректное имя файла! В нем не должны присутствывать знаки (@,№,$,^, &, *, /, %) ")
    elif not format_flag:
        print("Неверный формат файла. Файл должен заканчиватся на (.txt, .docx)")
    else:
        print("Файл сохранен!")
        break