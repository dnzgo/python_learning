from transaction import Transaction

transaction_history = []

def add_income(amount, category):
    income_transaction = Transaction(amount, category, 'income')
    transaction_history.append(income_transaction)
    print('You have a new income ' + category + ' amount: ' + str(amount))


def add_expense(amount, category):
    expense_transaction = Transaction(amount, category, 'expense')
    transaction_history.append(expense_transaction)
    print('You have a new expense' + category + ' amount: ' + str(amount))


def calculate_balance():
    balance = 0
    for transaction in transaction_history:
        if transaction.type == 'income':
            balance += transaction.amount
        elif transaction.type == 'expense':
            balance -= transaction.amount

    return balance


def show_balance():
    print('Your current balance is ' + str(calculate_balance()) + ' euros.')


def show_transaction_history():
    for transaction in transaction_history:
        print(transaction.type + ' - ' + transaction.category + ' - ' + str(transaction.amount))


