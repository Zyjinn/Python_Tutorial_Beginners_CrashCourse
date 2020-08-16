# Vars player
player_name = "Nick"
player_attack = 10
player_heal = 12
player_health = 100

# List
# player_info = [player_name, player_attack, player_heal, player_health]

# Dictionary
player_info = {'name': player_name, 'attack': player_attack, 'heal': player_heal, 'health': player_health}
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

    # Check if player is dead
    if player_info['health'] <= 0:
        game_running = False
        print(player_info['name'] + " has died, game over!")
    
    # Attack the monster
    if player_selection == '1': 
        # PLayer attacks 
        print(player_info['name'] + " attacks " + monster_info['name'])

        # Deal damage to the monster, equal to hp - player_attack
        monster_info['health'] = monster_info['health'] -  player_info['attack']

        # Print how much monster has remaining
        print(monster_info['name'] + " Has " + str(monster_info['health']) + " health remaining")

    # Heal
    elif player_selection == '2':
        # Player heals
        print(player_info['name'] + " Heals themself for " + str(player_info['heal'])+ 'hp')

    # Else, invalid input, error
    else: 
        print('input invalid')

    # Monster Attacks
    print(monster_info['name'] + " attacks " + player_info['name'] + " and deals " + str(monster_info['attack']) + " damage")

    # Subtract monster attack from player hp
    player_info['health'] -= monster_info['attack']
    print(player_info['name'] + ' has ' + str(player_info['health']) + ' health remaining')

    # Check if player is dead
    if player_info['health'] <= 0:
        game_running = False
        print(player_info['name'] + " has died, game over!")

    # Check monster has died
    if monster_info['health'] <= 0:
        game_running = False
        print(monster_info['name'] + " has been defeated!")

# Print information of player
print(player_info)
