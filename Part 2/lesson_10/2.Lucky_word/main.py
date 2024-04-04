# Цель: Напишите программу, которая запрашивает у пользователя число до тех пор,
# пока сумма запрашиваемых чисел не станет больше либо равна 777.
# Каждое введённое число при этом дозаписывается в файл out_file.txt.
# Сделайте так, чтобы перед дозаписью программа с вероятностью 1 к 13
# выдавала пользователю случайное исключение и завершалась.
import random

sum_nums = 0
count_cycle = 1
random_number = random.randint(1,13)
print(random_number)
while sum_nums < 777:
    try:
        num = int(input("Введите число: "))
        if count_cycle == random_number:
            raise BaseException("Вас постигла неудача!")
        with open("out_file.txt",'a') as write_to_file:
            write_to_file.write("\n" + str(num))
    except ValueError:
        print("Неверный тип данных! Вводить можно только ЦИФРЫ!")
    except BaseException:
        print("Вам не удалось покинуть этот цикл")
        raise
    sum_nums += num
    count_cycle += 1
print("Поздравляю! Вам удалось выбратся из этого цикла!!!")


