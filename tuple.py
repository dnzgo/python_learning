# immutable lists
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0] = 100 can not be done because tuples immutable

for dimension in dimensions:
    print(dimension)

# redefine entire tuple is allowed
dimension = (100, 20)