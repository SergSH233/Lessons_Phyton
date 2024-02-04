earth = float(1.08321 * 10 ** 12)
radius_new_planet = float(input("Введите радиус для новой планеты: "))
new_planet = float((4/3) * 3.14 * (radius_new_planet ** 3))
difference = float(earth/new_planet)
if difference < 1:
    x = 1/difference
    print("Объем планеты земля меньше в",round(x,3),"раз")
else:
    print("Объем планеты земля больше в",round(difference,3),"раз")
