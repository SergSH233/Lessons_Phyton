# Цель: Создание нового плей-листа на базе уже имеющихся. Подсчет времени его прослушивания
# 1. Создать альбом уже имеющихся у пользователя песен. Прим: CurtainCall = [["Lose Yourself],[5.14]]
# 2. Создать новый Play-List(PL), с указанием его размара.
#   - выводить сообщение если песни нет в имеющемся списке
# 3. Вывод в консоль кол-во песен и их общую продолжительность.

# Альбом взят из задания
# Depeche Mode - Violator

violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
new_pl = []
pl_size = int(input("Введите кол-во песен нового плей-листа: "))
# for _ in range(int(input("Введите кол-во песен нового плей-листа: "))):
while len(new_pl) < pl_size:
    name_song = input("Введите название песни: ")
    for i in range(len(violator_songs)):
        for j in range(len(violator_songs[i])):
            if violator_songs[i][j] == name_song:
                new_pl.append(violator_songs[i][j])
                print("Добавлена песня: ",violator_songs[i][j])
                break
            else:
                print("Такой песни тут нет")
print(new_pl)

