import json

username = input('What is your name? ')
filename = 'username.json'

with open(filename, 'w') as f_obj: # write to file
    json.dump(username, f_obj)
    print('we will remember u when u come back ' + username + '!')

with open(filename) as f_obj: # read from file
    username_infile = json.load(f_obj)
    print('welcome back ' + username_infile + '!')