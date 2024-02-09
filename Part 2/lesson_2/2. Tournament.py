# Цель:
# Создать список с именами участников турнира
#   - Добовление осужествляется с запроса пользователя
#   - Добавить проверку чтобы пользователей было не меньше 4-х и их финальное количество было кратно 2-м
# Создать метод для определения участников турнира в первый и второй день
#   - В первый день участвует каждый второй заявленный участник
participants_list = []
participants_1day = []
participants_2day = []
participants = int(input("Введите количество участников турнира (Не менее 4-х и кратное 2-м): "))
while participants % 2 != 0 or participants < 4:
    print("Недостаточно участников для проведения турнира")
    participants = int(input("Введите количество участников турнира (Не менее 4-х и кратное 2-м): "))

for _ in range(participants):
    name = input("Введите имя участника: ")
    participants_list.append(name)

for x in range(len(participants_list)):
    if x % 2 == 0:
        participants_1day.append(participants_list[x])
    else:
        participants_2day.append(participants_list[x])

print("В первый день учавствуют:")
calc = 1
for i1 in participants_1day:
    print(calc, ".", i1)
    calc += 1
print("Во второй день учавствуют:")
calc_2 = 1
for i2 in participants_2day:
    print(calc_2, ".", i2)
    calc_2 += 1