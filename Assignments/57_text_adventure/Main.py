from time import sleep
from os import system, name

#Okay so this is pretty much my final project - I want to make it easier for myself because I don't really enjoy writing the options/all of the creative stuff 

#Grab file
intro_text = open("Assignments/57_text_adventure/Text/Intro.txt", "r") 


#Read file
intro_text_string = intro_text.read() 

#Def some useful functions
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

#This was made to help me make this much easier so note that
def create_dict_from_text(file_path):
    final_options = {}
    with open(file_path) as f:
        for line in f:
            (key, val) = line.split()
            final_options[int(key)] = val
        return final_options

create_dict_from_text("CodeWars/file.txt")







def option1_Flyer():
    print_slow("You decided to take the flyer and investigate the underground club.")
    print_slow("The address leads you to a dimly lit alley. You can hear faint music thumping behind a hidden door.")
    print_slow("What do you do next?")
    
    flyer_choices = {
        "knock on the door": "You knock on the door, and a sliding panel opens to reveal a pair of eyes. A raspy voice asks for a password. Do you:",
        "listen at the door": "You press your ear to the door to eavesdrop. You catch fragments of conversation inside, but someone might notice you. Do you:",
        "look around the alley": "You decide to look around the alley for clues. There’s graffiti on the walls, and a shadowy figure lingers near a dumpster. Do you:",
        "open the door": "You push the door open without hesitation. Inside, strobe lights and pounding bass overwhelm your senses, but a bouncer immediately blocks your way. Do you:",
    }
def option1_Book():
    print("Book")
def option1_Phone():
    print("PHONE")
def option1_Apartment():
    print("APARTMENT")



def introChoice1():
    choices = {
        "take the flyer": "You decide to take the flyer and investigate the underground club. The address leads you to a dimly lit alley. You can hear faint music thumping behind a hidden door. Do you:",
        "pick up the flyer": "You decide to take the flyer and investigate the underground club. The address leads you to a dimly lit alley. You can hear faint music thumping behind a hidden door. Do you:",
        "grab the flyer": "You decide to take the flyer and investigate the underground club. The address leads you to a dimly lit alley. You can hear faint music thumping behind a hidden door. Do you:",
        "get the flyer": "You decide to take the flyer and investigate the underground club. The address leads you to a dimly lit alley. You can hear faint music thumping behind a hidden door. Do you:",
        "investigate the flyer": "You decide to take the flyer and investigate the underground club. The address leads you to a dimly lit alley. You can hear faint music thumping behind a hidden door. Do you:",
        
        "pick up the notebook": "You decide to pick up the notebook and follow the notes about 'The Passage.' The scrawled directions lead you to an old subway station. The platform is abandoned, but you notice strange symbols on the walls. Do you:",
        "grab the notebook": "You decide to pick up the notebook and follow the notes about 'The Passage.' The scrawled directions lead you to an old subway station. The platform is abandoned, but you notice strange symbols on the walls. Do you:",
        "read the notebook": "You decide to pick up the notebook and follow the notes about 'The Passage.' The scrawled directions lead you to an old subway station. The platform is abandoned, but you notice strange symbols on the walls. Do you:",
        "investigate the notebook": "You decide to pick up the notebook and follow the notes about 'The Passage.' The scrawled directions lead you to an old subway station. The platform is abandoned, but you notice strange symbols on the walls. Do you:",
        
        "check the phone": "You decide to check the phone. The cryptic text, 'Meet me where the light fades,' was sent from an unknown number. You can reply or try to trace the sender. Do you:",
        "pick up the phone": "You decide to check the phone. The cryptic text, 'Meet me where the light fades,' was sent from an unknown number. You can reply or try to trace the sender. Do you:",
        "look at the phone": "You decide to check the phone. The cryptic text, 'Meet me where the light fades,' was sent from an unknown number. You can reply or try to trace the sender. Do you:",
        "investigate the phone": "You decide to check the phone. The cryptic text, 'Meet me where the light fades,' was sent from an unknown number. You can reply or try to trace the sender. Do you:",
        
        "search the apartment": "You decide to search the apartment for more clues. As you rummage through drawers and cabinets, you find a locked box and a strange key under the bed. Do you:",
        "look around the apartment": "You decide to search the apartment for more clues. As you rummage through drawers and cabinets, you find a locked box and a strange key under the bed. Do you:",
        "investigate the apartment": "You decide to search the apartment for more clues. As you rummage through drawers and cabinets, you find a locked box and a strange key under the bed. Do you:",
        "explore the apartment": "You decide to search the apartment for more clues. As you rummage through drawers and cabinets, you find a locked box and a strange key under the bed. Do you:",
    }
    
    intro_choice = input("What do you do? ") .lower() #Give them the option
    if intro_choice == "take the flyer" or intro_choice == "pick up the flyer" or intro_choice == "grab the flyer" or intro_choice == "get the flyer" or intro_choice == "investigate the flyer":
        option1_Flyer()
    if intro_choice == "pick up the notebook" or intro_choice == "grab the notebook" or intro_choice == "read the notebook" or intro_choice == "investigate the notebook":
        option1_Book()
    if intro_choice == "check the phone" or intro_choice == "pick up the phone" or intro_choice == "look at the phone" or intro_choice == "investigate the phone":
        option1_Phone()
    if intro_choice == "search the apartment" or intro_choice == "look around the apartment" or intro_choice == "investigate the apartment" or intro_choice == "explore the apartment":
        option1_Apartment()
    intro_choice_string = choices.get(str(intro_choice)) #Is their option in the dictionary
    if intro_text_string != "None":
        print(intro_choice_string) #Print the outcome of their choice
    else:
        print("Sorry, I didn't get that!")
        introChoice1()

def introText():
    print_slow(intro_text_string)










#okay so I wanted to make it so there aren't as many functions as there are descisions but I sent all my time trying to figure out how to use 1 function - couldn't figure it out so we are here :)
introChoice1()