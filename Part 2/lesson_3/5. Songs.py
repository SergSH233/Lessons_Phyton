# Цель: Создание нового плей-листа на базе уже имеющихся. Подсчет времени его прослушивания
# 1. Создать альбом уже имеющихся у пользователя песен. Прим: CurtainCall = [["Lose Yourself],[5.14]]
# 2. Создать новый Play-List(PL), с указанием его размара.
#   - выводить сообщение если песни нет в имеющемся списке
# 3. Вывод в консоль кол-во песен и их общую продолжительность.

def FloatInMin(float):
    sec = 0.6
    minute = int((float * 100) // 100)
    sec_1 = ((float * 100) % 100)
    sec = int(sec_1 * sec)
    return print("Длинна плей-листа:",minute,"min", round(sec,2),"sec")

# Альбом взят из задания
# Depeche Mode - Violator
calc = 1
total_time = float(0)
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
new_pl = [['Clean', 5.83],['Waiting for the Night', 6.07],['Policy of Truth', 4.76]]
pl_size = int(input("Введите кол-во песен нового плей-листа: "))
while len(new_pl) < pl_size:
    list_start = len(new_pl)
    list_finish = 0
    name_song = input("Введите название песни: ")
    for i in range(len(violator_songs)):
        for j in range(len(violator_songs[i])):
            if violator_songs[i][j] == name_song:
                name = violator_songs[i][j]
                time = violator_songs[i][j + 1]
                new_pl.append([name,time])
                print("Добавлена песня: ",violator_songs[i][j])
    list_finish = len(new_pl)
    if list_start == list_finish:
        print("Такой песни нет в вашем списке")
# print(new_pl)
for x in range(len(new_pl)):
    total_time = total_time + float(new_pl[x][1])
    print(calc,new_pl[x][0],"Time:",new_pl[x][1])
    calc += 1
FloatInMin(total_time)


