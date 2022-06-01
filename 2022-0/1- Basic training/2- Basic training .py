import os
os.system('cls')


class CarClass:
    def __init__(self, car_color, model, types_of_chassis):
        self.color = car_color
        self.model = model
        self.chassis = types_of_chassis 
        # 1-Hatchback 2-Sedan/Notchback 3-Estate/Station Wagon 
        #4-  Multi Purpose Vehicle (MPV) / Multi Utility Vehicle (MUV)
        #5-Sport Utility Vehicle (SUV)
        #6- Pick-Up Truck
        #7-  Van


    def print_details(self):
        return f'Color:{self.color} | Model:{self.model} | Type of Chassis:{self.chassis}'

car1 = CarClass('Red', 'TOYOTA', 'Pick-Up Truck')

print()
print(car1.print_details())
print()
