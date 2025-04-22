# choices = {
#     "take the flyer": "You decide to take the flyer and investigate the underground club. The address leads you to a dimly lit alley. You can hear faint music thumping behind a hidden door. Do you:",
#     "pick up the flyer": "You decide to take the flyer and investigate the underground club. The address leads you to a dimly lit alley. You can hear faint music thumping behind a hidden door. Do you:",
#     "grab the flyer": "You decide to take the flyer and investigate the underground club. The address leads you to a dimly lit alley. You can hear faint music thumping behind a hidden door. Do you:",
#     "get the flyer": "You decide to take the flyer and investigate the underground club. The address leads you to a dimly lit alley. You can hear faint music thumping behind a hidden door. Do you:",
#     "investigate the flyer": "You decide to take the flyer and investigate the underground club. The address leads you to a dimly lit alley. You can hear faint music thumping behind a hidden door. Do you:",
    
#     "pick up the notebook": "You decide to pick up the notebook and follow the notes about 'The Passage.' The scrawled directions lead you to an old subway station. The platform is abandoned, but you notice strange symbols on the walls. Do you:",
#     "grab the notebook": "You decide to pick up the notebook and follow the notes about 'The Passage.' The scrawled directions lead you to an old subway station. The platform is abandoned, but you notice strange symbols on the walls. Do you:",
#     "read the notebook": "You decide to pick up the notebook and follow the notes about 'The Passage.' The scrawled directions lead you to an old subway station. The platform is abandoned, but you notice strange symbols on the walls. Do you:",
#     "investigate the notebook": "You decide to pick up the notebook and follow the notes about 'The Passage.' The scrawled directions lead you to an old subway station. The platform is abandoned, but you notice strange symbols on the walls. Do you:",
    
#     "check the phone": "You decide to check the phone. The cryptic text, 'Meet me where the light fades,' was sent from an unknown number. You can reply or try to trace the sender. Do you:",
#     "pick up the phone": "You decide to check the phone. The cryptic text, 'Meet me where the light fades,' was sent from an unknown number. You can reply or try to trace the sender. Do you:",
#     "look at the phone": "You decide to check the phone. The cryptic text, 'Meet me where the light fades,' was sent from an unknown number. You can reply or try to trace the sender. Do you:",
#     "investigate the phone": "You decide to check the phone. The cryptic text, 'Meet me where the light fades,' was sent from an unknown number. You can reply or try to trace the sender. Do you:",
    
#     "search the apartment": "You decide to search the apartment for more clues. As you rummage through drawers and cabinets, you find a locked box and a strange key under the bed. Do you:",
#     "look around the apartment": "You decide to search the apartment for more clues. As you rummage through drawers and cabinets, you find a locked box and a strange key under the bed. Do you:",
#     "investigate the apartment": "You decide to search the apartment for more clues. As you rummage through drawers and cabinets, you find a locked box and a strange key under the bed. Do you:",
#     "explore the apartment": "You decide to search the apartment for more clues. As you rummage through drawers and cabinets, you find a locked box and a strange key under the bed. Do you:",
# }



# def handle_choice(choice):
#     response = choices.get(choice.lower(), None)
#     if response:
#         print(response)
#     else:
#         print("Invalid choice. Please try again.")


# z = "explore the apartment"
# Handle the user's choice
# handle_choice(z)


    
    # # Open the file and read each line
 
# Load the choices from the file



def create_dict_from_text(file_path):
    final_options = {}
    with open(file_path) as f:
        for line in f:
            (key, val) = line.split()
            final_options[int(key)] = val
        return final_options

create_dict_from_text("CodeWars/file.txt")

