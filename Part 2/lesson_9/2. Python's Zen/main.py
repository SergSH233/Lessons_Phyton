# Цель: Взять текст из файла zen.txt, считать с него строки и вывести их в обратном порядке.

zen = open("zen.txt", 'r')
zen_return = ""
for x in zen:
    zen_return = x + zen_return
print(zen_return)
