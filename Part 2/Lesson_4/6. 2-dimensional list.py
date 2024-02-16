# Цель: Создать двумерный список методом "List comcomprehensions".
# 1. Результат вывода должен быть по условию задачи: " [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]] "

# Решение:

new_list = [[x for x in range(1, 13, 4)], [x for x in range(2, 13, 4)], [x for x in range(3, 13, 4)],
            [x for x in range(4, 13, 4)]]
print(new_list)
