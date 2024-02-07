total_students_in_class = int(input("Введите кол-во учеников в классе"))
grade = []
for x in range(total_students_in_class):
    number_student = x + 1
    grade_st = int(input(("Введите оценку полученную студентом #", number_student," :")))
    if grade_st < 3 or grade_st > 5:
        print("Студент # ", number_student, "сегодня не отвечал")
    else:
        grade.append(grade_st)
