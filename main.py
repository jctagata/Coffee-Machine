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

def printReport():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${profit}")


def is_resource_sufficient(order_ingredients):
    """Returns True if the resources are sufficient to fulfill the drink.
    Returns False if at least one ingredient is insufficient."""
    #Loop through the ingredients data dictionary
    #item = dictionary key
    is_enough = True

    #The value of is_enough only changes if the ingredient from order_ingredients
    #is greater than the available resources. If this function reaches the end of 
    #the For-Loop without any change in is_enough, then return the original value
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there's not enough {item}.")
            is_enough = False
    
    #End of the For Loop
    return is_enough


def process_coins():
    """Returns the total amount calculated from the coins inserted.
    This function will accept four types of coins sequentially."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickel?: ")) * 0.05
    total += int(input("how many quarters?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True if the payment is accepted. Return False if the money is insufficient"""
    if money_received > drink_cost:

        change = round(money_received - drink_cost, 2)
        print(f"Payment accepted. Change: {change}")

        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, not enough money received. Refunding...")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients form the resources."""
    for item in order_ingredients:
        #For each item in the order ingredients dictionary, subtract from the resources dictionary
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Have a great day!")


def coffee_machine():
    is_On = True

    while is_On:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if choice == "off":
            is_On = False
        elif choice == "report":
            printReport()
        else:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])


coffee_machine()
