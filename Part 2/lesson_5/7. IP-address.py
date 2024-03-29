# Цель: Создать проверку на правильность написания IP адреса.
# 1. Создать переменную для ввода IP
# 2. Сделать проверку длинны (от 7 до 15 символов)
# 3. Разделить строку на элементы методом split(".")
# 4. Создать цикл для проверки каждого элемента
# - а.не привышает ли значение 255.
#  -б.Есть ли в значении посторонние элементы.
# 5. Вывод результата.

print("Введите новый IP адрес по данному шаблону:\n255.255.255.255")

while True:
    nums = False
    symbol = False
    error = ""

    new_ip = input("Введите новый IP: ")
    new_ip_split = new_ip.split(".")
    for x in new_ip_split:
        if x.isdigit():
            if 0 <= (int(x)) <= 255:
                continue
            else:
                error = x
                nums = True
                break
        else:
            error = x
            symbol = True
            break

    if len(new_ip_split) != 4:
        print("Данный IP не соответствует по длинне. Возможно вместо знака (.) вы поставили иной знак. Проверте!")
    elif symbol:
        print("Строка должна состоять исключительно их цифр!",error,"-неверное значение")
    elif nums:
        print("Значения должны быть в границе от 0 до 255.",error,"-неверное значение")
    else:
        print("Ваш новый IP:",new_ip)
        break

