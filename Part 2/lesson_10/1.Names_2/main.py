# Цель: Напишите программу, которая берёт количество символов в каждой строке файла
# и в качестве ответа выводит общую сумму.
# Если в какой-либо строке меньше трёх символов (не считая литерала \n),
# то вызывается ошибка и сообщение, в какой именно строке она возникла.
# Программа при этом не завершается и обрабатывает все имена файла.
# Также при желании можно вывести все ошибки в отдельный файл errors.log.

line_count = 1
sym_sum = 0
try:
    with open("people.txt", 'r') as people_file:
        for i_line in people_file:
            line_count += 1
            length = len(i_line)
            if i_line.endswith("\n"):
                length -= 1
            if length < 3:
                raise BaseException('Длинна {} строки меньше 3-х символов'.format(line_count))
            sym_sum += len(i_line)

except FileNotFoundError:
    with open("errors.log", 'a') as errors:
        print("Файл не найден")
        errors.write("\nFileNotFoundError - Файл не найден")
except BaseException:
    with open("errors.log", 'a') as errors:
        print("Файл не найден")
        errors.write("\nBaseException - Длинна {} строки меньше 3-х символов".format(line_count))
    print('Длинна {} строки меньше 3-х символов'.format(line_count))
finally:
    print("Сумма найденых символов ровна:", sym_sum)
    print(people_file.closed)
    print(errors.closed)
