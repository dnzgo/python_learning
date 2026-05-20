import random

player_data = {'money' : 100, 'energy' : 0, 'apples' : 0, 'swords' : 0}

while True:
    print(player_data)
    print('eat apple/ buy apples/ buy sword / work / fight')
    player_input = input('what do u want to do').lower()
    
    if player_input == 'buy apple':
        apples = int(input('how many apples do u want to buy? '))
        if player_data['money'] >= apples * 5:
            player_data['money'] -= apples * 5
            player_data['apples'] += apples
        else:
            print('u do not have enough money to buy ' + str(apples) + ' apples')
    elif player_input == 'eat apple':
        if player_data['apples'] >= 1:
            player_data['energy'] += 2
            player_data['apples'] -= 1
        else:
            print(' u do not have any apples')
    elif player_input == 'buy sword':
        if player_data['money'] >= 50 and player_data['swords'] == 0:
            player_data['swords'] = 1
            player_data['money'] -= 50
        else:
            if player_data['money'] < 50:
                print('u do not have enough money')
            if player_data['swords'] == 1:
                print('u already have a sword, u can not buy anymore')
    elif player_input == 'work':
        if player_data['energy'] >= 2:
            player_data['energy'] -= 2
            player_data['money'] += 20
        else:
            print('u are so tired to work')
    elif player_input == 'fight':
        if player_data['swords'] >= 1 and player_data['energy'] >= 3:
            outcome = random.choice(['win', 'lose'])
            reward_chance = random.randint(1, 100)
            player_data['energy'] -= 2
            if outcome == 'win':
                player_data['money'] += 40
                print('you gained 40 euros')
            else:
                player_data['money'] -= 30
                print('you lost 30 euros')
            if reward_chance <= 10:
                print('monster dropped treasure')
                player_data['money'] += 100
        else:
            print('u do not have enough sources to fight')
    elif player_input == 'quit':
        break
            
            