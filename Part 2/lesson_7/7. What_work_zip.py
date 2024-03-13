# Цель: Написать программу которая наглядно покажет как работает функция zip

import random
nums = [(random.randint(1,100)) for _ in range(1,6)]
print(nums)
nums_t = tuple(nums)
keys = ("d","t","p","x","o")

if len(nums_t) <= len(keys):
    lengue = len(nums_t)
else:
    lengue = len(keys)

for num in range(lengue):
    ziper = (keys[num],nums_t[num])
    print(ziper)