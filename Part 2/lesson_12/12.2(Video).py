class Person:
    __count = 0  # двойное нижнее подчеркивание изменяет наш параметр из публичного в приватный

    def __init__(self, name, age):
        self.set_name(name)
        self.__age = self.set_age(age)
        Person.__count += 1

    def __str__(self):
        return "Имя: {name}\t Возраст: {age}".format(name=self.__name, age=self.__age)

    def set_name(self, name):
        if str(name).isalpha():
            self.__name = name
        else:
            raise Exception("Имя должно состоять только из букв")

    def get_count(self):
        return self.__count

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age in range(1, 90):
            self.__age = age
        else:
            raise Exception("Недопустимый возраст")

    def get_name(self):
        return self.__name


misha = Person(name="Vova", age=15)
tomas = Person("Tomas", 25)
print(misha.get_count())
new_age = 50
tomas.set_age(new_age)
print(tomas.get_age())
print(misha.get_name())
print(misha.get_name())
misha.set_name("Misha")
print(misha.get_name())