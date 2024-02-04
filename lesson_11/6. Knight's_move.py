# Функция вывода игрового поля
def graficBoardImput (axis_x, axis_y):
    chess_square = "|_|"
    horse = "|N|"
    board = ""
    for y in range(8):
        if y == int(axis_y):
            for x in range(8):
                if x == int(axis_x):
                    board = board + horse
                else:
                    board = board + chess_square
            board = board + "\n"
        else:
            board = board + (chess_square * 8) + "\n"
    print("Разположение на доске")
    print(board)

# Условное обозначение позиции на поле
# Ввод начальных данных
horse_x = float(input("Введите расположение коня по оси (X): "))
horse_y = float(input("Введите расположение коня по оси (y): "))
# Проверка нарушений границы поля
while (horse_y > 8 or horse_y < 0) or (horse_x > 8 or horse_x < 0):
    print("!!Введите координаты в границах поля!!\nКуда хотите поставить коня")
    horse_x = float(input("По оси (x): "))
    horse_y = float(input("По оси (y): "))
# Вывод таблицы с условным обозначением
graficBoardImput(horse_x,horse_y)
# Ввод новой координаты
print("Введите координаты куда хотите переставить коня")
new_point_x = float(input("По оси (x): "))
new_point_y = float(input("По оси (y): "))
# Проверка границ
while (new_point_y > 8 or new_point_y < 0) or (new_point_x > 8 or new_point_x < 0):
    print("!!Введите координаты в границах поля!!\nКуда хотите переставить коня")
    new_point_x = float(input("По оси (x): "))
    new_point_y = float(input("По оси (y): "))
# Сравнивание разницы между точками
dx = abs(int(horse_x) - int(new_point_x))
dy = abs(int(horse_y) - int(new_point_y))
# Проверка - отладка
# Сравнение и вывод если ход доступен
if (dx == 1 and dy == 2) or (dx == 2 and dy == 1):
    print("Ход конем возможен")
    graficBoardImput(new_point_x,new_point_y)
else:
    print("Так конь ходить не может")

