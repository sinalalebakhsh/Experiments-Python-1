from cmath import pi
import os
os.system('cls')

class HumanBeings:
    def __init__(self, gender, age):
        self.gender = gender
        self.age = age

    def iseating(self):
        raise NotImplementedError('You have to decide what to eat.')

class Man(HumanBeings):
    def __init__(self, age, height):
        super().__init__("Man", age)
        self.height = height

    def iseating(self):
        print(f'The man eats a hamburger. With {self.height} cm height')
        after_eating = self.height * 3
        return f'But after eating hamburger, the man became {after_eating} cm tall '

class Women(HumanBeings):
    def __init__(self, age, height):
        super().__init__("Women", age)
        self.height = height

    def iseating(self):
        print(f'The Women eats a pasta. With {self.height} cm height')
        after_eating = self.height * 2
        return f'But after eating pasta, the woman became {after_eating} cm tall '

def show_what_eating(sina):
    print(sina.iseating())


person1 = Man('28', 178)
person2 = Women('20', 160)
print()
show_what_eating(person1)
print()
show_what_eating(person2)
print()
