
import os
os.system('cls')

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
  
class BankAccount:
    def __init__(self, user_account, account_balance):
        self.user_account = user_account
        self.account_balance = account_balance

    def __str__(self):
        return f'Name account:{self.user_account}, Account balaance:{self.account_balance}'
         
    def __add__(self, other):
        new_user_account = self.user_account + other.user_account
        new_account_balance = self.account_balance + other.account_balance
        return (f"{new_user_account} | {new_account_balance}")

    def __iadd__(self, other):
        self.account_balance += other.account_balance
        return self
    
    def __repr__(self):
        return f'{self.__class__.__name__}(User account={self.user_account} \
                 | Account balance={self.account_balance})'
        

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
account2 += account1
print(colored(255, 0, 127, f'{account2}'))
print()
print(colored(0, 222, 255, repr(f'{account1}')))
print()
print(colored(255, 0, 127, repr(f'{account2}')))
print()

        

