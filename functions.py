def great_user(username):
    """display a simple greating"""
    print('Hello ' + username)

great_user('Deniz')

def describe_pet(animal_type, animal_name):
    print('I have a ' + animal_type)
    print('my ' + animal_type + "'s name is " + animal_name.title())

describe_pet('dog', 'karabas')