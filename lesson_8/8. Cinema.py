print("Задача 8.8: Кинотеатр\nУсловие:\nX мальчиков и Y девочек пошли в кинотеатр и купили билеты на идущие подряд "
      "места в одном ряду.\nНапишите программу, которая выдаст, как нужно сесть мальчикам и девочкам,\nчтобы рядом с "
      "каждым мальчиком сидела хотя бы одна девочка,\n а рядом с каждой девочкой — хотя бы один мальчик.")
print()
boy = int(input("Введите кол-во мальчиков: "))
girl = int(input("Введите кол-во девочек: "))
seats = int(input("Введите кол-во мест в ряду: "))  # Доработать
sdt = (seats / 2) # Сидения в ряду деленные на 2
kids = boy + girl
difference = 0
row = 0
y = ""
while kids >= seats:
    if boy >= (seats/2) and girl >= sdt:
        for x in range(seats):
            if x % 2 == 0:
                y = y + "G"
                row += 1
            else:
                y = y + "B"
                row += 1
    print("Ряд", row,":", y)
    y = ""
    boy = boy - sdt
    girl = girl - sdt
    kids = kids - seats

if boy == 0 and girl == 0:
    print("Все дети рассажены")
else:
    if boy > girl:
        difference = girl / boy
        print(difference)
    else:
        difference = boy / girl
        print(difference)










