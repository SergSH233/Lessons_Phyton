end = int(input("Введите нижнюю границу X функции: "))
start = int(input("Введите верхнюю границу X функции: "))
step = -1
while end > start:
    print("Решение невозможно")
    end = int(input("Введите нижнюю границу X функции: "))
    start = int(input("Введите верхнюю границу X функции: "))
for x in range(start, end, step):
    y = (x ** 3) + 2 * (x ** 2) - (4 * x) + 1
    print("В точке", x, "y будет =", y)
