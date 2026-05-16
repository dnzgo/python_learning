alien_0 = {'color' : 'green', 
           'points' : 5
           } # {key : value}
print(alien_0['color'])

alien_0['x_pos'] = 25  # adding a new key-value pair to dictionary
alien_0['y_pos'] = 100
print(alien_0)

alien_1 = {} # starting with empty dictionary
alien_1['color'] = 'red'
alien_1['points'] = 25
alien_1['x_pos'] = 0
alien_1['y_pos'] = 10
print(alien_1)

alien_0['color'] = 'yellow' # modifying value

alien_0['speed'] = 'medium'
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_pos'] += x_increment
print(alien_0['x_pos'])

del alien_0['y_pos']  # remove a key-value pair

# exercise
person = {'first_name' : 'deniz', 'last_name' : 'gozcu', 'age' : 25, 'city' : 'berlin'}

for key, value in person.items(): 
    print('\nKey: ' + key)
    print('\nValue: ' + str(value))

for key in sorted(person.keys()):    #  can sort the keys. access just keys with keys() method, values with values() method
    print('key name: ' + key)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for language in set(favorite_languages.values()): # set(), python identifies the unique items in the list and builds a set from those items
    print(language.title())

aliens = []
for i in range(30):
    new_alien = {'color' : 'green', 'point' : 5, 'speed' : 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['point'] = 10
        alien['speed'] = 'medium'

print(aliens[:5])