class Property:
    def __init__(self, cost):
        self.__cost = self.set_coast(cost)

    def get_cost(self):
        return self.__cost

    def set_coast(self, cost):
        if cost < 0 or type(cost) != int:
            raise Exception("Недопустимые значения!")
        else:
            self.__cost = cost


class Apartment(Property):
    def __init__(self, city, address, apartment_area, cost):
        super().__init__(cost)
        self.city = city
        self.address = address
        self.apartment_area = apartment_area

    def __str__(self):
        return "City: {City}\t Address: {Address}\nApartment Area: {Apartment_area} m2\nCost: {Cost}".format(
            City=self.city,
            Address=self.address,
            Apartment_area=self.apartment_area,
            Cost=self.get_cost()
        )


class Car(Property):
    def __init__(self, cost, brand, model, year):
        super().__init__(cost)
        self.brand = brand
        self.model = model
        self.year = self.set_year(year)

    def set_year(self, year):
        if year <= 1901:
            raise Exception("Введены неверные данные! До 1902 года были лишь телеги!")
        else:
            self.year = year



car1 = Car(cost=4000, brand="mazda", model="xedos 6", year=1901)

