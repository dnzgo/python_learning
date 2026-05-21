import tracker

while True:
    print("""
1 - add income
2 - add expense
3 - show balance
4 - show transaction history
5 - exit
        """)
    choice = input('Select: ')

    if choice == '1':
        amount = float(input('Enter income amount: '))
        category = input('Enter a category for income: ')

        if amount <= 0:
            amount = float(input('Please enter a valid amount'))
        
        if amount > 0:
            tracker.add_income(amount, category.lower())

    elif choice == '2':
        amount = float(input('Enter expense amount: '))
        category = input('Enter a category for expense: ')

        if amount == 0:
            amount = float(input('Please Enter valid amount: '))

        if amount != 0:
            if amount < 0:
                amount *= -1
            tracker.add_expense(amount, category)
    
    elif choice == '3':
        tracker.show_balance()
    
    elif choice == '4':
        tracker.show_transaction_history()

    elif choice == '5':
        print('you quit')
        break

    else:
        print('Invalid number')
    