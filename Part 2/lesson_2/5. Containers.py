# Цель:
# Внести кол-во контейнеров которые есть на складе
#   - Каждому контейнеру написать его массу в невозрастающей последовательности (те на уеньшение веса)
# Добавить контенер к уже стоящим определив его положение в порядковой цепи уже установленных
#   - Сделать проверку того что контейнер не привышает 200
# Вывести итог какое место занимает контейнер

containers = []
caunt_containers = int(input("Введите кол-во контейнеров: "))
for _ in range(caunt_containers):
    weight = int(input("Введите вес (0 - 200): "))
    while weight > 200 or weight < 0:
        print("неверный вес! Введите вес заново")
        weight = int(input("Введите вес (0 - 200): "))
    containers.append(weight)
containers.sort(reverse=True)
print("|отладка|",containers)

new_containers = int(input("Введите вес нового контейнера: "))
while new_containers > 200 or new_containers < 0:
    print("неверный вес! Введите вес заново")
    new_containers = int(input("Введите вес (0 - 200): "))
counter = 1
for x in containers:
    if new_containers <= x:
        counter += 1
containers.append(new_containers)
containers.sort(reverse=True)
print("Ваш контейнер установлен под номером: ",counter)
print(containers)




