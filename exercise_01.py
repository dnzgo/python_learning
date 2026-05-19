product_prices = {'apple' : 2.50, 'pineapple' : 5.05, 'watermelon' : 2}

done = 'y'
total = 0
while done.lower() == 'y':
    new_product = input('what do you want to add? ')
    if new_product.lower() == 'apple':
        total += product_prices['apple']
    elif new_product.lower() == 'pineapple':
        total += product_prices['pineapple']
    elif new_product.lower() == 'watermelon':
        total += product_prices['watermelon']
    else:
        print('we do not have that product')
    done = input('do you want to continue adding new product? (y/n) ')
print('your total is ' + str(total))
