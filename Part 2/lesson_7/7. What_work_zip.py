# Цель: Написать программу которая наглядно покажет как работает функция zip

import random
nums = [(random.randint(1,100)) for _ in range(1,6)]
print(nums)
nums_t = tuple(nums)
keys = ("d","t","p","x","o")

lengue = min(len(nums_t),len(keys))

ziper = ((keys[num],nums_t[num]) for num in range(lengue))

print(ziper)
for key, num in ziper:
    print(key,num)