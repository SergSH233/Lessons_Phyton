import math
exponent = float(2.718)
natur_num = int(0)
lg = float(0)
nums = int(input("Введите кол-во чисел для подсчета: "))
for num in range (nums):
    x = float(input("Введите десятичную дробь для расчета: "))
    if x > 0:
        natur_num = int(x + 1)
        lg = math.log(natur_num)
        print("log(",natur_num,") =",lg)
    elif x < 0:
        natur_num = int(x - 1)
        lg = exponent * natur_num
        print("exp(",natur_num,") =",lg)


