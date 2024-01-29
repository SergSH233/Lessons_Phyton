input_number = int(input("Введите число для нахождения факториала: "))
factorial = input_number
for x in range(input_number - 1):
    factorial = factorial * (x + 1)
    print(factorial)
print(input_number, "! = ", factorial)
