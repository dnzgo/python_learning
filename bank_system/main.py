from bank import BankAccount

accounts = []
accounts.append(BankAccount('Deniz', 1000))
accounts.append(BankAccount('Emir', 1500))

accounts[0].withdraw(200)
accounts[0].deposit(233)

for account in accounts:
    account.show_info()

accounts[0].transfer(accounts[1], 150)

for account in accounts:
    account.show_info()