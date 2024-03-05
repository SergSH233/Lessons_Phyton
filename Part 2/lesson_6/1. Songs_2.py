# Цель: Выбрать несколько песен (кол-во песен указывается пользователем) и подсчитать общую длинну их прослушивания.
# 1. Создать переменную для кол-ва выбора песен из списка.
# 2. Сделать проверку чтобы список не привышал суммарное количество песен в списке.
# 3. Создать переменную float для подсчета времени.
# 4. Создать поиск по словарю для добовления песни в новый плей-лист
# 5. Вывод результата в строку консоли.

# Словарь песен взят из задания:

violator_songs = {
'World in My Eyes': 4.86,
'Sweetest Perfection': 4.43,
'Personal Jesus': 4.56,
'Halo': 4.9,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.20,
'Policy of Truth': 4.76,
'Blue Dress': 4.29,
'Clean': 5.83
}
# Метод подсчета времени

def FloatInMin(float):
    sec = 0.6
    minute = int((float * 100) // 100)
    sec_1 = ((float * 100) % 100)
    sec = int(sec_1 * sec)
    return print("Длинна плей-листа:",minute,"min", round(sec,2),"sec")

sum_time = float(0.0)
calc = 1
for x in violator_songs.keys():
    print(calc,".",x)
    calc += 1
num = int(input("Введите кол-во песен которые вы хотите добавить: "))
for _ in range(num):
    while True:
        song_name = input("Введите название песни из списка: ")
        if violator_songs.get(song_name) is not None:
            break
        else:
            print("Такой песни нет в списке! Введите название из списка")
    sum_time = sum_time + violator_songs[song_name]

FloatInMin(sum_time)
