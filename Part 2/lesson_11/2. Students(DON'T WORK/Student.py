# Цель: Реализовать модель с именем Student,
# содержащую поля «ФИ»,
# «Номер группы»,
# «Успеваемость» (список из пяти элементов).
# Создать список из десяти студентов (данные о студентах можете придумать или запросить у пользователя)
# Отсортировать список по возрастанию среднего балла. Выведите результат на экран.
class Student:



    # for i_elem in achievement.keys():
    #     try:
    #         print("What's your score on", i_elem)
    #         grad = int(input("Enter a grade: "))
    #         achievement[i_elem] = grad
    #     except ValueError:
    #         print("Error!!! Enter only numbers")
    # grad_sum = 0
    # for i_grade in achievement.values():
    #     grad_sum += i_grade
    # aver_grade = grad_sum / 5

    def __init__(self,name,number_group,English,Math,Physics,Informatics,Biology):
        self.name = name
        self.number_group = number_group
        self.achievement = {"English": English, "Math": Math, "Physics": Physics, "Informatics": Informatics, "Biology": Biology}





# student_1 = Student()
# print("Средний балл {name} = {aver}".format(name=student_1.name,aver=student_1.aver_grade))
