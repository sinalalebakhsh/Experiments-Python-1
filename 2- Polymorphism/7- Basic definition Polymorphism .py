from cmath import pi
import os
os.system('cls')

class HumanBeings:
    def __init__(self, gender, age):
        self.gender = gender
        self.age = age

    def IsEating(self):
        raise NotImplementedError('You have to decide what to eat.')

class Man(HumanBeings):
    def __init__(self, age, height):
        super().__init__("Man", age)
        self.height = height

    def IsEating(self):
        return 'The man eats a hamburger.'

person1 = Man('28', '178 Cm')
print()
print(person1.IsEating())
print()
