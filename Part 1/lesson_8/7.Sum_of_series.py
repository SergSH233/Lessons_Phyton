n = int(input("Введите натуральное положительное число: "))
sum_of_series = 0
while n <= 0:
    n = int(input("ВВЕДЕННОЕ ЧИСЛО ОТРИЦАТЕЛЬНОЕ!!! Введите вновь: "))
for x in range(n):
    elem = ((-1)**x) * (1/2**x)
    print("x = ", elem)
    sum_of_series += elem
print("Сумма ряда элементов =",sum_of_series)