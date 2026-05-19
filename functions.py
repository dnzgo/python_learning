def great_user(username):
    """display a simple greating"""
    print('Hello ' + username)

great_user('Deniz')

def describe_pet(animal_type, animal_name = 'fino'): #default values
    print('I have a ' + animal_type)
    print('my ' + animal_type + "'s name is " + animal_name.title())

describe_pet('dog', 'karabas')

describe_pet(animal_name= 'kara', animal_type= 'cat') # telling which parameter match with which argument (keyword arguments)

def sum(a, b):
    return float(a) + float(b) # returning a value

print(sum(12, 23))

def get_formatted_name(first_name, last_name, middle_name = ''): # making an arg optional
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

print(get_formatted_name('deniz', 'gozcu'))

def make_pizza(*toppings): # asterisks creates a tupple and packs whatever values it receives
    print(toppings)

make_pizza('pepperoni', 'margaritha')
make_pizza('sucuk')

def build_profile(first_name, last_name, **user_info): # ** creates an empty dictionary 
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first_name
    profile['last_name'] = last_name
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('deniz', 'gozcu', location= 'berlin', field= 'computer sciences')
print(user_profile)

