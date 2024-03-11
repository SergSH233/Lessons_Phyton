# Цель: Переписать код из задания, чтобы он был более читаемый и отвечал стандартам pythonic.
# 1. Создать метод для вывода в кансоль ID студента и его возраст.
# 2. Создать метод для вывода в кансоль Полный список интересов всех студентов.
# 3. Создать метод для вывода в кансоль Общей длинны всех фамилий студентов.

def name_and_age_students(dict_stud):
    students = dict_stud
    age_students = [(students[id_name]["name"], students[id_name]["age"]) for id_name in students]
    for id_student in range(len(age_students)):
        print(age_students[id_student][0], "-", age_students[id_student][1], "age")


def all_interests_students(dict_stud):
    students = dict_stud
    interests_list = [(j) for i_name in students for j in students[i_name]["interests"]]
    for interests_all_stud in interests_list:
        print(interests_all_stud)


def sum_letters_students_surname(dict_stud):
    students = dict_stud
    sum_letters = 0
    for id_student in students:
        sum_letters += int(len(students[id_student]["surname"]))
    print("Total letters of students surname:", sum_letters, "letters")


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

name_and_age_students(students)
all_interests_students(students)
sum_letters_students_surname(students)
