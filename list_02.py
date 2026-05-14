# sorting lists
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # sort elements of the list alphabetically a-z, changes order permanently
print(cars)
cars.sort(reverse= True) # sorts reverse alphabetically z-a
print(cars)

print(sorted(cars)) # sorts the list temporarily does not affect the original list
print(cars)

cars.reverse() # reverse order of the list (no alphabetical order just order)
print(cars)

print(len(cars)) # the lenght of a list with len() function
