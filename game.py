# Vars player
player_name = "Nick"
player_attack = 10
player_heal = 12
player_health = 100

# Create player info (dictionary)
player_info = {'name': player_name, 'attack': player_attack, 'heal': player_heal, 'health': player_health}

# Print information of player
print(player_info)

# Create monster
monster_info = {'name': 'Jake', 'attack': 15, 'health': 100}

# Define var to keep game running
game_running = True
monster_won = False
player_won = False

while game_running == True:
    # Print Battle options menu
    print('Please select an action')
    print('1) Attack')
    print('2) Heal')

    # Get input from user
    player_selection = input()
    # Check player choice
    
    # Attack the monster
    if player_selection == '1': 
        # Check if player dead
        if(player_info['health'] <= 0):
            monster_won = True

        else: 
            # Player attacks 
            print(player_info['name'] + " attacks " + monster_info['name'])

            # Deal damage to the monster, equal to hp - player_attack
            monster_info['health'] = monster_info['health'] -  player_info['attack']

            # Print how much monster has remaining
            print(monster_info['name'] + " Has " + str(monster_info['health']) + " health remaining")

    # Player Heals
    elif player_selection == '2':
        # Check if player is dead
        if(player_info['health'] <= 0):
            monster_won = True

        # Player heals
        else:
            print(player_info['name'] + " Heals themself for " + str(player_info['heal'])+ 'hp')

    # Else, invalid input, error
    else: 
        print('input invalid')

    # Check if monster is defeated
    if monster_info['health'] <= 0:
        player_won = True

    else:
        # Monster Attacks
        print(monster_info['name'] + " attacks " + player_info['name'] + " and deals " + str(monster_info['attack']) + " damage")

        # Subtract monster attack from player hp
        player_info['health'] -= monster_info['attack']
        print(player_info['name'] + ' has ' + str(player_info['health']) + ' health remaining')
    
    # check if player or monster has died 
    if player_info['health'] <= 0:
        monster_won = True
    if monster_info['health'] <= 0:
        player_won = True

    # Check if player or monster has won
    if player_won == True or monster_won == True:
        if player_won == True:
            print(player_info['name'] + " Has defeated the monster!")
        if monster_won == True:
            print(player_info['name'] + " Has been defeated")
        game_running = False

    # If no, keep running game
    else: 
        pass


