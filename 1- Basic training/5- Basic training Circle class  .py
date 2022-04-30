from cmath import pi
import os
os.system('cls')

class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
    
    def calc_diameter(self):
        return self.radius * 2

    def area_of_circle(self):
        return pi * (self.radius ** 2)

    def circumference(self):
        return (2 * pi ) * self.radius

circle_1 = Circle(32)

print()
print(f'Area circle --> {circle_1.area_of_circle()}')
print()
print(f'Circumference circle --> {circle_1.circumference()}')
print()
print(f'Diameter circle --> {circle_1.calc_diameter()}')
print()


