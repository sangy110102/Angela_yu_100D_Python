#Coffee Machine

from menu import MENU, resources

is_on = True
profit = 0

def is_resourse_sufficient(drink):
    for item in drink:
        if drink[item] >= resources[item]:
            print(f"Sorry, Not enough ingredients...")
            return False
    return True

def process_coins():
    print("Please insert coins...")
    total = int(input("How many quarters? : ")) * 0.25
    total += int(input("How many dimes? : ")) * 0.1
    total += int(input("How many nickles? : ")) * 0.05
    total += int(input("How many pennies? : ")) * 0.01
    return total

def make_coffee(drink_name,drink):
    for item in drink:
        resources[item] -= drink[item]
    print(f"Here is your {drink_name}")

def is_transaction(money_received,drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that not enough money. Money refunded.")
        return False


while is_on:
    choice = input("What would you like? (Expresso/Latte/Cappuccino): ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}ml")
        print(f"Money : ${profit}")
    else:
        drink = MENU[choice]
        if is_resourse_sufficient(drink["ingredients"]):
            payment = process_coins()
            is_transaction(payment,drink["cost"])
            make_coffee(choice,drink["ingredients"])