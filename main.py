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
resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resource[item]:
            print(f"Sorry no enough {item}.")
            return False
        return True


def process_coins():
    print("Please enter the coins")
    total = int(input("how many quaters:")) * 0.25
    total += int(input("how many dimes:")) * 0.10
    total += int(input("how many nickles:")) * 0.05
    total += int(input("how many pennies:")) * 0.01
    return total


def is_transaction_succesful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here the change ${change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry not enough money, return money")
        return False


def make_coffee(drink_name, order_ingredients):
    for items in order_ingredients:
        resource[items] -= order_ingredients[items]
    print(f"enjoy the coffee {drink_name} ☕")


profit = 0
is_on = True
while is_on:
    choice = input("which type of coffee : espresso, latte, cappuccino\n")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water : {resource['water']}ml")
        print(f"milk : {resource['milk']}ml")
        print(f"coffee : {resource['coffee']}ml")
        print(f"profit: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_succesful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

# print(f"menu:{MENU['latte']}")
