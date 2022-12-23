#Number guessing game
from random import randint


def set_dificulty():
    level = input('Ente the dificuilty level : easy or hard ').lower()
    if(level == 'easy'):
        attempt = 10
    else:
        attempt = 5
    return attempt
    
def check_answer(guessed_number,chosen_number,turns):
    if(guessed_number > chosen_number):
        print('Too High')
        return (turns-1) 
    elif(guessed_number < chosen_number):
        print('Too Low')
        return (turns-1)
    else:
        print('you\'ve guessed correct!!!\nYou win!!!')
    return (turns)
        
print('Think of a number between 1 and 100 :')
chosen_number = randint(1,100);
turns = set_dificulty()
while turns > 0:
    print(f'you\'ve {turns} attempts now')
    guessed_number = int(input('Make a guess : '))
    turns = check_answer(guessed_number,chosen_number,turns)
    if chosen_number == guessed_number :
        print(f'You won by {turns}!?')
        break;
    
if(turns == 0 and guessed_number != chosen_number):
    print('You lose!!!')