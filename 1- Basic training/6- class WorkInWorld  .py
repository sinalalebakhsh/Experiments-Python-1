from cmath import pi
import os
os.system('cls')

class WorkInWorld:
    def __init__(self, name, interest_rate):
        self.name = name
        self.interest_rate = interest_rate
    
    def details(self):
        return f'Work name: {self.name} | Interest rate: {self.interest_rate}'

class ProgrammingOption(WorkInWorld):
    def __init__(self, name, interest_rate, make_money):
        super().__init__(name, interest_rate)
        self.make_money = make_money
    
    def details(self):
        return f"""Work name: {self.name}
Interest rate: {self.interest_rate}
Make mony: {self.make_money}"""
    

programming = WorkInWorld('Programming', '100')
print()
print(programming.details())
print()
programming = ProgrammingOption('Programming', '100', '10.000 $USD in month')
print(programming.details())
print()


