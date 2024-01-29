client_numbers = []
total_debit = 0

for number in range(10):
    number = number + 1
    print("Введите ID клиента №", number)
    client_numbers.append(int(input("Значение ID от -1000 до 1000: ")))

for client in client_numbers:
    if client > 0 and client % 2 == 0:
        print("У клиента с ID: ", client, " есть задолженность")
        total_debit = total_debit + 1
    elif client <= 0:
        print("клиент номер ", client, " # Error!! Сбой в системе")
    else:
        print("клиент номер ", client, " без задолженности")
print("Всего должников ", total_debit)
