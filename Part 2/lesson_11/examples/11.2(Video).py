import random


class User:
    user = "Admin"
    password = "qwerty"
    is_banned = False


user_1 = User()  # Экземпляр класса User
user_2 = User()


class Toyota:
    model = "Camry"
    color = "grey"
    coast = 1000000
    max_speed = 200
    speed = 0
    model_line = []

    def print_car_info(self):
        print("Model: {}\nColor: {}\nCoast: {}\nMax Speed: {}\nSpeed now: {}\n".
              format(self.model,self.color, self.coast, self.max_speed,self.speed))

    def add_model_line(self,model):
        if isinstance(model,Toyota):
            self.model_line.append(model.model)
        else:
            self.model_line.append(model)

    def current_speed(self,speed):
        self.speed = speed
        # print("Car speed now: {}\n".format(self.speed))



car_1 = Toyota()
car_2 = Toyota()
car_3 = Toyota()
car_1.speed = random.randint(0, 200)
car_2.speed = random.randint(0, 200)
car_3.speed = random.randint(0, 200)
print(car_1.speed, car_2.speed, car_3.speed)
car_1.print_car_info()
car_2.model = "Avensis"
car_1.add_model_line(car_2)
car_1.add_model_line("Tundra")
print(car_1.model_line)
car_1.current_speed(28)
car_1.print_car_info()