# Цель: Напишите функцию, возвращающую список элементов итерируемого объекта
#       (кортежа, строки, списка, словаря),
#       у которых индекс — это простое число.
# 1. Создать метод для повери индекса на простое число(Метод взят из интернета)
# 2. Конвертировать данные в картеж и пройти по его элементам.
# 3. Вернуть список получившихся элементов.
# Метод взят из интернета
# (https://ru.stackoverflow.com/questions/1040160/%D0%9A%D0%B0%D0%BA-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%B8%D1%82%D1%8C-%D0%BF%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%B5-%D0%BB%D0%B8-%D1%87%D0%B8%D1%81%D0%BB%D0%BE-python-3)

def is_prime(num):
    prime = num > 1 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3)
    i = 5;
    d = 2;

    while prime and i * i <= num:
        prime = num % i != 0
        i += d
        d = 6 - d
    return prime

# Метод который печатает только элементы с индексом простого числа
def print_only_is_prime_index(data):
    tup_date = enumerate(data)
    return print([(values) for index, values in tup_date if is_prime(index)])

# Примеры данных
info_1 = [25,45,96,2,4,3,10,15]
info_2 = "Добро пожаловать в светлую гавань"

# Вывод данных
print_only_is_prime_index(info_1)
print()
print_only_is_prime_index(info_2)