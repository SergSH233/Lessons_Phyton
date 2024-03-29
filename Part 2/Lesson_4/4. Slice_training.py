# Цель: Тренировка работы со срезами списка
# 1. Взять список из задания и сделать операции:
#   - а) Копия списка, б)revers, в) вывести каждый второй элемент, г) все элементы до второго,
#   - д) все элементы с конца до последнего, е) от 3-его до 4-го без 4-ого элемента, ж) последние 3 - элемента,
#   - з) диапазон от 3-его до 4-ого включа 4-ый, и) тоже задание что и в "з)" только в обратном порядке.

alphabet = 'abcdefg'

print("Копия списка:", alphabet[:])
print("Revers:", alphabet[::-1])
print("Каждый второй элемент:", alphabet[::2])
print("Все элементы до второго:", alphabet[:1])
print("Все элементы с конца до последнего: ", alphabet[:0:-1])
print("от 3-его до 4-го без 4-ого элемента: ", alphabet[3:4])
print("последние 3 - элемента: ", alphabet[len(alphabet)-3:])
print("диапазон от 3-его до 4-ого включа 4-ый: ", alphabet[3:(4+1)])
print("в обратном порядке: ", alphabet[4:2:-1])