magicians = ['alice', 'david', 'carolina']

for magician in magicians: # do the following code for every element in the list
    print(magician)
    print(magician.title() + ', that was a great trick!')
print('thanks for the show')

pizzas = ['pepperoni', 'sucuk', 'mashroom']
for pizza in pizzas:
    print('I like ' + pizza + ' pizza')
print('I really like pizza!')

for i in range(1, 5): # first argument included, last exculuded
    print(i)

numbers = list(range(1, 5)) # making a list of numbers using range function
print(numbers)

even_numbers = list(range(2, 11, 2)) # creating a number list with step
print(even_numbers)

squares = []
for i in range(1, 11):
    squares.append(i**2)          # 2 asterisks = exponent
    
print(squares)
print(min(squares)) # min value of the list
print(max(squares)) # max value of the list
print(sum(squares)) # sum of values in the list

cubes = [value**3 for value in range(1, 11)] # list comprehension combines for loop and creation of new elements
print(cubes)

# slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) # slicing a list 0:3 -> start from 0 until 3(excluded) 
print(players[:3]) # slicing a list :3 -> start from 0 until 3(excluded) same as 0:3
print(players[2:]) # slicing a list 2: -> start from 2 until end
print(players[-3:]) # last 3 element

for player in players[:3]: # looping through slice
    print(player)

# creating a copy of a list
new_players = players[:] # creates a new list when we change players list does not effect the new_players list. but if we write new_players = players this does not create a new list, instead two varible points to same list


# exercise
print(numbers[:3]) # first 3 items
print(numbers[1:3]) # middle items
print(numbers[-2:]) # last 2 items

friends_pizzas = pizzas[:]
pizzas.append('margarita')
friends_pizzas.append('salami')

print('my favorite pizzas are:')
for pizza in pizzas:
    print(pizza)
print('my friends favorite pizzas are:')
for pizza in friends_pizzas:
    print(pizza)