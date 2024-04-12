class Property:
    def __init__(self, cost):
        self.set_coast(cost)

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
        self.set_year(year=year)

    def set_year(self, year):
        if year <= 1901:
            raise Exception("Введены неверные данные! До 1902 года были лишь телеги!")
        else:
            self.year = year

    def __str__(self):
        return "Brand: {brand}\t Model: {model}\nYear: {year}\nCost: {cost}".format(
            brand=self.brand,
            model=self.model,
            year=self.year,
            cost=self.get_cost()
        )


car1 = Car(cost=4000, brand="Mazda", model="Xedos 6", year=1995)
print(car1)
