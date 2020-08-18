# Default player values
player_name = "Nick"
player_attack = 10
player_heal = 12
player_health = 100

# Create player info default values (dictionary)
player_info = {'name': player_name, 'attack': player_attack, 'heal': player_heal, 'health': player_health}

# Create monster default values
monster_info = {'name': 'Jake', 'attack_min': 10, 'attack_max': 15, 'health': 100}

# Define var to keep game running
game_running = True
monster_won = False
player_won = False

# Game continuation loop
while game_running == True:
    # Get player name
    print('------' * 12) # Print a line of dashes
    print("Enter your name!")
    player_name = input()

    # set values for player
    player_info = {'name': player_name, 'attack': player_attack, 'heal': player_heal, 'health': player_health}

    # Create monster
    monster_info = {'name': 'Jake', 'attack': 15, 'health': 100}

    # Greet player
    print("Hello " + player_info['name'] + "\n")

    # Print player info
    print(str(player_info['name']) + " has " + str(player_info['health']) + "hp " + str(player_info['attack']) + " attack and heals " + str(player_info['heal']) + "hp")

    # Battle round continuation loop
    new_round = True
    while new_round == True: 
        # Battle Options
        print('Please select an action')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit')

        # Get input from user
        player_selection = input()
        # Check player choice

        if player_info['health'] <= 0:
            monster_won = True 

        # Attack the monster
        if player_selection == '1' and monster_won == False: 
            # Player attacks 
            print(player_info['name'] + " attacks " + monster_info['name'])

            # Deal damage to the monster, equal to hp - player_attack
            monster_info['health'] = monster_info['health'] -  player_info['attack']

            # Print how much monster has remaining
            print(monster_info['name'] + " Has " + str(monster_info['health']) + " health remaining")

        # Player heals
        elif player_selection == '2' and monster_won == False:
            print(player_info['name'] + " Heals themself for " + str(player_info['heal'])+ 'hp')
            player_info['health'] += player_info['heal'] # add heal value to player HP
        
        # Player exits the game
        elif player_selection == '3':
            game_running = False
            new_round = False

        # Else, invalid input, error
        else: 
            print('input invalid')

        # Check if monster is defeated
        if monster_info['health'] <= 0 and new_round == True:
            player_won = True

        elif new_round == True:
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
                print("\n**" + player_info['name'] + " Has defeated the monster!" "**\n")
            if monster_won == True:
                print("\n**" + player_info['name'] + " Has been defeated" + "**\n")
            # End battle
            new_round = False
        

# Game is over
print("Thanks for playing my game! \n ")

