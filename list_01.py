bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles) # prints representation of the list inc. brackets

print(bicycles[0]) # prints first element of the list

print(bicycles[1].title()) # title makes the elements first letter capital

print(bicycles[-1]) # python speacial last element access 

message = "my bicycle is a " + bicycles[2].title() + "."
print(message) #using individual value from the list

#Exercise
names = ["Deniz", "Serkan", "Azad", "Alper"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])

message = "Hello, "
print(message + names[0])
print(message + names[1])
print(message + names[2])
print(message + names[3])

motorcycles = ["honda", "yamaha", "suziki"]
print(motorcycles)
motorcycles[0] = "ducati" # changing an element of the list
print(motorcycles)

motorcycles.append("honda") # adding a new element to the end of the list
print(motorcycles)

motorcycles.insert(2, "kuba") # adding a new element to the list by specifying the index and the value
print(motorcycles)

del motorcycles[1] # removing an element from known position
print(motorcycles)

popped_motorcycle = motorcycles.pop() # pop(remove) a value from the list and store(pop lets to do that) that value in the variable
print(motorcycles)
print(popped_motorcycle)

motorcycles.pop(0) # remove an element at a position with giving an int to pop method
print(motorcycles)

motorcycles.remove("kuba")  # remove an element at unknown index by giving value of element to remove method
print(motorcycles)


