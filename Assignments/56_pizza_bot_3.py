
from time import sleep
from os import system, name


meat_options = ["Pepperoni", "Salami", "Grilled Chicken", "Spicy Italian Sausage", "Canadian Bacon", "Philly Steak", "Meatball", "Beef", "Bacon", "Sausage", "None"]
non_meat_options = ["Green Olives", "Black Olives", "Roma Tomatoes", "Green Peppers", "Jalapeno Peppers", "Mushrooms", "Banana Peppers", "Onions", "Pineapple", "Fresh Spinach", "None"]


final_pizza = []



def clearConsole():

    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')



def print_slow(txt):
    for x in txt:                    
        print(x, end='', flush=True) 
        sleep(0.03)
    print()



def greeting():
    print_slow("Welcome to Via Napoli Ristorante e Pizzeria")


def selectSize():
    print_slow("What size can I get for you? A Small, Medium, Large or Family?")
    size_choice = input("Enter size: ").lower()
    if size_choice == "small":
        final_pizza.append(size_choice)
    elif size_choice == "medium":
        final_pizza.append(size_choice)
    elif size_choice == "large":
        final_pizza.append(size_choice)
    elif size_choice == "family":
        final_pizza.append(size_choice)
    else:
        print("That size is not in out database! Please select a size.")
        selectSize()
    
def selectCrust():
    print_slow("What crust type can I get for you? Original, Thin or Gluten-Free?")
    crust_choice = input("Enter type: ").lower()
    if crust_choice == "original":
        final_pizza.append(crust_choice)
    elif crust_choice == "thin":
        final_pizza.append(crust_choice)
    elif crust_choice == "gluten-free" or crust_choice == "glutenfree":
        final_pizza.append(crust_choice)
    else:
        print("That type is not in out database! Please select a type.")
        selectCrust()

def selectCut():
    print_slow("What cut type can I get for you? Normal cut, Square cut or No cut?")
    cut_choice = input("Enter cut: ").lower()
    if cut_choice == "normal cut" or cut_choice == "normal":
        final_pizza.append(cut_choice)
    elif cut_choice == "square cut" or cut_choice == "square":
        final_pizza.append(cut_choice)
    elif cut_choice == "no cut" or cut_choice == "no":
        final_pizza.append(cut_choice)
    else:
        print("That cut is not in out database! Please select a cut.")
        selectCut()

def selectSauce():
    print_slow("Which sauce can I get for you? Original Sauce, Buffalo Sauce, Alfredo Sauce, BBQ Sauce or Ranch Sauce?")
    sauce_choice = input("Enter sauce: ").lower()
    if sauce_choice == "original sauce" or sauce_choice == "original":
        final_pizza.append(sauce_choice)
    elif sauce_choice == "buffalo sauce" or sauce_choice == "buffalo":
        final_pizza.append(sauce_choice)
    elif sauce_choice == "alfredo sauce" or sauce_choice == "alfredo":
        final_pizza.append(sauce_choice)
    elif sauce_choice == "bbq sauce" or sauce_choice == "bbq":
        final_pizza.append(sauce_choice)
    elif sauce_choice == "ranch sauce" or sauce_choice == "ranch":
        final_pizza.append(sauce_choice)
    else:
        print("We don't have that amount saved! Please try again.")
        selectSauce()

def selectSauceVolume():
    print_slow("How much sauce can I get for you? Normal Sauce, Light Sauce or Heavy Sauce?")
    sauce_volume_choice = input("Enter sauce: ").lower()
    if sauce_volume_choice == "normal sauce" or sauce_volume_choice == "normal":
        final_pizza.append(sauce_volume_choice)
    elif sauce_volume_choice == "light sauce" or sauce_volume_choice == "light":
        final_pizza.append(sauce_volume_choice)
    elif sauce_volume_choice == "heavy sauce" or sauce_volume_choice == "heavy":
        final_pizza.append(sauce_volume_choice)
    else:
        print("We don't have that amount saved! Please try again.")
        selectSauceVolume()

def selectCheese():
    print_slow("What cheese type can I get for you? 3-cheese blend, 5-cheese blend, Original Mozzarella or Parmesan Romano?")
    cheese_choice = input("Enter cheese: ").lower()
    if cheese_choice == "3-cheese" or cheese_choice == "3-cheese blend":
        final_pizza.append(cheese_choice)
    elif cheese_choice == "5-cheese" or cheese_choice == "3-cheese blend":
        final_pizza.append(cheese_choice)
    elif cheese_choice == "original mozzarella" or cheese_choice == "originalmozzarella":
        final_pizza.append(cheese_choice)
    elif cheese_choice == "parmesan romano" or cheese_choice == "parmesanromano":
        final_pizza.append(cheese_choice)
    else:
        print("That sauce is not in out database! Please select a sauce.")
        selectSauce()


def selectMeat():
    meat_choices = []

    print_slow("What meats type can I get for you? Please enter 1 below") 
    print("Current options are: ", meat_options)



    meat_choice = input("Enter a meat type: ").title()
    if meat_choice in meat_options:
        meat_choices.append(meat_choice)


        print("Would you like another? Y or N?")
        meat_choice_yn = input(" ").lower()
        if meat_choice_yn == "y":
            selectMeat()  
        elif meat_choice_yn == "n":
            final_pizza.append(meat_choices)  

 

def selectNonMeat():
    non_meat_choices = []

    print_slow("What non-meat types can I get for you? Please enter your first meat choice below") 
    print("Current options are: ", non_meat_options)

    non_meat_choice = input("Enter a non meat type: ").title()
    if non_meat_choice in non_meat_options:
        non_meat_choices.append(non_meat_choice)
    else:
        print_slow("We don't have that meat in out database?")
    print("Would you like another? Y or N?")
    non_meat_choice_yn = input(" ").lower()
    if non_meat_choice_yn == "y":
        selectNonMeat()
    else:
        final_pizza.append(non_meat_choices)

def getAddress():
    print_slow("You chose to have the order delivered! Please enter your address below: ")
    address = input("Enter Address ")
    final_pizza.append(address)


def selectDelivery():
    print_slow("Would you like this order delivered? Type Yes or No to choose")
    delivery_select = input().lower()
    if delivery_select == "yes":
        getAddress()
    else:
        return

def finalOrder():
    print_slow("Does this look correct?")
    print(final_pizza) #Add thing here
    order_y_n = input("Would you like to confirm your order? (y/n): ").lower()

    if order_y_n == "y":
        print("Your order is currently being prepared!")
    else:
        print("Your order will reset.")
        sleep(2)
        final_pizza.clear()
        
        orderPizza()


    
def orderPizza():
    greeting()
    clearConsole()
    selectSize()
    clearConsole()
    selectCrust()
    clearConsole()
    selectCut()
    clearConsole()
    selectSauce()
    clearConsole()
    selectSauceVolume()
    clearConsole()
    selectMeat()
    clearConsole()
    selectNonMeat()
    clearConsole()
    selectDelivery()
    clearConsole()
    finalOrder()

finalOrder()