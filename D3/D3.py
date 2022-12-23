#Treasure Island

print('Welcome to Treasue Island!\nYour mission is to find treasure.')
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
if choice1 == 'right':
    print('You fell into a whole. Game over.')
elif choice1 == 'left':
    choice2 = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice2 == 'swim':
        print('You got attacked by an angry trout.')
    elif choice2 == 'wait':
        choice3 = input('You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Which color do you choose?\n').lower()
        if choice3 == 'red':
            print('It\'s a room full of fire. Game over.')
        elif choice3 == 'yellow':
            print('You\'ve reached to the treasure unharmed. You win!\n Claim your reward.')
        elif choice3 == 'blue':
            print('You\ve reached a room of beasts. Gave over.')
        else:
            print('Wrong input')
    else:
        print('Wrong input')
else:
    print('Wrong input')
        
        
    
    
