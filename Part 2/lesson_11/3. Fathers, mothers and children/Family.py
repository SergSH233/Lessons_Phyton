class Parent:
    # status = {0: "No reaction", 1: "Feed the baby", 2: "Soothe the baby", 3: "scold the child", 4: "play with baby"}
    status = {0: "Не реагирует", 1: "Решил покормить", 2: "Решил утешить", 3: "Решил наказать", 4: "Решил поиграть с ребенком"}
    health = 100
    scoring = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.status = 0

    def print_parent_state(self):
        print("Реакция родителя - {}".format(Parent.status[self.status]))

class Children:
    health = 100
    scoring = 100
    # status = {0: "plays", 1: "hungry", 2: "upset, scared", 3: "pranks"}
    status = {0: "Играть", 1: "Голодный", 2: "Раздраженный, испуган", 3: "Праказничает"}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.status = 0
        self.actions = 0

    def print_children_state(self):
        print("Ребенок сейчас хочет {}".format(Children.status[self.status]))


