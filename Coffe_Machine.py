from data import MENU,resources
yn = False


def count_coins():
    print("Please insert coins: ")
    q = int(input("how many quarters? "))
    d = int(input("how many dimes? "))
    n = int(input("how many nickles? "))
    p = int(input("how many pennies? "))
    s = 0.25*q + 0.10*d + 0.05*n + 0.01*p
    return s


def res(us_c):
    p=0
    if us_c == 'espresso':
        if resources['water'] >= MENU[us_c]['ingredients']['water'] and resources['coffee'] >= MENU[us_c]['ingredients']['coffee']:
            resources['water'] = resources['water'] - MENU[us_c]['ingredients']['water']
            resources['coffee'] = resources['coffee'] - MENU[us_c]['ingredients']['coffee']
            print(f"Here is your {us_c}! Enjoy: ")
            p = 1

        else:
            print("Sorry! Not enough resources")
    else:
        if resources['water'] >= MENU[us_c]['ingredients']['water'] and resources['coffee'] >= MENU[us_c]['ingredients']['coffee'] and resources['milk'] >= MENU[us_c]['ingredients']['milk']:
            resources['water'] = resources['water'] - MENU[us_c]['ingredients']['water']
            resources['coffee'] = resources['coffee'] - MENU[us_c]['ingredients']['coffee']
            resources['milk'] = resources['milk'] - MENU[us_c]['ingredients']['milk']
            print(f"Here is your {us_c}! Enjoy: ")
            p = 1
        else:
            print("Sorry! Not enough resources")
    return p


while not yn:
    c = 0.0
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'report':
        for i in resources:
            print(f"{i}={resources[i]}")
    elif user_choice == 'latte' or user_choice == 'cappuccino':
        c = count_coins()
        if c >= MENU[user_choice]['cost']:
            m = res(user_choice)
            if m == 1:
                c = c - MENU[user_choice]['cost']
                print(f"Here is ${c} in change. ")
            else:
                print(f" Money refunded :  {c}")

        else:
            print("Sorry! that's not enough money. ")
            yn = True
    else:
        print("Invalid entry!")
