class Family:
    surname = "Coman family"
    money = 100000
    have_a_house = False

    def info(self):
        print("Family name: {}\nFamily funds: {}\nHaving house: {}".
              format(self.surname, self.money, self.have_a_house))

    def earn_money(self, amount):
        self.money += amount
        print("Earning {} money\nCurrent value: {}".format(amount, self.money))

    def buy_house(self, house_price, discount=0):
        house_price -= house_price * discount / 100
        if self.money >= house_price:
            self.money -= house_price
            self.have_a_house = True
            print("House purchased! Current money: {}\n".format(self.money))
        else:
            print("Not enough money\n")


my_family = Family()
my_family.info()
my_family.buy_house(250000)
if not my_family.have_a_house:
    my_family.earn_money(170000)
    my_family.buy_house(250000, 25)
my_family.info()
