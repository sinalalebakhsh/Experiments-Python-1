import os
os.system('cls')


class CarClass:
    def __init__(self, car_color):
        self.color = car_color

car1 = CarClass('red')

print(car1)

print(car1.color)

