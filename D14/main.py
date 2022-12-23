#Higher or Lower Game

from art import logo,vs
from game_data import data
import random

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}."

def check_answer(guess,account_a,account_b):
    if account_a["follower_count"] > account_b["follower_count"]:
        return guess == "a"
    else:
        return guess == "b"
        

print(logo)
score = 0
continue_game = True
account_b = random.choice(data)

while continue_game:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A : {format_data(account_a)}")
    print(vs)
    print(f"Against B : {format_data(account_b)}")

    guess = input("Who has more followers? Type A or Type B : ").lower()
    
    is_correct = check_answer(guess,account_a,account_b)

    if is_correct:
        score+=1
        print(f"You're right. Correct score : {score}")
    else:
        print(f"Sorry, you're wrong. Final score : {score}")
        continue_game = False
