from time import sleep
from os import system, name
import random

def print_slow(txt):
    for x in txt:            
        print(x, end='', flush=True)  
        sleep(0.1)
    print() 

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')



def game():
    #OPTIONAL (Commented out to save time)

    # print_slow("We are going to play Rock-Paper-Scissors. ")
    # print_slow("On the count of 5, enter R P or S for their respective tool") #Give them the info about the game
    # sleep(3) #Wait for them to read 
    # print_slow("Starting Game.") #Start load
    # sleep(1) 
    # clear()


    #Give them the dialouge
    
    print("Rock")
    sleep(1)
    print("Paper")
    sleep(1)
    print("Scissors")
    sleep(1)
    print("Shoot")
    sleep(1)
    print("Enter R P or S")

    #Computer can choose
    choice = random.randint(0,2)
    if choice == 0:
        choice = "Rock"
    elif choice == 1:
        choice = "Paper"
    elif choice == 2:
        choice = "Scissors"

    #User chooses
    selected_pos = input("").lower()
    if selected_pos == "r":
        selected_pos = "Rock"
    elif selected_pos == "p":
        selected_pos = "Paper"
    elif selected_pos == "s":
        selected_pos = "Scissors"
    else:
        print(" I did not get that")
        print_slow("Restarting in 5 seconds")
        sleep(4)
        clear()
        game()

    # #Final "Battle"
    print_slow("You chose " + selected_pos + " and the computer chose " + choice)
    if choice == selected_pos:
        print("It was a draw!")
    elif selected_pos == "Rock" and choice == "Scissors" or selected_pos == "Paper" and choice == "Rock" or selected_pos == "Scissors" and choice == "Paper":
        print("You won!")
    else:
        print("You lost!")
game()