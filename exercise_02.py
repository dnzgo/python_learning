user_data = {'username' : 'deniz', 'password' : '12345'}

user_input = input('password: ')

while user_input != user_data['password']:
    user_input = input('Wrong! password again: ')
print('you loged in!')