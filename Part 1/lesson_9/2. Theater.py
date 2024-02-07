row = int(input("Введите кол-во рядов: "))
sitting = int(input("Введите кол-во сидений в ряду: "))
distance = int(input("Введите расстояние между рядами: "))
sitting_vis = "|-|"
distance_vis = "*"
theater_plan = ""
row_number = (sitting_vis * sitting) + (distance_vis * distance) + (sitting_vis * sitting)
for r in range(row):
    theater_plan = theater_plan + row_number + "\n"

print("-----Сцена театра-----")
print(theater_plan)