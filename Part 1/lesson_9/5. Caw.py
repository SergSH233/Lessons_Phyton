corral = int(input("Введите кол-во загонов для коров: "))
print("Всего загонов ", corral)
corral_occupied = input("Введите наличие коровы в загоне.\nA - Корова в загоне\nB - коровы в загоне нет\n")
count = 1
sum_milk = 0


while len(corral_occupied) != corral:
    print("Всего загонов ", corral)
    corral_occupied = input("Введите верное количество A и B соответственно имеющимся загонам\n")
for caw in corral_occupied:
    if caw == "a" or caw == "A":
        sum_milk = sum_milk + (count * 2)
        count += 1
    elif caw == "b" or caw == "B":
        count += 1
    else:
        print("Веден неверный символ -",caw,"Расчет произведен из учета того что загон пустовал")
        count += 1
print("За день было произведено", sum_milk,"молока")

