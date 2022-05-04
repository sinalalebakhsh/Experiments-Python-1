
import os
os.system('cls')

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)
  
class BankAccount:
    def __init__(self, user_account, account_balance):
        self.user_account = user_account
        self.account_balance = account_balance

    def __str__(self):
        return f'Name account:{self.user_account}, Account balance:{self.account_balance}'
         
    def __add__(self, other):
        new_user_account = self.user_account + other.user_account
        new_account_balance = self.account_balance + other.account_balance
        return (f"{new_user_account} | {new_account_balance}")

    def __iadd__(self, other):
        self.account_balance += other.account_balance
        return (self)
    
    def __repr__(self):
        return f'{self.__class__.__name__}(User account={self.user_account} \
                 | Account balance={self.account_balance})'
    
    def __eq__(self, other):
        return self.account_balance == other.account_balance
        

    def transfer(self, other, withdrawal_amount):
        if other.account_balance >= withdrawal_amount:
            other.account_balance = other.account_balance - withdrawal_amount
            self.account_balance += withdrawal_amount
            return f'{other.user_account} - {withdrawal_amount} | {self.user_account} + {withdrawal_amount}'
        else:
            return f'This account does not have enough money.'
        

account1 = BankAccount("sina", 100)
account2 = BankAccount('sasan', 400)


print(account2.transfer(account1, 200))
print()
print()


        

