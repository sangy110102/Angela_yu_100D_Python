#Blackjacket/21 Program

import random
from turtle import clear

def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    chosen_card = random.choice(cards)
    return chosen_card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)        
    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return 'Draw'
    elif computer_score == 0:
        return 'Lose, opponent has blackjack'
    elif user_score == 0:
        return 'Win with a blackjack'
    elif user_score > 21:
        return 'You went over, you lose'
    elif computer_score > 21:
        return 'Opponent went over, you win'
    elif user_score > computer_score:
        return 'You win'
    else:
        return 'You lose'


def play_game():
    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    is_game_over = False

    while not is_game_over: 
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'Your cards are {user_cards} and your card score is {user_score}\nComputer\'s first card are {computer_cards[0]}')

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass : ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
                print(f'Your cards are {user_cards} and your score is {calculate_score(user_cards)}')
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
        
    print(compare(user_score,computer_score))
    
print("Blackjack Game")    
play_game()

while input('Do you wanna play blackjack game again?(y) ') == 'y':
    play_game()