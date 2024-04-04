name_list = []

while True:
    try:
        name = input("Введите имя: ")
        if name.lower() == "error":
            raise BaseException("Ты сломал программу!!!")
        if not name.isalpha():
            raise TypeError
        name_list.append(name)
        if len(name_list) == 5:
            print("Место закончилось")
            break
    except TypeError:
        print("Что ты ввел?!")
    except BaseException:
        print("Введено стоп слово")
        name_list = []
        raise

name_file = open("name.txt",'r')
name_file.write("\n".join(name_list))
name_file.close()
print("Работа завершена!")