# Цель:
# Напишите программу, которая проверяет данные из файла для каждой строки:
# Присутствуют все три поля.
# Поле «Имя» содержит только буквы.
# Поле «Имейл» содержит @ и точку.
# Поле «Возраст» представляет число от 10 до 99.


with open("registrations.txt", "r") as people_info:
    with open("registrations_good.log",'a') as good_log:
        with open("registrations_bad.log",'a') as bad_log:
            for i_line in people_info:
                try:
                    i_people = i_line.split()
                    if len(i_people) < 3:
                        raise IndexError()
                    if not i_people[0].isalpha():
                        raise NameError("Имя содержит не только буквенные символы")
                    if not "@" in i_people[1] or not "." in i_people[1]:
                        raise SyntaxError("Неверный e-mail, нет символа @")
                    if not "." in i_people[1]:
                        raise SyntaxError("Неверный e-mail, нет символа (.) ")
                    if not 10 <= int(i_people[2]) <= 99:
                        raise ValueError("Неверно указан возраст!")
                    else:
                        good_log.write("\n" + i_line)
                except IndexError:
                    bad_log.write(i_line + "Не заполнены все поля\n*************\n")
                    print(i_people, "Не заполнены все поля")
                except NameError:
                    bad_log.write(i_line + "Имя содержит не только буквенные символы\n*************\n")
                    print(i_people, "Имя содержит не только буквенные символы")
                except SyntaxError:
                    bad_log.write(i_line + "Неверный e-mail\n*************\n")
                    print(i_people,"Неверный e-mail")
                except ValueError:
                    bad_log.write(i_line + "Неверно указан возраст!\n*************\n")
                    print(i_people,"Неверно указан возраст!")
# print("bad_log",bad_log.closed)
# print("good_log",good_log.closed)

