# Цель: Создать список списков(или конвертировать многомерный массив в одномерный)
# 1. Создать метод который принимает многомерный лист и возвращает одномерный.
# 2. Вставить список из задания в метод и вывести его в консоль.

def multi_dimenConcertList(m_list):
    new_list = [x for i in m_list
            for j in i
            for x in j]
    return new_list

lesson_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
print(multi_dimenConcertList(lesson_list))