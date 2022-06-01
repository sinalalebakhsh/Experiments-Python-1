import os
os.system('cls')

class HumanBeings:
    def __init__(self, gender, age):
        self.gender = gender
        self.age = age

    def __str__(self):
        return self.gender  # ---->>>> this here the magic method runing  

sina = HumanBeings('man', '28')

print()
print(sina)
print()
print()
