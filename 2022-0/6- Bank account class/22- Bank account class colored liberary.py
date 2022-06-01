
import os
os.system('cls')

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
  
# text = 'Hello, World'
# colored_text = colored(0, 222, 255, text)
# print(colored_text)
# #or
# print(colored(255, 0, 127, 'Hello, World'))

class BankAccount:
    def __init__(self, user_account, account_balance):
        self.user_account = user_account
        self.account_balance = account_balance

    def __str__(self):
        return f'Name account:{self.user_account}, Account balaance:{self.account_balance}'
         
    def __add__(self, other):
        return (f"{self.user_account} + {other.user_account} | {self.account_balance + other.account_balance}")

    def transfer(self, user_account2 , transfer_amount):
        self.user_account2 = user_account2
        self.transfer_amount = transfer_amount
        self.account_balance += self.transfer_amount
        return self.account_balance
        

account1 = BankAccount("sina", 1000)

account2 = BankAccount('sasan', 400)
print()
print(colored(0, 222, 255, f'{account1 + account2}'))
print()
print(colored(255, 0, 127, f'{account1 + account2}'))
print()
        

