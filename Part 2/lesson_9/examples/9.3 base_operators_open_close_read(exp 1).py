import os

file_1 = os.path.abspath(os.path.join(os.path.sep,"task","group_1.txt"))
file_2 = os.path.abspath(os.path.join(os.path.sep,"task","Additional_info","group_2.txt"))
group_1 = open(file_1, 'r')
group_2 = open(file_2, 'r')

sum_group_1 = 0
difference_group_1 = 0
multiplication = 0
multiplication_group_2 = 1

for i_line in group_1:
    calc = i_line.split()
    sum_group_1 = sum_group_1 + int(calc[2])
    difference_group_1 = difference_group_1 - int(calc[2])
for i_line in group_2:
    calc = i_line.split()
    multiplication = int(calc[2])
    multiplication_group_2 = multiplication_group_2 * multiplication


print(sum_group_1)
print(difference_group_1)
print(multiplication_group_2)
# for i in os.listdir(file_1):
#     print(i)