educational_grant = int(input("Введите размер ежемесячной степендии: "))
expenses = int(input("Введите ежемесячные расходы: "))
parents_money = 0
for month in range(10):
    month += 1
    difference_in_money = educational_grant - expenses
    print(difference_in_money)
    if difference_in_money < 0:
        parents_money = parents_money + (difference_in_money * (-1))
        print("В", month, "-ом месяце обучения сумма необходимая от родителей будет состовлять ",
              (difference_in_money * (-1)))
    else:
        print("В", month, "-ом месяце помощь родителей не понадобиться")
    three_percent = (expenses / 100) * 3
    print('3% = ', three_percent)
    expenses += three_percent
print("Общая сумма необходимая от родителей за 10 месяцев составила: ", parents_money)
