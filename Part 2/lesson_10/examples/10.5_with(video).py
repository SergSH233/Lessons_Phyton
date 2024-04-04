line_count = 0
sym_sum = 0
try:
    with open("people.txt",'r') as people_file:
        for i_line in people_file:
            line_count += 1
            length = len(i_line)
            if i_line.endswith("\n"):
                length -= 1
            if length < 3:
                raise BaseException('Длинна {} строки меньше 3-х символов'.format(line_count))
            sym_sum += len(i_line)

except FileNotFoundError:
    print("Файл не найден")
finally:
    print("Сумма найденых символов ровна:",sym_sum)
    print(people_file.closed)
