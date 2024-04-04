import Student

st1 = Student.Student("Ivan", 4, 5, 3, 4, 5, 6)
st2 = Student.Student("Petya", 4, 6, 1, 4, 3, 6)
st3 = Student.Student("Sasha", 3, 4, 7, 6, 1, 2)
st4 = Student.Student("Vanya", 2, 5, 6, 3, 7, 1)
st5 = Student.Student("Dima", 1, 3, 1, 6, 2, 4)
st6 = Student.Student("Kirill", 2, 5, 6, 2, 5, 1)
st7 = Student.Student("Leonid", 4, 7, 4, 9, 5, 9)
st8 = Student.Student("Stanislav", 2, 5, 6, 4, 4, 7)
st9 = Student.Student("Fedor", 3, 7, 1, 2, 5, 6)
st10 = Student.Student("Stepan", 2, 4, 5, 4, 5, 6)
list = [st1,st2,st3,st4,st5,st6,st7,st8,st9,st10]
print(list[0].number_group)