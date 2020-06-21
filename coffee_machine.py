def remaining():
    result = "The coffee machine has:\n{0} of water\n{1} of milk\n{2} of coffee beans\n{3} of disposable cups\n{4} of money"
    result_format  = result.format(coffee[0], coffee[1], coffee[2], coffee[3], coffee[4])
    print(result_format)

def buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    nested_command = input()
    coffee[3] = disposable_cups - 1
    if coffee[3] > 1:
        if nested_command == "1": 
            buy_espresso()
        elif nested_command == "2":
            buy_latte()
        elif nested_command == "3":
            buy_cappuccino()
        elif nested_command == "back":
            pass
        else:
            print("Wrong command!")
            

            
    else:
        print("Sorry, not enough disposable cups!")
                          
def buy_espresso():
    if coffee[0] >= 250 and coffee[2] >= 16:
        print("I have enough resources, making you a coffee!")
        coffee[4] = money + 4
        coffee[0] = water - 250
        coffee[2] = coffee_beans - 16
    elif coffee[0] < 250 and coffee[2] < 16:
        print("Sorry, not enough water and coffee beans!")
    elif coffee[0] < 250:
        print("Sorry, not enough water!")
    else:
        print("Sorry, not enough coffee beans!")        
    
def buy_latte():
    if coffee[0] >= 350 and coffee[2] >= 20 and coffee[1] >= 75:
        print("I have enough resources, making you a coffee!")
        coffee[4] = money + 7
        coffee[0] = water - 350
        coffee[1] = milk - 75
        coffee[2] = coffee_beans - 20
    elif coffee[0] < 350 :
        print("Sorry, not enough water")
    elif coffee[1] < 75 :
        print("Sorry, not enough milk!")
    else:
        print("Sorry, not enough coffee beans!")       

def buy_cappuccino():
    if coffee[0] >= 200 and coffee[2] >= 12 and coffee[1] >= 100:
        print("I have enough resources, making you a coffee!")
        coffee[4] = money + 6
        coffee[0] = water - 200
        coffee[1] = milk - 100
        coffee[2] = coffee_beans - 12 
    elif coffee[0] < 200 :
        print("Sorry, not enough water")
    elif coffee[1] < 100 :
        print("Sorry, not enough milk!")
    else:
        print("Sorry, not enough coffee beans!")
        
def fill():
    print("Write how many ml of water do you want to add:")
    water_add = int(input())

    print("Write how many ml of milk do you want to add:")
    milk_add = int(input())

    print("Write how many grams of coffee beans do you want to add:")
    coffee_beans_add = int(input())

    print("Write how many disposable cups of coffee do you want to add:")
    disposable_cups_add = int(input())
   
    coffee[0] = water + water_add
    coffee[1] = milk + milk_add
    coffee[2] = coffee_beans + coffee_beans_add 
    coffee[3] = disposable_cups + disposable_cups_add

def take():
    print("I gave you ${0}".format(coffee[4]))
    coffee[4] = 0

water = 400
milk = 540
coffee_beans = 120 
disposable_cups = 9 
money = 550

coffee = [water, milk, coffee_beans, disposable_cups, money]

while True:
    print("Write action (buy, fill, take, remaining, exit):")
    command = input()
    print()
    if command == "buy":
        buy()
    elif command == "fill":
        fill()    
    elif command == "take":
        take()
    elif command == "remaining":
        remaining()
    elif command == "exit":
        break    
    else: 
        print("Wrong command!")

















