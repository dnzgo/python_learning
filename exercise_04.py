pin = 123456
count = 0

while count < 3:
    user_input = int(input('enter your pin'))
    count += 1
    if user_input == pin:
        print('you logged in')
        break
    else:
        print('Wrong!')
if count == 3:
    print('you are blocked')