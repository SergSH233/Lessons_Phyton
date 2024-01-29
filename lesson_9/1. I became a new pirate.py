total_pirates = 0
word = ""
for cry in range(10):
    word = input("Введите пиратский клич: ")
    if word == "Карамба" or word == "Карамба":
        total_pirates += 1
    else:
        print("Ты трюмовая крыса, и наш карабль не место для тебя!!!")
print("Всего было принято на корабль", total_pirates,"человек")

