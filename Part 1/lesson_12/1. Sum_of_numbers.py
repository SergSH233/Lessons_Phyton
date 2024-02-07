# summa_n,
# которая принимает одно целое положительное число N
# и выводит сумму всех чисел от 1 до N включительно.
def Summa_N(number):
    sum_num = 0
    for x in range(1,number + 1):
        sum_num = sum_num + x
        # print(sum_num,"отладка")
    print("Сумма чисел от 1 до",number,"=",sum_num)

num = int(input("Введите положительное число для подсчета суммы чисел: "))
Summa_N(num)
