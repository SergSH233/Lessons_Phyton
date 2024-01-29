employee_salary_year = []
average_salary = 0
sum_money_year = 0
for month in range(12):
    employee_salary = 0
    number_month = month + 1
    print("Введите зарплату полученную работником в месяце №", number_month)
    print("!!! Если работник не получал никкаких средств в месяце №", number_month,", то в программу введите цифру 0 ")
    employee_salary = int(input("Ввод Суммы: "))
    if employee_salary != 0:
        employee_salary_year.append(employee_salary)
        print()
    else:
        print()

print(len(employee_salary_year))

for x in employee_salary_year:
    sum_money_year = x + sum_money_year

average_salary = sum_money_year / len(employee_salary_year)
print("Средняя зарплата роботника за год составила ", average_salary)
print("Работник отработал ", len(employee_salary_year), "месяцев за этот год")
