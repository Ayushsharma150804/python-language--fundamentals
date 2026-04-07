#*****************coffee machine project**********************************
#two ways of solution is available here
#way one-user define function is less
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def checking(order_ingredients):
    global resources
    for item in order_ingredients:
        if order_ingredients[item]>resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def coin_collector():
    total_coin = int(input("quarters : $"))*0.25
    total_coin += int(input("dimes : $"))*0.10
    total_coin += int(input("nickles : $"))*0.05
    total_coin += int(input("pennies : $"))*0.01
    return total_coin

def chek_transection(resource_amount, credit_amount):
    global resources
    if credit_amount >= resource_amount:
        change = round(credit_amount-resource_amount,2)
        global ACCOUNT
        print(f"keep the change ${change}.Enjoy!")
        ACCOUNT += resource_amount
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(selected_item, drink_name):
    global resources
    for items in selected_item:
        resources[items] -= selected_item[items]
    print(f"Here is your {drink_name} ☕️.Enjoy!")

ACCOUNT=0
Flag =True

while Flag:
    SELECT = input("What would you like? (espresso/latte/cappuccino):")
    if SELECT=="report":
        print(resources)
    elif SELECT=="off":
        print("machine get tur off")
        Flag=False
    else:
        typer = MENU[SELECT]
        if checking(typer["ingredients"]):
            credit = coin_collector()
            if chek_transection(typer["cost"], credit):
                make_coffee(typer["ingredients"], SELECT)





#**************way-2 more user define function is available**************
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
