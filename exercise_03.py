number = 100
count = 1
prediction = input('enter your prediction')

while int(prediction) != number:
    if number < int(prediction):
        print('too high')
    elif number > int(prediction):
        print('too low')
    prediction = input('try again: ')
    count += 1
print('you found the number')
print('you guessed in ' + str(count) + ' tries')