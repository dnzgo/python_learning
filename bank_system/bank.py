class BankAccount(): # class definition
    # initializing an object with constructor
    def __init__(self, name, balance): # self refers to current object/instance
        self.name = name
        self.balance = balance
    

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print('Deposited amount: ', amount)
        else:
            print('Invalid amount')

    
    def withdraw(self, amount):
        if amount > self.balance:
            print('not enough money')
        elif amount <= 0:
            print('Invalid amount')
        else:
            self.balance -= amount
            print('Withdrawn amount: ', amount)
    

    def show_info(self):
        print('Name: ', self.name)
        print('Balance: ', self.balance)
    

    def transfer(self, other_account, amount):
        if amount > self.balance:
            print('u do not have enough money')
        elif amount <= 0:
            print('Invalid amount')
        else:
            self.balance -= amount
            other_account.balance += amount
            print('you transfered ' + str(amount) + ' to ' + other_account.name)
