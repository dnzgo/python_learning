cars = ['audi', 'bmw', 'mercedes', 'toyota']
for car in cars:
    if car == 'bmw':      # == equality check, != inequality
        print(car.upper())
    else:
        print(car.title())

age = 17
if age != 20:
    print('u are very young')

if age > 15 and age < 25: # using multiple conditions with and both conditions must be true, with or at least one of them should be true
    print('u are young')

if age >= 18:
    print('u are old enough to vote')
else:
    print('sorry u r too young to vote')

toppings = ['mashroom', 'onion', 'pineapple']
print('mashroom' in toppings) # check whether a value is in list
print('peperoni' in toppings)

banned_users = ['deniz', 'emir', 'andrew']
user = 'marie'
if user not in banned_users:     # check wheter a value is not in list
    print(user.title() + ', u can play')

passenger_age = 12
if passenger_age < 4:
    price = 0
elif passenger_age < 18:
    price = 10
elif passenger_age < 65:
    price = 20
else:
    price = 5
print('your ticket costs ' + str(price )+ ' dollar.')

# exercise
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

alien_color = 'yellow'
if alien_color == 'green':
    point = 5
elif alien_color == 'yellow':
    point = 10
else:
    point = 25
print('you just earn ' + str(point) + ' points')

person_age = 19
if person_age < 2:
    print('baby')
elif person_age >= 2 and person_age < 4:
    print('toddler')
elif person_age >= 4 and person_age < 13:
    print('kid')
elif person_age >= 13 and person_age < 20:
    print('teenager')
elif person_age >= 20 and person_age < 65:
    print('adult')
elif person_age >= 65:
    print('elder')

if cars:            # checking if a list is not empty
    for car in cars:
        print(car)
else:
    print('there is no car')

avaible_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in avaible_toppings:
        print('Adding ' + requested_topping + '.')
    else:
        print('Sorry, we do not have ' + requested_topping + '.')
print("\nFinished making your pizza")