class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        print("Name: {}\nSalary: {}\n".format(self.name, self.salary))


emp_1 = Employee("Karl", 4000)
emp_2 = Employee("Sten", 12000)
emp_1.info()
emp_2.info()


class Potato:
    state = {0: "Отсутствует", 1: "Росток", 2: "Зеленая", 3: "Зрелая"}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print("Картошка {} сейчас в стадии {}".format(self.index,Potato.state[self.state]))

    def is_ripe(self):
        if self.state == 3:
            return True
        return False


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print("Картошка проростает!")
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all([i_potato.is_ripe() for i_potato in self.potatoes]):
        # for i_potato in self.potatoes:
        #     if not i_potato.is_ripe():
            print("Картошка еще не созрела!\n")
                # break
        else:
            print("Вся картошка созрела! Можно собирать!")

my_potato = PotatoGarden(4)
my_potato.are_all_ripe()
for _ in range(5):
    my_potato.grow_all()
    my_potato.are_all_ripe()