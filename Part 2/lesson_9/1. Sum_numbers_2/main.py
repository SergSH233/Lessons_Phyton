# Цель: Взять из файла numbers.txt данные и все между собою сумировать. Результат записать в файле answer.txt
numbers = open('numbers.txt','r')
sum = 0
for i_line in numbers:
    num_list = i_line.split()
    for i_num in num_list:
        sum += int(i_num)
numbers.close()
sum_str = str(sum)
numbers_str = open('answer.txt', 'w')
numbers_str.write(sum_str)
numbers_str.close()

