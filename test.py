LIGHT_PURPLE = "\033[1;35m"
yellow  = "\033[1;33m"
RESET = '\033[0m'  # This resets the color back to default

# Simple example
print(f"{LIGHT_PURPLE}======================================\n{yellow}DAY 1: Oh No, We’re Really Doing This{LIGHT_PURPLE}\n======================================{RESET}")
print(f"{LIGHT_PURPLE}======================================\n{yellow}DAY 2: Martian Mondays{LIGHT_PURPLE}\n======================================{RESET}")
print(f"{LIGHT_PURPLE}======================================\n{yellow}DAY 3: Midlife Crisis on Mars{LIGHT_PURPLE}\n======================================{RESET}")
print(f"{LIGHT_PURPLE}======================================\n{yellow}DAY 4: The Martian Blues{LIGHT_PURPLE}\n======================================{RESET}")
print(f"{LIGHT_PURPLE}======================================\n{yellow}DAY 5: Rescue (or Not){LIGHT_PURPLE}\n======================================{RESET}")

# *************************************************************************
# Program: problem solving.py
# Course: CSP1114 PROBLEM SOLVING AND PROGRAM DESIGN
# Lecture / Lab Section: TC4L / TL2L
# Trimester: 2430
# Names: MADHUSHAA A/P KALITHASS | MEMBER_NAME_2 | NURSYAHIRAH_AQILAH_BINTI_AINUL_HISHAM | MEMBER_NAME_4
# IDs: 242FC244JR | MEMBER_ID_2 | 242FC243DZ | MEMBER_ID_3
# Emails: MADHUSHAA.KALITHASS@student.mmu.edu.my | MEMBER_EMAIL_2 | nursyahirah.aqilah.ainul@student.mmu.edu.my | MEMBER_EMAIL_3
# *************************************************************************

import os 

#Dictionary of resources used in the game 
game_resources = {"oxygen": 100, "water": 100, "food": 100, "energy": 100} 

#Initialise value of resources and inventory items
oxygen = 100
water = 100
food = 100
energy = 100
score = 0
inventory = [] #List to hold inventory items

#File to store user data (username, password, progress, game resources, inventory, score)
user_data_file = "user_data.txt"

#Check if user_data file exists; if not, create one
def checkfile():
    if not os.path.exists(user_data_file):
        with open(user_data_file, "w") as file:
            #Writing header
            file.write("username, password, progress, game_resources, inventory, score\n") 

#Register new users and initial game resources, progress & score
def save_data(username, password, progress = 0, oxygen = 100, water = 100, food = 100, energy = 100, inventory = [], score = 0):
     #If file is empty, write the header
    if os.path.getsize(user_data_file) == 0:  #If file size = 0 (empty file)
        with open(user_data_file, "w") as file:
            file.write("username, password, progress, oxygen, water, food, energy, inventory, score\n")

    #Append user data
    with open(user_data_file, "a") as file:
        #Ensure every inventory item is written in the correct format
        inventory_str = ",".join(inventory) if inventory else "empty"
        file.write(f"{username}, {password}, {progress}, {oxygen}, {water}, {food}, {energy}, {inventory_str}, {score}\n")

# Save the user's progress (updates progress, resources, inventory, score)
def save_progress(username, progress, oxygen, water, food, energy, inventory, score):
    users = load_userdata()  # Load all user data

    # Ensure every inventory item is written correctly
    inventory_str = ",".join(inventory) if inventory else "empty"

    # Update the existing user data
    users[username] = [str(progress), str(oxygen), str(water), str(food), str(energy), inventory_str, str(score)]

    # Write the updated data back to the file
    with open(user_data_file, "w") as file:
        file.write("username, password, progress, oxygen, water, food, energy, inventory, score\n")  # Header
        for user, data in users.items():
            file.write(f"{user}, {', '.join(data)}\n")

#Load user progress, resources, score based on username
def progress_load(username): 
    users = load_userdata()  #Load user data from file

    if username in users:
        progress = users[username][1]
        
        #Extract resources (separate variables for each resource)
        oxygen = users[username][2]
        water = users[username][3]
        food = users[username][4]
        energy = users[username][5]
        
        #Handle inventory which is split by commas for correct format
        inventory_str = users[username][6]
        inventory = inventory_str.split(",") if inventory_str != "empty" else []
        
        score = users[username][7]

        return progress, oxygen, water, food, energy, inventory, score 
    else:
        return None  #Return None if the username is not found

#Load all user data from the file into a dictionary
def load_userdata():
    #Dictionary to store users' data
    users = {}  

    if not os.path.exists(user_data_file):  #If file doesn't exist, return an empty dictionary
        return users

    with open(user_data_file, "r") as file:
        #Read all lines, skipping the header
        lines = file.readlines()[1:]  

    for line in lines:
        data = line.strip().split(", ")  
        users[data[0]] = data[1:] 

    return users

#Login function for existing users or register new ones
def login():
    users = load_userdata()  #Load all user data

    print("Welcome to Lost in Mars (and My Sanity) Game!\n")
    while True:
        choice = input("Do you have an account? (yes/no): ").lower()

        if choice == "yes":
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if username in users and users[username][0] == password:
                print(f"Welcome back, {username}!")
                #Return user details
                return username, int(users[username][1]), int(users[username][2]), int(users[username][3]), int(users[username][4]), int(users[username][5]), users[username][6].split(",") if users[username][6] != "empty" else [], int(users[username][7])
 
            else:
                print("Invalid username or password. Try again.")

        elif choice == "no":
            username = input("Choose a username: ")

            while username in users:
                print("Username already taken. Choose a different one.")
                username = input("Choose a username: ")

            password = input("Choose a password: ")
            #Register new user
            save_data(username, password)  
            print("Account created successfully!")
            #New user starts with default resources, 0 progress and score
            return username, 0, 100, 100, 100, 100, [], 0

        else:
            print("Invalid choice. Please type 'yes' or 'no'.")
    

#Function to allow users to restart the game or continue from last saved pone
def restart_or_continue(username):
    while True:
        choice = input("Do you want to restart the game or continue from your last save? (restart/continue): ").lower()

        if choice == "restart":
            save_progress(username, 0, 100, 100, 100, 100, [], 0)  #Reset progress, resources, inventory, score
            print("Game restarted.")
            #Return default new game values
            return 0, 100, 100, 100, 100, [], 0

        elif choice == "continue":
            saved_data = progress_load(username)
            if saved_data:
                progress, oxygen, water, food, energy, inventory, score = saved_data
                print(f"Resuming game from Day {(int(progress)) + 1}.")  # Show the correct day they're continuing from
                return progress, oxygen, water, food, energy, inventory, score   
            else:
                print("No saved data found. Starting a new game.")
                #Default new game values
                return 0, 100, 100, 100, 100, [], 0

        else:
            print("Invalid choice. Please type 'restart' or 'continue'.")

#Game each day
import sys

def game_loop(username, progress):
    yellow  = "\033[0;33m"
    nocolor = "\033[0m"
    light_purple = "\033[1;35m"
    #Continue from last saved day until Day 5
    for day in range(int(progress) + 1, 6): 

        if day == 1:
            intro_sequence_day1()
            explore_mars()
            InsideSpaceShip()
            time_coded1()
            event_day_1()

        elif day == 2:
            intro_sequence_day2()
            get_random_narration()
            explore_mars()
            InsideSpaceShip()
            event_day_2(inventory)
            time_coded2()

        elif day == 3:
            intro_sequence_day3()
            time_coded3()
            get_random_narration()
            explore_mars()
            InsideSpaceShip()
            event_day_3()

        elif day == 4:
            intro_sequence_day4()
            get_random_narration()
            explore_mars()
            InsideSpaceShip()
            event_day_4()
            time_coded4()

        elif day == 5:
            intro_sequence_day5()
            explore_mars()
            InsideSpaceShip()
            event_day_5()  

        # Update progress after completing the day
        progress = day  # Moves to the next day

        # Save the updated values at the end of each day
        save_progress(username, progress, oxygen, water, food, energy, inventory, score)

        #Print resources after saving progress
        print(f"Resources after saving progress:\noxygen: {oxygen}, water: {water}, food: {food}, energy: {energy}, inventory: {inventory}")

        #Ask if the player wants to continue or exit
        if day < 5:
            choice = input("\nDo you want to continue to the next day? (yes/no): ").strip().lower()
            if choice == "no":
                print(f"----------------------------------------------------\noxygen:{oxygen} | water:{water} | food:{food} | energy:{energy} | score:{score}\n----------------------------------------------------")
                print("\n🚀 Progress saved. See you next time!")
                return  #Exit game
            elif choice == "yes": 
                print(f"----------------------------------------------------\noxygen:{oxygen} | water:{water} | food:{food} | energy:{energy} | score:{score}\n----------------------------------------------------")
                continue
            else: 
                print("Invalid input. Enter 'yes' or 'no'.")
                choice = input("\nDo you want to continue to the next day? (yes/no): ").strip().lower()
                
        if day == 5: 
            print("MARVIN: Against all odds, you did it. I’m… speechless. Almost.")
            print(f"Proud of you, {username}. Your score: {score}. Thank you for playing!")
            print(u"\033[1;35m""""
                  __| |___________________________________________| |__
                  __   ___________________________________________   __
                    | |                                           | |  
                    | |     \u001b[1;33m.___________. __    __   _______\u001b[1;35m      | |  
                    | |     \u001b[1;33m|           ||  |  |  | |   ____|\u001b[1;35m     | |  
                    | |     \u001b[1;33m`---|  |----`|  |__|  | |  |__\u001b[1;35m        | |  
                    | |         \u001b[1;33m|  |     |   __   | |   __|\u001b[1;35m       | |  
                    | |         \u001b[1;33m|  |     |  |  |  | |  |____\u001b[1;35m      | |  
                    | |         \u001b[1;33m|__|     |__|  |__| |_______|\u001b[1;35m     | |  
                    | |                                           | |  
                    | |         \u001b[1;33m_______ .__   __.  _______\u001b[1;35m        | |  
                    | |        \u001b[1;33m|   ____||  \ |  | |       \ \u001b[1;35m      | |  
                    | |        \u001b[1;33m|  |__   |   \|  | |  .--.  |\u001b[1;35m      | |  
                    | |        \u001b[1;33m|   __|  |  . `  | |  |  |  |\u001b[1;35m      | |  
                    | |        \u001b[1;33m|  |____ |  |\   | |  '--'  |\u001b[1;35m      | |  
                    | |        \u001b[1;33m|_______||__| \__| |_______/ \u001b[1;35m      | |  
                  __| |___________________________________________| |__
                  __   ___________________________________________   __
                    | |                                           | |  
    """)
    print(nocolor)
    sys.exit()



#Main function to start the game login process
def main():
    global oxygen, water, food, energy, inventory, score, username, progress 
    #Game Interface
    yellow  = "\033[0;33m"
    nocolor = "\033[0m"
    light_purple = "\033[1;35m"
    print(light_purple)
    print("__| |_________________________________________________________________________| |__\n"
    "__   _________________________________________________________________________   __\n"
    "  | |                                                                         | |\n"
    f"  | |   {yellow}  __        ______        _______.___________.    __  .__   __.   {light_purple}    | |\n"
    f"  | |   {yellow} |  |      /  __  \\      /       |           |   |  | |  \\ |  | {light_purple}      | |\n"
    f"  | |   {yellow} |  |     |  |  |  |    |   (----`---|  |----`   |  | |   \\|  |  {light_purple}     | |\n"
    f"  | |   {yellow} |  |     |  |  |  |     \\   \\       |  |        |  | |  . `  | {light_purple}      | |\n"
    f"  | |   {yellow} |  `----.|  `--'  | .----)   |      |  |        |  | |  |\\   |  {light_purple}     | |\n"
    f"  | |   {yellow} |_______| \\______/  |_______/       |__|        |__| |__| \\__| {light_purple}      | |\n"
    f"  | |                                                                         | |\n"
    f"  | |   {yellow}       .___  ___.      ___      .______          _______.      {light_purple}       | |\n"
    f"  | |   {yellow}       |   \\/   |     /   \\     |   _  \\        /       |   {light_purple}          | |\n"
    f"  | |   {yellow}       |  \\  /  |    /  ^  \\    |  |_)  |      |   (----`  {light_purple}           | |\n"
    f"  | |   {yellow}       |  |\\/|  |   /  /_\\  \\   |      /        \\   \\   {light_purple}              | |\n"
    f"  | |   {yellow}       |  |  |  |  /  _____  \\  |  |\\  \\----.----)   |   {light_purple}             | |\n"
    f"  | |   {yellow}       |__|  |__| /__/     \\__\\ | _| `._____|_______/  {light_purple}               | |\n"
    "  | |                                                                         | |\n"
    "__| |_________________________________________________________________________| |__\n"
    "__   _________________________________________________________________________   __\n"
    "  | |                                                                         | |")
    print(nocolor)
    #Make sure the file exists
    checkfile()  
    
    #Login or register
    username, progress,  oxygen, water, food, energy, inventory, score = login()  
    #Ask if they want to restart or continue
    progress,  oxygen, water, food, energy, inventory, score = restart_or_continue(username)
    
    # Initialize global variables with loaded values and ensure they are integers
    oxygen = int(oxygen)
    water = int(water)
    food = int(food)
    energy = int(energy)
    inventory = inventory  
    score = int(score)

    print(f"----------------------------------------------------\noxygen:{oxygen} | water:{water} | food:{food} | energy:{energy} | score:{score}\n----------------------------------------------------")   

    #Start the game loop from the saved progress
    game_loop(username, progress)


#-----------------CHECK DEPLETED RESOURCE------------------------------------------------------

#When resource is low, show choices to user
def show_choices(depleted_resource):
    global oxygen, water, food, energy 
    print(f"\nYour {depleted_resource} is fully used. Choose an option: ")
    print("1. Rest\n2. Use inventory item (water packet/food packet/energy packet)\n3. Sacrifice other resource")

    #Make sure user only can enter 1,2 or 3    
    while True:    
        choice = input("Pick your choice(1/2/3): ")
        if choice.isdigit():
            choice = int(choice)
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please enter 1, 2 or 3")
        else:
            print("Invalid input. Please enter a number!")

def sacrifice_resource(depleted_resource):
    global oxygen, water, food, energy
    temp_resources = {"oxygen": oxygen, "water": water, "food": food, "energy": energy}
    #Remove resource that's used up
    del temp_resources[depleted_resource]
    #Remove oxygen, since oxygen cannot be sacrificed 
    del temp_resources["oxygen"] 
    
    print(f"You have ran out of {depleted_resource}")
    print("Here are your current resources: ")
    for resource, value in temp_resources.items():
        print(f"{resource}: {value}") 
    
    while True: 
        chosen_resource = input("Which resource would you like to sacrifice? :").lower()
        if chosen_resource not in temp_resources: 
            print("Invalid choice. No resource sacrificed.")
            continue
        
        while True:
            #How much resource to sacrifice
            sacrifice_amount = input(f"How much {chosen_resource} would you like to sacrifice? : ")
            if sacrifice_amount.isdigit(): 
                sacrifice_amount = int(sacrifice_amount)
                if sacrifice_amount <= temp_resources[chosen_resource]:
                    break
                else: 
                    print(f"You don't have enough {chosen_resource} to sacrifice!")
            else: 
                print("Invalid input. Please enter a valid number!")

        #Deducting sacrifice amount from the resource that has been sacrificed
        if chosen_resource == "water" and sacrifice_amount <= water: 
            water -= sacrifice_amount
        elif chosen_resource == "food" and sacrifice_amount <= food: 
            food -= sacrifice_amount
        elif chosen_resource == "energy" and sacrifice_amount <= energy: 
            energy -= sacrifice_amount
                
        #Add on to depleting resource 
        if depleted_resource == "water":
            water += sacrifice_amount
        elif depleted_resource == "food":
            food += sacrifice_amount
        elif depleted_resource == "energy":
            energy += sacrifice_amount
            
        print(f"You sacrificed {sacrifice_amount} of {chosen_resource} to get {sacrifice_amount} of {depleted_resource}")
        save_progress(username, progress, oxygen, water, food, energy, inventory, score)  # Save to file
        return 

def check_depleted_resources(username):
    global progress, oxygen, water, food, energy, inventory   
    save_progress(username, progress, oxygen, water, food, energy, inventory, score)  # Save to file

    #Game condition loop to check depleted resources
    while True: 
        if oxygen <= 0:
            print("You ran out of oxygen. Game Over :(")
            sys.exit()  #Force the game to exit
        #Initialise depleted resource to nothing
        depleted_resource = None 
        
        #Check for depleted resources
        if water <= 0: 
            depleted_resource = "water"
        elif food <= 0:
            depleted_resource = "food"
        elif energy <= 0:
            depleted_resource = "energy"
        else:
            break
        
        #Call show_choices only when a resource is depleted
        if depleted_resource: 
            choice = show_choices(depleted_resource)
            
        #User choice output    
        if choice == 1:
            energy += 15
            print("You had some rest and gained 15 energy.")
            save_progress(username, progress, oxygen, water, food, energy, inventory, score)  # Save to file
            
        elif choice == 2:
            if not inventory:
                print("Inventory is empty")
                continue
            while True:
                #Standardize inventory item names
                inventory = [item.replace(" ", "_") for item in inventory]
                use_inventory = input(f"What inventory item do you want to use? You have {inventory}: ").lower()
                if use_inventory == "water packet" or use_inventory == "waterpacket" or use_inventory == "water_packet":
                    if "water packet" in inventory or "waterpacket" in inventory or "water_packet" in inventory:
                        water += 30
                        inventory.remove("water_packet")
                        save_progress(username, progress, oxygen, water, food, energy, inventory, score)  # Save to file
                        print(f"DEBUG: Inventory after removing food_packet: {inventory}")  # Debugging
                        break
                    else:
                        print("You don't have a water packet in your inventory!") 
                elif use_inventory == "food packet" or use_inventory == "foodpacket" or use_inventory == "food_packet":
                    if "food packet" in inventory or "foodpacket" in inventory or "food_packet" in inventory:
                        food += 30
                        energy += 15
                        inventory.remove("food_packet")
                        save_progress(username, progress, oxygen, water, food, energy, inventory, score)  # Save to file
                        break
                    else:
                        print("You don't have a food packet in your inventory!") 
                elif use_inventory == "energy packet" or use_inventory == "energypacket" or use_inventory == "energy_packet":
                        if "energy packet" in inventory or "energypacket" in inventory or "energy_packet" in inventory:
                            energy += 30
                            inventory.remove("energy_packet")
                            save_progress(username, progress, oxygen, water, food, energy, inventory, score)  # Save to file
                            break
                        else:
                            print("You don't have an energy packet in your inventory!") 
                else:
                    print("Invalid choice!")
                
        elif choice == 3: 
            sacrifice_resource(depleted_resource)
        
        #Update resource value after each loop  
        print(f"\nUpdated Resources: oxygen: {oxygen}, water: {water}, food: {food}, energy: {energy} ")
            
        if oxygen <= 0 or water <= 0 or food <= 0 or energy <= 0:
            print("You have ran out of critical resources. Game over:(")
            sys.exit()  #Force the game to exit
    return True #Continue game if resources are sufficient 
#--------------------------------------END OF CONDITION----------------------------------------------------------
#--------------------------------------TAYA'S CONDITION (RANDOM NARRATION)--------------------------------------------------------------------------
# Taya's condition for the random narration given to promt the player to make a fixed (explore mars) choice
import random
import textwrap

options = {
    1: """Your initial mission has produced amazing clues and delightful hints, but the ultimate solution is still unclear. 
You should continue to investigate your current place in hopes of finding the answers you seek""",
    
    2: """Time is slipping away like Martian dust through your fingers.
You plan to double down on your current efforts and gamble on a completely  
new direction..choose wisely..""",
    
    3: """Desperation is a cold wind whistling across the Martian plains, and it's biting at your heels.
“I want to play it safe, risking everything on a last-ditch attempt to secure my survival! 
HERE I GO..BUT WHERE T-T”"""
}

available_numbers = [1, 2, 3]  # List of available choices

def get_random_narration():
    global available_numbers  # We need to modify the global list of available numbers
    
    if not available_numbers:  # If all numbers have been used, do nothing and stop
        print("The end!")
        return
    
    random_number = random.choice(available_numbers)  # Pick a random number from the list
    available_numbers.remove(random_number)  # Remove the selected number
    
    # Print the corresponding message for the selected number
    print(textwrap.dedent(options[random_number]))
    print("\n" + "-" * 80 + "\n")  # Separator for readability
    #get_random_narration()
#------------------------------------------------------END----------------------------------------------------------------------------------------------------

#---------------------------------------TAYA'S CONDITION (EXPLORE MARS)---------------------------------------------------------------------------------------
#Taya's condition for the choice
#Game for choice d in explore mars
def riddle_game():
    riddle = {
        "question": "I have cities, but no houses; forests, but no trees; and water, but no fish. What am I?",
        "options": ["a. A map", "b. A cloud", "c. A dream", "d. A photograph"],
        "answer": "a"  # The correct option letter
    }

    count = 0

    print("\nMARVIN: 'Hold on a second, space cowboy. Before you get too excited about that water, answer me this:'")
    while True:
        print(riddle["question"])
        for option in riddle["options"]:
            print(option)

        player_answer = input("What's the answer? ").lower()

        if player_answer == riddle["answer"]:
            print("MARVIN: 'Huh. Not bad. Guess you're not a total space cadet after all.'")
            print("Wait a minute...")
            print("You collect the water and move on.")
            return True
        else:
            print("MARVIN: 'Wrong!  Looks like someone needs to brush up on their Martian trivia.'")
            count += 1
        if count > 2:
            print("MARVIN: 'Alright, alright, you're clearly struggling.  Here's a *little* help. Choose a lifeline:'")
            print("1. Hint")
            print("2. 50/50")
            print("3. Give up and try a different approach (lose water opportunity)")

            while True: # Lifeline input loop
                lifeline_choice = input("Which lifeline do you choose (1/2/3)? ")

                if lifeline_choice == '1':
                    print("MARVIN: 'Okay, here's a hint: Think about something that represents the world but isn't the world itself.'")
                    break  # Exit lifeline choice loop
                elif lifeline_choice == '2':
                    print("MARVIN: 'Fine. I've eliminated two wrong answers. You're welcome.'")
                    # Directly remove "cloud" and "photograph"
                    if "b. A cloud" in riddle["options"]:
                        riddle["options"].remove("b. A cloud")
                    if "d. A photograph" in riddle["options"]:
                        riddle["options"].remove("d. A photograph")
                    break  # Exit lifeline choice loop
                elif lifeline_choice == '3':
                    print("MARVIN: 'Smart move. Sometimes it's best to cut your losses.'")
                    return False # player did not get the answer correct, and they are giving up
                else:
                    print("MARVIN: 'Invalid lifeline choice. You get nothing!'")
                    continue  # Restart the lifeline choice loop
        else:
            continue

#Game in explore mars choice e        
def game_e():
    import time
    import sys
    import random

    keepGoing = True
    water_packet = False  
    preserved_food = False  # Condition to track if supplies have been found

    # Initial game introduction
    print("""You are wandering through a desolate landscape when you spot a derelict spacecraft abandoned quietly in the distance, its hull cracked but seemingly intact.""")
    

    # Places and their descriptions
    outside_ship = ("Outside the Ship", "You stand outside the derelict spacecraft, its cracked hull looming over you.")
    inside_ship = ("Inside the Ship", "You are inside the ship. The eerie silence feels almost alive. You found some water packets and some tools.")
    abandoned_camp = ("Abandoned Camp", "You find an abandoned camp nearby, with remnants of a fire and some old supplies and preserved food.")

    # Dictionary of where you are and where you can go based on where you are #
    transitions = {
        outside_ship: (inside_ship, abandoned_camp),
        inside_ship: (outside_ship,),
        abandoned_camp: (outside_ship,)
    }

    ## Current location ##
    location = outside_ship

    ## Main game loop ##
    while keepGoing:
        print("")
        print(location[1])
        time.sleep(2)
        print("\nYou can go to these places:")
        
        ## Adds a number to each place ##
        for (i, t) in enumerate(transitions[location]):
            print(i + 1, t[0])
        
        ## Obviously where you choose to go ##
        choice = input("\nGo to (enter the number): ")  # Prompt for choice

        # Validate choice
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(transitions[location]):
            print("Invalid choice. Please try again.")
            continue  # Restart the loop if the choice is invalid

        location = transitions[location][int(choice) - 1]
        
        if location == inside_ship:
            print("MARVIN quips: 'Another spaceship? Looks like you’re not the only one who failed out here. At least this one left water.'")
            print("\nYou grab the water packet as well as supplies and move on.")
            time.sleep(2)
            water_packet = True  # Set the condition to True
        
        if location == abandoned_camp:
            print("You find preserved food and some old supplies but nothing of great value.")
            time.sleep(2)
            preserved_food = True  # Set the condition to True

        if location == outside_ship:
            print("You can choose to enter the ship or explore the camp.")
            time.sleep(1)

        # Check if the player has found the supplies and end the game
        if water_packet and preserved_food:
            print("\nYou have gathered supplies and explored the ship. Your adventure ends here.")
            keepGoing = False  # End the game after finding supplies

    print("Exploration Over.")

available_choices = {"a": "Enter the cave", "b": "Dismantle the rover", "c": "Explore the crater", "d": "Break the asteroid", "e": "Search the abandoned spaceship"}

# Function to explore Mars
def explore_mars():
    global energy, food, oxygen, water, available_choices
    # Check for depleted resources
    if not check_depleted_resources(username):
        return False  # Exit if game over
    
    while True:
        print("\nChoose your action:")
        for key, value in available_choices.items():
            print(f"{key}. {value}")

        choice = input("Enter your choice: ").lower()
        if choice in available_choices:
            break
        else:
            print("Invalid choice. No action taken.")
            continue

    if choice == "a":
        food += 20
        energy -= 10
        oxygen += 10
        nocolor = "\033[0m"
        print(u"\u001b[38;5;204m"f"""
                                                  )>                                                 
                                               +@ >@[>-                                             
                                               @+ @[)+:@+                                           
                                              +@= #@[  #]                                           
                                             %>@= #@*  :@:                                          
                                           >@< @= %@+ > :@                                          
                                     )[@* =@  @@= @@*)@ <[  +@+@                                    
                                    :@  #[)<  ]@=+@@*@@  @+>@: >@                                   
                                    [< - @@:  ]@]@@@@@@  @@@=   ]%                                  
                                    @* )+@[ @ )@@@@@@@@  <@@  <+ )>                                 
                                   @+  #)%--@ %@@@ %@@@)  ]@@ *: %+                                 
                                  )#  +@@@ *@=@@    +@@@@+ )@@  @[[                                 
                                  [[   @@  )@@@)       )@>  %@: :-@                                 
                            )%@- -@    %-  %@@%         @@@: @@  *@@                                
                            @ :@ #> @  )-=:@@)          @@@:  @*  -@=                               
                           )[+@%*@= @   :@*@<           @@@<+   >> @*                               
                           [] [@@@  [>  +@#@        *@%@@@@@< ::   %)  %)                           
                          ]@] *@@[  [@> [@@%        @- >@@@@<*@#   <##@  ))                         
                         <@@%  #@ = [@* @@<        +@   )@@@< @@    @@> > @                         
                         )+@@)+@>)@>[@*>@@         +@ + =@@@< @@)   )@@%<>>@                        
                         @:%@@@@=@@@[@*@@@=        +@ ) +@@@# @@@@: -@@@@@=)%                       
                         @:@@@@@@@@@@@@@@      @@# +@ [@)@@@@+@@@@:  @@@@@@  @]                     
                        [@: =] )@@@@@@@@@     :@>@ +@ [@)*@@@@@@@@= =@@@@@@@ -=@                    
                    )@%==@@@@@@) @@)-@@@@-    [% @]+@ @@@@@@@@@@@@@ %@@@@@@@@@[+%                   
                  @@)@@@@@@@@@@-@@@@@][@@]    [@@@%#@@@@<>@@@@]@@@@@@@@@@@@@@@@@)@                  
                +%%%%%%%%%%%%%%%%%%]***********)%%%%%%)+===========<%%%%%%%%%%%%%%%+                
                    {nocolor}                         :----------                                            
                You step into the cave, the air cool and damp. Among the shadows, you find a small patch of soil suitable for planting.
                MARVIN: "A cave garden? Bold choice. Let's hope you have a green thumb—or at least a brown one."
                You start planting, envisioning the fresh food it will yield. Your food supply increases but you sacrificed your energy, still worth it.
                """)
    elif choice == "b":
        energy -= 20
        oxygen -= 10
        print(u"\u001b[38;5;240m""""                                                                                                                                
                               @@@@                                          
                               @==@                                          
                               @@@@  @@@@@                                   
                                @@    @@                                     
                            @@@@@@@@@@@@@@@@@                                
\u001b[38;5;137m        @@@@@@@@@@@\u001b[38;5;240m         @\u001b[38;5;22m:........+*:..:\u001b[38;5;240m@                                
\u001b[38;5;137m      @@@@:.......@#%@\u001b[38;5;240m      @\u001b[38;5;22m:..%%...@--#+.:\u001b[38;5;240m@                                
\u001b[38;5;137m      @%*@:.......@*%@\u001b[38;5;240m      @\u001b[38;5;22m:.......##*%-.:\u001b[38;5;240m@                                
\u001b[38;5;137m       @@@:......:@@@@\u001b[38;5;240m      @+=============+@\u001b[38;5;101m  @@@   @@\u001b[38;5;240m                      
\u001b[38;5;137m         @@@@#=#@@@\u001b[38;5;240m            @+:::::::*@\u001b[38;5;101m    @*.=@@@@@\u001b[38;5;240m                      
            @%-=@              @@%%%%%%%@@\u001b[38;5;101m    @=...+@@    @@@\u001b[38;5;240m                
            @@--@@                @#+#@\u001b[38;5;101m       @@%*%%.*@@ @%-@@\u001b[38;5;240m               
             @+-%@                @#+#@\u001b[38;5;101m        @=::#++%@ @@@@@\u001b[38;5;240m               
             @*-%@                @#+#@\u001b[38;5;101m        @=::#@     @@\u001b[38;5;240m                 
             @#-*@\u001b[38;5;137m        @+-----------------------------------+@\u001b[38;5;240m            
             @%-=@\u001b[38;5;137m        @=...................................-@\u001b[38;5;240m            
              @--@@\u001b[38;5;137m    @@@@#***********************************#@\u001b[38;5;240m            
              @%*%@@@@@@*+++\u001b[38;5;137m%-:::::::::::::::::::::::::::::::%@\u001b[38;5;240m              
             @#+++##---%*+++\u001b[38;5;137m%-:::::::::-------------:::::::::%@\u001b[38;5;240m              
              @%#%@@@@@@*+++\u001b[38;5;137m%-::::::::=%-:::::::::+%:::::::::%@\u001b[38;5;240m              
                       \u001b[38;5;137m@@@@@@-::::::=%%+%........-@#@%%%#::::%@\u001b[38;5;240m              
                            \u001b[38;5;137m@#****%%--#@@%******#@@%%*+++@***%@\u001b[38;5;240m              
                             @@@#-=#@@\u001b[38;5;137m         @@@%+##++*%*%@@@              
\u001b[38;5;136m                         @@%@*-+%@@\u001b[38;5;137m        @@@\u001b[38;5;240m%+-+#@@@@@@@@#=-*%\u001b[38;5;101m@@@\u001b[38;5;240m          
\u001b[38;5;136m                         @*+#@@@\u001b[38;5;137m          @@++@@@@\u001b[38;5;101m          @@%@++%@\u001b[38;5;240m         
\u001b[38;5;136m                        @#***#@\u001b[38;5;137m          @%****%@\u001b[38;5;101m            @@****%@\u001b[38;5;240m        
\u001b[38;5;136m                        @@@@@@@\u001b[38;5;137m          @@@@@@@@\u001b[38;5;101m            @@@@@@@@\u001b[38;5;240m        
\u001b[38;5;136m                      @@#*****%@\u001b[38;5;137m        @%******%@\u001b[38;5;101m          @@******%@\u001b[38;5;240m       
\u001b[38;5;136m                      @#*%#+%#*%@\u001b[38;5;137m      @@**@*+@**@\u001b[38;5;101m         @@**%*+@**%@\u001b[38;5;240m      
\u001b[38;5;136m                      @#*#@#%**%@\u001b[38;5;137m      @@#*%%%%**@\u001b[38;5;101m          @#*#%%%**@@\u001b[38;5;240m      
\u001b[38;5;136m                       @%*****%@\u001b[38;5;137m        @@#****#@@\u001b[38;5;101m           @%****#@@\u001b[38;5;240m       
\u001b[38;5;136m                         @@@@@\u001b[38;5;137m             @@@@@\u001b[38;5;101m               @@@@@\u001b[0m         
                                                                             
                You find an old, battered rover half-buried in the ground.Its solar panels are cracked, and one wheel is barely hanging on, 
                but it might have usable parts.
                MARVIN: "Ah, a rover! Like finding a used car in the desert. Sure, it’s broken, but maybe you can give it a second chance—unlike 
                your career as an astronaut."
                  
                You dismantle the rover, salvaging some parts and gaining some knowledge about the technology. But..
                All you got was a screw.
                """)
    elif choice == "c":
        energy -= 20
        oxygen -= 10
        print(u"\u001b[38;5;54m""""
                ::::::::::::::::::::::::::::::::::::++==::::-+=+:::::::::::::::::::::::::::::::::::::
                ::::::::::::::::::::::::::::::::::=*#=++=-=-+=+*=#:::::::::::::::::::::::::::::::::::
                :::::::::::::::::::::\u001b[38;5;54m-++#++==*#@%#%%%@%%%%%%%%%%%%#%@%#-=++*=#-\u001b[38;5;54m::::::::::::::::::::::
                ::::::::::::::::::::\u001b[38;5;54m+#*#%@@%%@%%###%%%%%\u001b[38;5;8m@@%@@\u001b[38;5;54m%%%%###%%@%%%@%#*#*\u001b[38;5;54m:::::::::::::::::::::
                ::::::::::::::::\u001b[38;5;54m+*+%@%%##*########%%%%%\u001b[38;5;8m@@@@@@\u001b[38;5;54m%%%%#########**#%%@%*#-\u001b[38;5;54m:::::::::::::::::
                :::::::::::::::\u001b[38;5;54m%*+##***####%%%%%%\u001b[38;5;8m@@%@@@@@@@@@@@@@%@\u001b[38;5;54m%%%%%%#####**##+*#\u001b[38;5;54m::::::::::::::::
                :::::::::::::\u001b[38;5;54m=%+@%*++#**%%\u001b[38;5;8m@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;54m%%#*#++*#%##*\u001b[38;5;54m::::::::::::::
                ::::::::::::\u001b[38;5;54m@**%#**+**#%\u001b[38;5;8m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;54m%%##*+*#%#=@=\u001b[38;5;54m::::::::::::
                :::::::::::\u001b[38;5;54m+#+*-+-***#%%\u001b[38;5;8m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;54m%%#***-==#=*@\u001b[38;5;54m::::::::::::
                ::::::::::\u001b[38;5;54m##+==++++**#%%\u001b[38;5;8m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;54m%##*+*++=+=*@\u001b[38;5;54m:::::::::::
                :::::::\u001b[38;5;54m@@@%##%#*#%-==+=%\u001b[38;5;8m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;54m=+=--%%*#%###@@%+\u001b[38;5;54m:::::::
                ::::::\u001b[38;5;54m*%%*%@**%@%#*###+++*\u001b[38;5;8m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;54m#+++######@@*#@%#%%#\u001b[38;5;54m:::::::
                ::::::\u001b[38;5;54m#@@@@@@@@##=#*+*@=**#*=+*--=%@@@%++++++@%@@@=:+=+=+##+-%%++#+*#@@@@%@%@%\u001b[38;5;54m:::::::
                ::::::\u001b[38;5;54m*%@%#%@#%%##*#*+=+#@@@%@-####%+*+--=+=-+++%@*##+%@%%@#*=++#*##%%#%%%#@@#\u001b[38;5;54m:::::::
                ::::::::\u001b[38;5;54m-=*#@%%@#@@%#+#%%@#@%=*++%#@-*+==::-=*=+@@#*=*=#@#@@@##*#@@%@%%%%#+-\u001b[38;5;54m:::::::::
                :::::::::::\u001b[38;5;54m#%@###%#++####%@%%=*##+@@##-*-=-+=:*#@@**#*-#%@#%###*+*%%*#@@%\u001b[38;5;54m::::::::::::
                :::::::::::::::::\u001b[38;5;54m*@%#*%@@@%**=#+**@@@%+****#*=#@@@#*#*=*+%@@@@##%%%\u001b[38;5;54m::::::::::::::::::
                :::::::::::::::::\u001b[38;5;54m*@+*@@#*%%%#*@%%@@@**+#=+=+++**@@@#@%**%@#%#@@#*#%\u001b[38;5;54m::::::::::::::::::
                ::::::::::::::::::::::::::\u001b[38;5;54m%**%%%##@@@@*@###%%+%@@@%#%%@**%*\u001b[38;5;54m::::::::::::::::::::::::::
                :::::::::::::::::::::::::::::::::::\u001b[38;5;54m@*#@@#++*@@##@*\u001b[38;5;54m:::::::::::::::::::::::::::::::::::
                :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                \u001b[0mOoh, a crater. It’s either a treasure trove of resources, or your tomb. Let’s find out!
                You descend into the crater, the walls rising high above you. The ground is uneven and treacherous, but you press on, driven by curiosity and necessity.
                MARVIN: "Congratulations! You found… a rock. I hope you’re happy."
                You peer deeper, but there’s nothing here except disappointment.
                """)
    elif choice == "d":
        print(u"\u001b[38;5;237m""""
                --------------------------------------------------------------
                -----------------------\u001b[38;5;18m*@@@@%*+===\u001b[38;5;8m----------------------------
                --------------------\u001b[38;5;18m*@#=-----======*%@*\u001b[38;5;8m-----------------------
                -----------------\u001b[38;5;18m=%@+-----------------+@@@@*\u001b[38;5;8m------------------
                --------------\u001b[38;5;18m=%@#=---=*=---------------%@=*%%=\u001b[38;5;8m---------------
                ------------\u001b[38;5;18m*@*=-----=*%%-----+%%+-------+@%*+%@+=**=\u001b[38;5;8m---------
                ----------\u001b[38;5;18m=@#---------==----*#=--%*--------%@%%@%*==+%%\u001b[38;5;8m-------
                ----------\u001b[38;5;18m%%---------------%=-*###=%-------*----------*@=\u001b[38;5;8m-----
                -------\u001b[38;5;18m=%@%---------=------=%%%**%%+----------=@%%=---*+@\u001b[38;5;8m-----
                -----\u001b[38;5;18m=%%=@*-------%@%@=-------++=-------------*@#@@---**%%\u001b[38;5;8m----
                ----\u001b[38;5;18m*@=-=%--------%*@@=------------------------=##---=+=*@=\u001b[38;5;8m---
                ---\u001b[38;5;18m*@=--==------------------------------------------+*%-*@=\u001b[38;5;8m---
                --\u001b[38;5;18m#@-------------------------------------===--------==--*@%%\u001b[38;5;8m--
                -\u001b[38;5;18m*@----*=-------------=+*+=------------=#--=*@=-----=*=-##=*@\u001b[38;5;8m-
                \u001b[38;5;18m=@+--=%#---=*##------@=---=%%=---------=#--+%@@#-----==-%+%%@+\u001b[38;5;8m
                \u001b[38;5;18m*@--+%%=---+%@*-----%+------=@=---------%*-*@@@%--------%%@%%#\u001b[38;5;8m
                \u001b[38;5;18m%*-=#*==-----------+%----=#*#@=----==-----=%@@+---------#%@%#%\u001b[38;5;8m
                \u001b[38;5;18m%*-=*#+------------=%+-=*##%%@=--=--=-=-=-----------%@@%*+@%*%\u001b[38;5;8m
                \u001b[38;5;18m%*--%*=--------------+@%+#%@@=---------------------***%@+*%%*%\u001b[38;5;8m
                \u001b[38;5;18m*@---%=------=%%%*-----===--------------------------=**+=+**#%\u001b[38;5;8m
                \u001b[38;5;18m=@*---*-----%=--=+%------------*@*===+%+----------=*=*=*##@=@#\u001b[38;5;8m
                -\u001b[38;5;18m=@---------*#*%%%%-----------=@=--*%%%@=-------+*+*+**#%%**@=\u001b[38;5;8m
                --\u001b[38;5;18m+@=--*-----*@@%=------------%+-=*%%%@*------=*+++++=#%@*#@=\u001b[38;5;8m-
                ---\u001b[38;5;18m=%*-%-----------------*#=--=%#=*%%#%-------+===*++*%@+@%=\u001b[38;5;8m--
                -----\u001b[38;5;18m=%@#--------------*%=@#----=%%%%%=----==----+*%%@#*@#\u001b[38;5;8m----
                -------\u001b[38;5;18m=@+-------------=*#+-------------------+#*+**#@@*\u001b[38;5;8m------
                --------\u001b[38;5;18m=@*----------------------------------+%-=%%*\u001b[38;5;8m----------
                ---------\u001b[38;5;18m=@#-=#*=----------------++--------=%@%#%=\u001b[38;5;8m------------
                -----------\u001b[38;5;18m%@++*=-----=+=-------%#@#-----=#%%*@#\u001b[38;5;8m--------------
                ------------\u001b[38;5;18m=%@+---#%##%*%%#=----*+----=%#@*@%=\u001b[38;5;8m---------------
                ---------------\u001b[38;5;18m#@%+**%#%##*=+*=+-==---#*+%@#\u001b[38;5;8m------------------
                ------------------\u001b[38;5;18m+%@@@%+===-==---==+%@@*\u001b[38;5;8m---------------------
                -------------------------\u001b[38;5;18m=*#%@@@@%%+\u001b[38;5;8m--------------------------
                --------------------------------------------------------------
                \u001b[0mA jagged asteroid sits nearby, shimmering faintly with minerals. 
                MARVIN : "An asteroid! Grab your tools, champ!"
                You approach the asteroid, hammer in hand. "
                Crack. Thump. Something hard. Grrr drr.  
                Dust and rock fell away, revealing an ancient inscription. 
                "Well, well," Marvin chuckled, "looks like you found a message from the ancients.  Let's see...oh, it's a riddle THAT GIVES YOU WATER?!? 
                """)
        if riddle_game():
            print("You are now hydrated and can continue your journey.") 
        else:
            print("You missed the water opportunity.  Better luck next time.") 
        energy -= 20
        oxygen -= 10
        water += 1

    elif choice == "e":
        game_e() # Call the game_e function
        food += 20
        energy -= 10
        water += 20
        print(u"\u001b[38;5;237m""""                                                                                 
          ------------------------------------------------------------------------------------------------------------          
          ------------------------------------------------------------------------------------------------------------          
          ------------------------------------------------------------------------------------------------------------          
          ------------------------------------------------------------------------------------------------------------          
          ---------------------------------------------------------------------------------------\u001b[38;5;15m=*@@@@#**@@\u001b[38;5;237m----------          
          --------------------------------------------------------------------------------\u001b[38;5;15m=*@@@@#+===@@@@@+\u001b[38;5;237m-----------          
          -------------------------------------\u001b[38;5;15m%@@=---------------------------------\u001b[38;5;15m=#@@%====+%*+@@@%*@*\u001b[38;5;237m--------------          
          -------------------------------------\u001b[38;5;15m=*@#\u001b[38;5;237m--=*@@@%##+===*%#@%@@@@@@@==#@@**++#@%#%*\u001b[38;5;15m%@@@%**@#\u001b[38;5;237m=----------------          
          ---------------------------------------=@@*+----=#*@%**@@@@@+@@@@@#\u001b[38;5;237m=---------\u001b[38;5;15m=@@@@*=*%@*\u001b[38;5;237m=-------------------          
          ------------------------------------*@*+*=%=%====+@%@#%@@@@@@+%#+*-=-=*=\u001b[38;5;249m+*@@@@=--=%@\u001b[38;5;237m=-----------------------          
          ----------------------------------@@*%%@*@=*+*@@@@@@@@@@*=+=--*%@*=-=\u001b[38;5;0m@@@@%-==@+@@\u001b[38;5;237m=--------------------------          
          --------------------------------*@=-*+#+##\u001b[38;5;250m@@@\u001b[38;5;237m@@=%@@@**==+==*=*%**\u001b[38;5;249m@@@@**=--+@@*\u001b[38;5;237m------------------------------          
          -------------------------------#%-==*%\u001b[38;5;250m@@@\u001b[38;5;237m@@@@@@%+=-----==%*+\u001b[38;5;249m#@@@@+-==-=@@@@@@\u001b[38;5;237m=------------------------------          
          ------------------------------*@=*\u001b[38;5;250m@@@\u001b[38;5;237m@@@@@@*=**=*===---=\u001b[38;5;15m@@@@**@**=+@@@@@@@@\u001b[38;5;237m=--------------------------------          
          -----------------------------=@@@@@*\u001b[38;5;250m@@@##+*%===%%=*%\u001b[38;5;15m@@@@@+****+@@@@@@@@**@*\u001b[38;5;237m=--------------------------------          
          ----------------------------%@@*@@@*=%*@*+#=%@+\u001b[38;5;15m@@@@*====#+#@@@@@@@@#===*@*\u001b[38;5;237m====------------------------------          
          ----------------\u001b[38;5;94m=@@@@=\u001b[38;5;237m------+@@@=**-+-=+#@=\u001b[38;5;15m@@@@=+=%=-=@@@@@@@@@@=*%=++@#\u001b[38;5;237m----------------\u001b[38;5;94m+@@=\u001b[38;5;237m----------------          
          ---------\u001b[38;5;94m=*%%%@=-----=\u001b[38;5;237m*=*@@@%-*=##*+=@*\u001b[38;5;249m@@@%*++===*@@@@@@@@@@\u001b[38;5;237m=====*%@*+*\u001b[38;5;94m=+++++====+#@@@@@*++====*@@@*@*\u001b[38;5;237m------          
          ------\u001b[38;5;94m*@%+**#\u001b[38;5;15m%@@@@@@@@%%@*+\u001b[38;5;237m+==***%@@@@*+#*@%*%@@@@@@@@@@%%*%%#%@+==+\u001b[38;5;94m***#**+=-=+==**=--=*=+=----=+====#@#\u001b[38;5;237m----          
          -\u001b[38;5;94m*@@*=--==------=****##**+======--------------+-=******+=+==+\u001b[38;5;7m=**=*==*****=+**+**##*=\u001b[38;5;94m-----=------=+=---=+@@--          
          \u001b[38;5;94m=@@=---=--=--=+=----------=====-+-*#==+**#**=--------------=====\u001b[38;5;94m-----------------=*--*------=*****==*#@@%=\u001b[38;5;237m--          
          ---\u001b[38;5;130m===++*@@#+==+\u001b[38;5;15m*##%%%%#**=\u001b[38;5;130m---------------=------=+=-----===---------==---=*=--------*=--=*=*##==+--+@%\u001b[38;5;237m-----          
          -------\u001b[38;5;130m*@+----------------=---------*+--==-------=\u001b[38;5;15m***+\u001b[38;5;130m==========-==-----------=*###***#@@@@@@@@@@%+\u001b[38;5;237m=--------          
          -----------=\u001b[38;5;130m*%@@@@@@@@#*+=======+==============================-=---==-======#@@@=\u001b[38;5;237m--------------------------          
          ------------------------------------------------------------------------------------------------------------          
          ------------------------------------------------------------------------------------------------------------          
                                                                                                             
        \u001b[0m"The light of life covers you blind, just like a cat that steals sausage, You made it quick
        back to your spaceship. You have made it back safely but you are still in danger. It wont be long before you run out of supplies.
        """)

    available_choices.pop(choice, None)

    print(f"----------------------------------------------------\noxygen:{oxygen} | water:{water} | food:{food} | energy:{energy} | score:{score}\n----------------------------------------------------")
    # Check for depleted resources
    if not check_depleted_resources(username):
        return False  # Exit if game over

    
    if energy <= 0:
        print("\nGame Over: You ran out of energy!")
    elif food <= 0:
        print("\nGame Over: You ran out of food!")
    elif oxygen <= 0:
        print("\nGame Over: You ran out of oxygen!")        
    elif water <= 0:
        print("\nGame Over: You ran out of water!")
    else:
        print("Hooray! You have successfully explored Mars!... for today, I suppose.")
#explore_mars()



#----------------------------------------------END-----------------------------------------------------------------------------
#---------------------------------------SYAHIRAH'S CONDITION (FIX SPACESHIP)---------------------------------------------------
#introduction everytime the player need to fix the spaceship
Instruction = """
\nTime to fix the spaceship!!! 
There are 5 things to repair and you can only choose one per day. 
Where do you wish to go?
\nChoose your action : 
a. power supply room
b. oxygen tank
c. main room
d. spaceship body
e. toilet
"""

#asking the player where do they wish to fix. Each place have different problems and the player need to make a choice.
def InsideSpaceShip():
    import time
    directions = ["a", "b", "c", "d", "e"] # acceptable input
    time.sleep(2) 
    print(Instruction)
    while True:
        InputDirection = input("Enter your choice :").lower() #useer's input
        if InputDirection == "a":
            PowerSupplyRoom() #go to the power supply room
            break
        elif InputDirection == "b":
            OxygenTank() #go to the oxygen tank
            break
        elif InputDirection == "c":
            MainRoom() #go to the main room
            break
        elif InputDirection == "d":
            SpaceshipBody() #go to the spaceship body
            break
        elif InputDirection == "e":
            Toilet() #go to the toilet
            break
        else:
            print("Please enter correct directions") # if the input != available input
            
        
#if player choose to fix the power supply room           
def PowerSupplyRoom():
    global energy
    import time

    print("You went into the power supply room. Suddenly, the light started flickering.")
    print("Marvin : Dude did you forget to pay the electric bill? How am I supposed to charge myself you human")
    #add delay in the execution of a program.
    time.sleep(2)
    # Code for the game (number sequence)
    def math_puzzle(sequence, correct_answer):
        attempts = 3  # maximum incorrect answer
        global score
        #The player can only play if the attempts is more than 0
        while attempts > 0:
            try:
                answer = int(input(f"Solve the sequence: {sequence} (What’s the next number?): "))
            except ValueError: #If player enter invalid value
                print("Enter a valid integer!")
                continue

            #Check the player's answer
            if answer == correct_answer:# if the answer is correct
                print("Correct!")
                score += 20
                return True
            else: #if incorrect answer
                attempts -= 1 #minus number of attempts if player enter wrong answer
                print(f"Incorrect. You have {attempts} attempts left.")

        print("You lose!")
        #add delay in the execution of a program.
        time.sleep(4)
        print("Suddenly, the lights are back on")
        print("Marvin : Dang, you played for nothing")
        return False

    def PowerSupplyGame():
        print("""
                The lights are flickering... Solve the math puzzle to stabilize the system.
                You need to guess the next number of the sequence.
        """)
        print("Marvin : You better prepare a calculator\n")
        
        
        #Puzzle 1
        sequence = "3, 6, 12, 24, ___"
        correct_answer = 48  # The correct answer for the sequence
        
        if not math_puzzle(sequence, correct_answer):
            return  # End the game if they fail the first puzzle
        
        #Puzzle 2
        sequence = "17, 34, 51, 68, ___"
        correct_answer = 85  # The correct answer for the sequence
        
        if not math_puzzle(sequence, correct_answer):
            return  # End the game if they fail the second puzzle
        
        # if the player successfully answer everything
        print("\nYou solved all the puzzles! The lights are fully restored.")

    PowerSupplyGame()

    energy -= 20
    inventory.append("water_packet")
    print(f"----------------------------------------------------\noxygen:{oxygen} | water:{water} | food:{food} | energy:{energy} | score:{score}\n----------------------------------------------------")  

    # Check for depleted resources
    if not check_depleted_resources(username):
        return False  # Exit if game over

#if player choose to fix the oxygen tank
def OxygenTank():
    global oxygen
    global energy
    global score
    print("You enter the room with the oxygen tank and notice it's old and rusted. As you approach it, the machine suddenly starts to smoke.")
    print(u"\u001b[38;5;14m""""

 ---------------------------------------------------::@.  :--:       :*    -------------------------------------------- 
 ----------------------------------------------------: -@:     @@@ @@. :@@ -------------:     :------------------------ 
 --------------------------:::::::--------------------:  :@  @@ @@ @@ .    -------------  @@@  ------------------------ 
 --::---------------------:     :   :-------------:.      @@@@@.      :---------------:  @=:@@ -------------------:---- 
 -----------------------:   @@% @@@  ------------:  =@@@%-@@@%:::@@@%    :-----------:  @@@@@  ------------------------ 
 ---:-------------------: @@ @  @  @ ----------:   @-   .@@@@@@@@   =@@@       :::::.  @      :--------------------:--- 
 ------------------------  @%     @@ ----------  @@:@@@@-.     .%@@@: %@@@@@@@        @   :---------------------------- 
 ------------------------:   @% @#   ---------- %@@:     ....     *@@* @.   @@@@@=@@=@@@@    :------------------------- 
 --------------------------: @  @   :---------: @: .\u001b[38;5;65m+@@@@@@@@@@@@%.  \u001b[38;5;14m..@ :.@   +  @  @ @::@@   :----------------------- 
 -----------------------:    @ @@@+  ---------: @.:=:..         .:-==-.@   @@@@@@@@@@@@* -@:@@  :---------------------- 
 -----------------------: @@@@@  @:@ ---------  @ .  ..-----::.. ....:: @@@@@   @@@@  *@@@. :@@  ---------------------- 
 -------------:-::-::::-. @  *@@@@@@  :------: @@ @@@@  .=%%-..@@@ @@== @  @ @@-.  .:=.   #@  .@  :::-::::------------- 
 -------------::::::::::. @@% @ @  @   :----:  @@   @@@@@-  %@@@@@  .:= @  @@@ ....-:.. ... @=.@# ::::::::------------- 
 -----------------------: @@@@@ @ :@:@        @@=.= @    *@ @@@@@@ :=== @. @@:.: @%-:@@ @*- @@ *@  -------------------- 
 ------------------------    @  @@@  @@@@@@@@@ @ := @@#  :@@@  @@@.:=== @  :@ =@@@.-:-@@=   @@. @%  ------------------- 
 --------------------------: @  @ @@@@  @.. @  @ == @@@@@@@  @ @ %.:=== @  @@ +. .*=-- @@@@@ .*#-@@ :------------------ 
 --------------------------: @@@@   @@@@@@@@@@*@ == @@@   %@@ % .@.:=== @  @* :..::::: @: #* .::.:@ :------------------ 
 --------------------------:  .:  :            @ == @@@@@  @@@:  @.:=== @  @@ :@@  @#... @@:@.    @ :------------------ 
 ---:-------------:      ----:   ------::   :  @  .   :@=@@.  @@+@ .:== @  @@ @*=@@=#@@% @  @@@@@@@ :-------------::--- 
 ----------------\u001b[38;5;7m   =@@@ \u001b[38;5;14m:----         .- @@=@@@ @@@:-: ....:::  @@@:== @ .+@ ...  .. .@@@%@@% =@   :------------------ 
 ----------------\u001b[38;5;7m @@#@@@=\u001b[38;5;14m:---- @@ @@@ # - @@@@@@   .:===++=++=+*=:..:== @ ..@ ..:=====:.  @  @@@  :-------------------- 
 ----------------\u001b[38;5;7m  @@@*  \u001b[38;5;14m:---  @  -  @@        @-.-==================== @: *@@@@+-:.      -@@         :---------------- 
 ----------------:      ::--- @@ @@@  @@       @@#-:..:==============-. @#:@*    .%@@@@@@@# \u001b[38;5;7m   @@  @@  \u001b[38;5;14m:--------------- 
 ----------------------------  :@ +@ @  =@@@@@    %@@@@+-:.     ..::=+@@@@*    @@@@@        .\u001b[38;5;7m @ @@@ @@ \u001b[38;5;14m:--------------- 
 -----------------------------:  = .   @=:@@@@@@        +@@@@@@@@@@%=       :- #@@@  ...:---.:\u001b[38;5;7m@ @@@@@@ \u001b[38;5;14m:--------------- 
 ----------------:.:.::::------:    @@@@@:    %@@    @@@@         @@*@@  .:.             :--:\u001b[38;5;7m  @@@@@@  \u001b[38;5;14m:--------------- 
 ----------------: . .   :---:   @@@::. .:@@@:  @= @@@@@@@ -:  @@@=:@-@@ -- @= @@@@:@*@@     .        :---------------- 
 ----------------\u001b[38;5;7m .@:=%@ \u001b[38;5;14m.--:  @@:..:====-::...@@   @:*@*  :  @@@@. +@   :- :@@@@%@@@@@@@@@@-:------------------------- 
 ----------------\u001b[38;5;7m @@*@@@ \u001b[38;5;14m.--: @*  :---:.. ..:@@    %@@    :  @     @#  :---:                 :------------------------- 
 ----------------\u001b[38;5;7m  *==.  \u001b[38;5;14m:--: =@@@@%%%@@@@@%%%@@@@+@@ *@  - @@ @@@@@               :----------------------------------- 
 ----------------:.    ::----.          %@@%:.. @:  @@ @@ -  @@    :@@@*  :@@=@@@@  :---------------------------------- 
 :::::::-:-------------------.   @@@@@@*:.@. == -@  %@@@@ -:  @@:+@-  =@@@@ :@.  -@ .:::::::-----------------------:--- 
 :-::-:-::------------------- *@-:. #@ :-..@  ::@@@@%           *@@+=@@ @= @@..=:.@ .::-:--:--------------------------- 
 ----------------------------  @@-.: @:   =@@@@@    \u001b[38;5;7m    @@@@  \u001b[38;5;14m-.      .@* @@ :==.:@ .---------------------------------- 
 ----------------------------: @ @.::@@@@@=      ::\u001b[38;5;7m @@@@@-  @ \u001b[38;5;14m----::.  @ =@ :=-. @@ :---------------------------------- 
 -----------------------------  *@@@@*     .:-----:\u001b[38;5;7m @@@-@@@@= \u001b[38;5;14m------- @@ @*.=:.-@@  ----------------------------------- 
 -----------------------------:        ::---------:          :------- @@ @...:@@   ------------------------------------ 
 -----------------:-------------------------------------------------- =@-@:@@@   :-------------------:----------------- 
  
          """)
    print(u"\033[0m")
    print("Quick! To fix the oxygen tank, you need to guess the correct number starting from 0 to 50")
    
    import datetime
    import random
   
    #code for the game
    timer = datetime.datetime.now() + datetime.timedelta(seconds=30) #setting timer to be 30 seconds from current time
    target = random.randrange(51)  # Generate a random number between 0 and 50

    print("\nOh I forgot to mention that you only have 30 seconds!")

    while True:
        try:
            guess = int(input("Enter a number between 0 to 50: "))
        except ValueError:  # if player enters invalid value
            print("Enter an integer!")
            continue

        # Calculate the remaining time
        remaining = (timer - datetime.datetime.now()).total_seconds()

        # Check if the time is up
        if remaining < 0:
            print("Too late! You lost!")
            energy -= 20
            print(f"----------------------------------------------------\noxygen:{oxygen} | water:{water} | food:{food} | energy:{energy} | score:{score}\n----------------------------------------------------")
            if not check_depleted_resources(username):
                break #Break if there's depleted resource
            break #break after player lose

        if guess < target:
            print("Too low!")  # The guess is too low
            print(f"{remaining:.0f} seconds left before you lose!\n")
        elif guess > target:
            print("Too high!")  # The guess is too high
            print(f"{remaining:.0f} seconds left before you lose!\n")
        else:
            print("You got it!")
            oxygen += 100
            score += 50
            print(f"----------------------------------------------------\noxygen:{oxygen} | water:{water} | food:{food} | energy:{energy} | score:{score}\n----------------------------------------------------")
            if not check_depleted_resources(username):
                break #Break if there's depleted resource
            break #break after player wins

            
      

#if player choose to go to the main room
def MainRoom():
    global energy
    global food
    global score
    import time

    print(u"\u001b[38;5;249m""""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%\u001b[38;5;249m@\u001b[38;5;60m%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%\u001b[38;5;249m@\u001b[38;5;60m%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%\u001b[38;5;249m@@@\u001b[38;5;60m%\u001b[38;5;249m@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%\u001b[38;5;249m@@\u001b[38;5;60m%%\u001b[38;5;249m@@\u001b[38;5;60m%\u001b[38;5;249m@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@@@\u001b[38;5;60m%%\u001b[38;5;249m@@@@@@@@@@@@@@
@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@
@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%\u001b[38;5;249m@@@@@\u001b[38;5;60m%\u001b[38;5;249m@@@@@@@@@@@@@
@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%\u001b[38;5;249m@@@@@@@\u001b[38;5;60m%\u001b[38;5;249m@@@@@@@@@@@@
@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%\u001b[38;5;249m@@@@@@\u001b[38;5;60m%\u001b[38;5;249m@@@@@@@@@@@@
@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%\u001b[38;5;249m@@@@\u001b[38;5;60m%%\u001b[38;5;249m@@@@@@@@@@@@
@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@
@@@@@@@@\u001b[38;5;60m%%%%%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%%%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%%%%%%\u001b[38;5;249m@@@@@@@@
@@@@@@\u001b[38;5;60m%%%%%%%%%%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%%%%%%%\u001b[38;5;249m@@@@@@@@
@@@@@@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%%%%%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@@\u001b[38;5;60m%\u001b[38;5;249m@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%%%%%%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@\u001b[38;5;60m%\u001b[38;5;249m@@\u001b[38;5;60m%%%%%%%%%%%%%%%%%%%%%%\u001b[38;5;249m@@@@@@@@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;249m@\u001b[38;5;60m%%%%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%%%%%\u001b[38;5;249m
@@@@@@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%%%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m\u001b[38;5;249m@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\u001b[38;5;249m@@@@@@@@\u001b[38;5;60m%%\u001b[38;5;249m@\u001b[38;5;60m%%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@@@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m
@@@@@@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%%\u001b[38;5;249m@@\u001b[38;5;60m%\u001b[38;5;249m@@@@@@@@@@@\u001b[38;5;60m%%%\u001b[38;5;249m@@@\u001b[38;5;60m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\u001b[38;5;249m@@@@@@@@@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@@@@@@@@
\u001b[38;5;60m%%%%%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@@\u001b[38;5;60m%\u001b[38;5;249m@@@@@@@@@@@\u001b[38;5;60m%%%%%%\u001b[38;5;249m@@@@\u001b[38;5;60m%%\u001b[38;5;249m@\u001b[38;5;60m%%%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%\u001b[38;5;249m@\u001b[38;5;60m%%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%%%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@\u001b[38;5;60m%\u001b[38;5;249m@@\u001b[38;5;60m%%\u001b[38;5;249m@@@@@@@
@@\u001b[38;5;60m%%%\u001b[38;5;249m@\u001b[38;5;60m%%%%%%\u001b[38;5;249m@@@@@@\u001b[38;5;60m%%%%%%%%%\u001b[38;5;249m@@@\u001b[38;5;60m%%%%%%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@@\u001b[38;5;60m%%%%%%\u001b[38;5;249m@@\u001b[38;5;60m%%%%%%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%%\u001b[38;5;249m@@@\u001b[38;5;60m%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%%%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%%%%%%%%%%%\u001b[38;5;249m@@@@\u001b[38;5;60m%%%%%\u001b[38;5;249m@@@@@\u001b[38;5;60m%%\u001b[38;5;249m@@@@@@@
@@@\u001b[38;5;60m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%%%%%%%%%\u001b[38;5;249m@@\u001b[38;5;60m%%%%%%\u001b[38;5;249m@@@@\u001b[38;5;60m%%%%%\u001b[38;5;249m@\u001b[38;5;60m%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@@@\u001b[38;5;60m%%%%%\u001b[38;5;249m@@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%%%%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@@@@\u001b[38;5;60m%%%%%\u001b[38;5;249m@@@@@\u001b[38;5;60m%%\u001b[38;5;249m@@@@@
@@@\u001b[38;5;60m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%%%%%%%\u001b[38;5;249m@@\u001b[38;5;60m%%%%%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%%%\u001b[38;5;249m@@@@@\u001b[38;5;60m%%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%%%%%%%%%%%%%%%%%%%%\u001b[38;5;249m@@@@@@@@@\u001b[38;5;60m%%%%%%%%\u001b[38;5;249m@@@@
@@\u001b[38;5;60m%%\u001b[38;5;249m@\u001b[38;5;60m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%%%%\u001b[38;5;249m@@@@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@@@@@@@@@@\u001b[38;5;60m%%%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%%%\u001b[38;5;249m
\u001b[38;5;60m%%%%%%%%%%%%%%%%%%%%%%\u001b[38;5;249m@@@\u001b[38;5;60m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\u001b[38;5;249m@@@@@@@@\u001b[38;5;60m%%%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%%%%\u001b[38;5;249m
\u001b[38;5;60m%%%%%%%%%%%%%\u001b[38;5;249m@@@@\u001b[38;5;60m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\u001b[38;5;249m@@\u001b[38;5;60m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%%%%%%%%%%%%%%\u001b[38;5;249m@@@\u001b[38;5;60m%%%\u001b[38;5;249m@\u001b[38;5;60m%%%%\u001b[38;5;249m
\u001b[38;5;60m%%%%%%\u001b[38;5;249m@@@@\u001b[38;5;60m%%%%%%%%%%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%%%%%%%%%%%%%%%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%%%\u001b[38;5;249m@\u001b[38;5;60m%%%\u001b[38;5;249m@\u001b[38;5;60m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\u001b[38;5;249m@@@\u001b[38;5;60m%%%%%%%%%%%%%%%%\u001b[38;5;249m
\u001b[38;5;60m%%%%%%%%%%%%%%%%%%\u001b[38;5;249m@@@@@@@@@@\u001b[38;5;60m%%%%%%%%%%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%%%%%%%%%%%%%%%%%%%\u001b[38;5;249m@@@@@@@@@\u001b[38;5;60m%%%%%%%%%\u001b[38;5;249m
\u001b[38;5;60m%%%%%%%%%%%\u001b[38;5;249m@@@@@@\u001b[38;5;60m%%%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%%%%%%%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%%%%\u001b[38;5;249m@@@@@\u001b[38;5;60m%\u001b[38;5;249m
\u001b[38;5;60m%%%%\u001b[38;5;249m@@@@@@\u001b[38;5;60m%%%%%%%%\u001b[38;5;249m@@@@@\u001b[38;5;60m%%%%%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%\u001b[38;5;249m@@@@@@@@\u001b[38;5;60m%%%%%%%%%%%%%%%%%%\u001b[38;5;249m
\u001b[38;5;60m%%\u001b[38;5;249m@@@\u001b[38;5;60m%%%%%%%\u001b[38;5;249m@@@@@@\u001b[38;5;60m%%%%%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%%\u001b[38;5;249m@\u001b[38;5;60m%%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%\u001b[38;5;249m@@\u001b[38;5;60m%\u001b[38;5;249m@@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%%%%%\u001b[38;5;249m@@\u001b[38;5;60m%\u001b[38;5;249m@@@@@@@@\u001b[38;5;60m%%%%%%%%%%%%\u001b[38;5;249m
\u001b[38;5;60m%\u001b[38;5;249m@@@@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@@\u001b[38;5;60m%%%%%%%%%%%%%%%%%\u001b[38;5;249m@@\u001b[38;5;60m%\u001b[38;5;249m@@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\u001b[38;5;60m%%\u001b[38;5;249m@\u001b[38;5;60m%%\u001b[38;5;249m@\u001b[38;5;60m%%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%%%%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%%\u001b[38;5;249m@\u001b[38;5;60m%\u001b[38;5;249m@@@\u001b[38;5;60m%\u001b[38;5;249m@@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%%%%%\u001b[38;5;249m
\u001b[38;5;60m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\u001b[38;5;249m
\u001b[38;5;60m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%%%%%\u001b[38;5;249m@\u001b[38;5;60m%%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%%%%%%\u001b[38;5;249m@\u001b[38;5;60m%%%\u001b[38;5;249m@@\u001b[38;5;60m%\u001b[38;5;249m@\u001b[38;5;60m%%\u001b[38;5;249m@\u001b[38;5;60m%%%\u001b[38;5;249m@\u001b[38;5;60m%%%\u001b[38;5;249m@\u001b[38;5;60m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\u001b[38;5;249m
\u001b[38;5;60m%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\u001b[38;5;249m
    """)
    print(u"\033[0m")
    print("You are now in the main room. You are allowed to call someone and ask for their help.")
    print("Marvin : So who are you calling? Are you going to pick someone who can actually help you out of this mess, \nor are you just going to ask your mom to send you some snacks while you wait to be rescued?")
    print("""
                Welcome! In this game, you are required to guess the correct answer to all the questions.
    """)
  #code for quiz
    questions = ("How many planets are there in our solar system: ",
                          "\nWhich planets in our solar system are NOT made of rock?: ",
                          "\nMars is 2 times ____ than the Earth?: ",
                          "\nHow many moon(s) does Mars have?: ",
                          "\nWhich planet in the solar system is the hottest?: ")

    options = (("A. 5", "B. 10", "C. 8", "D. 14"),
                      ("A. Mercury", "B. Mars", "C. Earth", "D. Jupiter"),
                      ("A. smaller", "B. bigger", "C. Taller"),
                      ("A. 2", "B. 5", "C. 1", "D. 15"),
                      ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

    answers = ("C", "D", "A", "A", "B") #correct answers
    guesses = [] #all player's guess will be appended here
    score = 0
    question_num = 0

    # for each 'question' in the list, print the questions
    for question in questions:
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter (A, B, C, D): ").upper()
        while guess not in ["A", "B", "C", "D"]: # if player enter invalid answer
            print("Please input A, B, C, or D")
            guess = input("Enter (A, B, C, D): ").upper()

        guesses.append(guess) #adding the player's answer inside guesses list
        if guess == answers[question_num]:
            score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{answers[question_num]} is the correct answer")
        question_num += 1


    print("       RESULTS        ")
    #end= is to make sure the answer is printed in a line 
    print("answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()

    #end= is to make sure the guesses is printed in a line 
    print("guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

#calculating and print the score in percentage
    score = int(score / len(questions) * 100)
    print(f"\nYour score is: {score}%\n")

    #player win if the score is more than 60%
    if score >= 60:
        message = input("Enter your message here : ") #player can write a message
        print("Sending...")
        time.sleep(1)
        print("Your message is sent.")
        energy -= 20
        score += 50
    else: #if their score is less than 60%
        print ("Your score didn't reach 60%")
        energy -= 20
        food -= 5
        print(f"----------------------------------------------------\noxygen:{oxygen} | water:{water} | food:{food} | energy:{energy} | score:{score}\n----------------------------------------------------")  
        # Check for depleted resources
        if not check_depleted_resources(username):
            return False  # Exit if game over

def SpaceshipBody():
    import time 

    print("""
                You’re casually gazing outside the spaceship, when, out of nowhere, you spot it.
                A massive meteor, speeding toward you from the vast galaxy. 
                Your heart stops. You freeze in terror.
                In a panic, you scramble under the table, waiting for the inevitable collision.
    """)
    print("One...")
    time.sleep(2) #add delay in the execution of a program.
    print("Two...")
    time.sleep(2) #add delay in the execution of a program.
    print("Three...")
    time.sleep(3) #add delay in the execution of a program.
    print("""
                You can’t take it anymore. You rise, cautiously walking towards the window.
                You peek outside, holding your breath.
                BOOM!
                The spaceship shudders violently, and before you can even brace yourself, you’re sent sprawling to the floor.
    """)

    print(u"\u001b[38;5;56m""""
                                                                                                                                                                                                                                  
                                                                                                                        
            \u001b[38;5;152m %:                                                                                                         
               \u001b[38;5;152m=%*-===:-::.\u001b[38;5;56m                                                                                             
                  \u001b[38;5;152m@#*%-##=*=-=**#%%+=\u001b[38;5;56m                                                                                   
                   \u001b[38;5;152m=%%@#:= =:=+ :+**@@+++.\u001b[38;5;56m                                                                              
                     \u001b[38;5;152m@=:%.*#=-  :#@-:::+#=\u001b[38;5;159m*%@%\u001b[38;5;56m                                                                          
                      -@\u001b[38;5;152m%+:-@@@@%%::::::=\u001b[38;5;159m%#%@*#%%-\u001b[38;5;56m                                                                      
                        *%%\u001b[38;5;152m%-===***=:::\u001b[38;5;159m#@*@**=+@@@@%%=.\u001b[38;5;56m                                :-                               
                          *@@\u001b[38;5;152m*+@===-:\u001b[38;5;159m=@@-+@@%@@@+-=*@@@%%#*#\u001b[38;5;56m                      .%*.:  .*+=+:                         
                            =%*\u001b[38;5;152m@=-:=-=%-\u001b[38;5;159m.%@@@@@@@@*%*%@%%@@%=@@=\u001b[38;5;56m                    %+=       .@##:=.      %+           
                               #%\u001b[38;5;152m%%+-=@:=@*\u001b[38;5;159m::##+%@%%%*+@@*%@%#@@#=*+\u001b[38;5;56m                .:--       **%#   :@=#= .=          
                           \u001b[38;5;57m       #**\u001b[38;5;152m@@:*=    =\u001b[38;5;159m:#@@%#@@@%#%##*%@@*+*+=*=            \u001b[38;5;56m :%@%+:      =%  :+:-%+             
                              \u001b[38;5;57m       *@*\u001b[38;5;152m-::.   :%#.. - \u001b[38;5;159m=@@@@@@@@@*:      :=-=-=*#%*-\u001b[38;5;56m :====*%@%=.  \u001b[38;5;63m=  *:%%@              
                               \u001b[38;5;57m         =%#\u001b[38;5;152m=--. =    -   := ..:. :==-     :  :**:             \u001b[38;5;63m+%:*#+%**#@=              
                                    \u001b[38;5;57m       .#%#\u001b[38;5;152m--:  *===       .::.     :        :**         \u001b[38;5;57m *                         
                                               +%@*+\u001b[38;5;152m%:  **             =       .     :#:    \u001b[38;5;57m #:                         
                                                   *@@*\u001b[38;5;152m=: ..:%#.      +        .*%#+-.   := \u001b[38;5;57m *                          
                                                      .*@#\u001b[38;5;152m=.:::=:*  .:          :@%*:      \u001b[38;5;63m ::+=-:                      
                                                          :#@#=.:. . =:                    -.@@*    @@*:                
                                                               %@%--=%@**#=.              ::+=***%=   ++:*              
                                                                 %@:.::++.  .:++.        :.===*  *=: -*+@%*             
                                                                  =@%        .    %=*:. *:*@@%. #*+ +@*+.               
                                                                    ===           #=  :=#@*%@=:#:     :                 
                                                                     -@#=-            =+-=@%*-%=      =                 
                                                                         *@#+=:       +  @@@%+@@     -                  
                                                                           :%%@%*+=+++==@@%@@=                          
                                                                            -#===+%%%@*@@#                              
                                         *@*=:%===+=-:::+@+=                                
                                           @%* :: ..:.:==@%                                 
                                            #@==:          ::*:                             
                                              *%*+:..   .@: # .@*                           
                                                  .*#*=-=*-:* +@-                           
                                                       :*%+%==@#                            
                                                          +*%..        +*=::                
                                                            *@**                            
""")
    print(u"\033[0m")

    print("Marvin : OMG, WHAT WAS THAT?! I swear I nearly had a heart attack! I’m WAY too young to be facing my dramatic demise like this!\n")

    def OrderPuzzle():
      global energy
      global food
      global score
    # The correct order of words to form a sentence
      correctAnswer = ['I', 'am', 'playing', 'lost', 'in', 'Mars']
      #printing instruction
      print("TASK : Rearrange the words to repair the spaceship! You can only attempt once")
      print("You have the following words (in random order):")
      print("playing, in, am, Mars, I, lost")
      
      # Ask the player to input the words in the correct order
      player_guess = input("Enter the words in the correct order (separate by spaces): ").split()
      
      # Check if the player's input matches the correct order
      if player_guess == correctAnswer:
          print("Correct! The spaceship is repaired!")
          energy -= 10
          food += 10
          score += 50

      else:
          print(f"Incorrect! The correct order was: {' '.join(correctAnswer)}.") #display the correct order
          energy -= 20
          food -= 10

    time.sleep(2)
    OrderPuzzle()
    print(f"----------------------------------------------------\noxygen:{oxygen} | water:{water} | food:{food} | energy:{energy} | score:{score}\n----------------------------------------------------")  
    # Check for depleted resources
    if not check_depleted_resources(username):
        return False  # Exit if game over

# if player choose to go to the toilet
def Toilet():
    global energy
    global food
    global water

    print(u"\u001b[38;5;7m""""                                                                                                                                                                                                                                          
                                                                                                            
                                .    ......... .                                                               
                        ...::-=*=-::::::::::::::.                                                           
                . ..:::::::::::::::::::::::::::::::.                                                          
            ..:::::::::::::::::..::::::::::::::::::.                                                          
            :--:::::::::::::::::::::::::::---:::::. .                                                        
            :-----::::::::::::::::::--::::::::::::.                                                          
            .----===---==-::::::::::::::::::::::::.                                                          
            .:-----:::::::::::::::::::::::::::::::.                                                          
            :------::::::::::::::::::::::::::::::.                                                          
            . .------::::::::::::::::::::::::::::::.                                                          
                :-----::::::::::::::::::::::::::::::.                                                          
                .------:::::::::::::::::::::::::::::                                                           
                :-----:::::::::::::::::::::::::::::                                                           
                :-=----::::::::::::::::::::::::::::                                                           
                .------::::::::::::::::::::::::::::                                                           
                :-==--::::::::::::::::::::::::::::                                                           
                . .------:::::::::::::::::::::::::::                                                           
                :--=--::::::::::::::::::::::::::.                                                           
                :-----::::::::::::::::::::::::::.                                                           
                .------:::::::::::::::::::::::::                                                            
                    :-----::::::::::::::::::::::::..   ......  .                                               
                    .-----:::::::::::::::::::::-::.:::::::::::::...  .                                         
                    .-----::::::::::::::::::::::::::::::::::::::::::::..                                      
                    . :--:::::::::::::::::::::::::::::::::::::::::::::::::...  .                             
                        .   .:=:::::::::::::::::::::::::::::::::::::::::::::::::.                              
                            :-::::--::::::::::::::::::::::::::::::::::::::::::::..                           
                            .-=-::::---:::::::::::::::::::::::::::::::::::::::::::..                         
                            .-==-:--::--:::::::::::::::::::::::::::::::::::::::::::.                        
                                :-==-:---:--::::::::::::::::::::::::::::::::::::::::::.                       
                                .-==-::=-::::::::::.....::::::::::::::::::::::::::::.                       
                                    .:===-::--:::::::::........::::::::::::::::::::::::.                       
                                    .:*==--:::-:::::::::::::::::::::::::::::::::::::::.                       
                                    :-=+*=---::::-:::::::::::::::::.:.:::::::::::::::                        
                                .  :----=+=----:::::-:::::::::::::::::::::::::::--:                         
                                    :-===--+===--::::::::::::::::::::::::::-:::--=:.                         
                                    . ::-=====+=---==---::::::::::::::::::::-----==:                           
                                    ::--========-------==----:::::-:---------==-.                            
                                    .::--==-=-=====-----------------------=====: .                            
                                .  :::-====---======------------------=====:                                
                                    .-:::-===-----============-============.                                  
                                    .-:::---=----::-=====================:                                    
                                    ..=--:---------::-===========-----:::--.                                   
                                    .=------------:::-------::::::::::::--:  .                                
                                ...==-------::---::------::::::::::::::-:                                   
                                    .--:--------:::-:--:--:::::::::::::---.                                  
                                        .:----------:::::---::::::::::::::---                                  
                                        .::---------:----:-::::::::::::----.                                 
                                        .   .:-------------::::::::::::::---:                                 
                                            .:-------------::::::::::-----:.                                
                                                ::----------:::::::::::-----.                                
                                                    .:----------::::::::-:---:                                 
                                                    .::---:-:--:::--:::-::                                  
                                                        ..::::::-::::::..                                    
                                                            . ......                                         
                                                                                                                                                                                                                                                                                                                                    
""")
    print(u"\033[0m")
    #player gain nothing if they went to the toilet and even lose resources
    energy -=5
    food -= 10
    water -= 10
    print("Marvin : What are you even doing here? Stop wasting my precious time and go do something beneficial")
    #print available resources
    print(f"----------------------------------------------------\noxygen:{oxygen} | water:{water} | food:{food} | energy:{energy} | score:{score}\n----------------------------------------------------")  
    # Check for depleted resources
    if not check_depleted_resources(username):
        return False  # Exit if game over

#----------------------------------------------END-----------------------------------------------------------------------------

#----------------------------------------------DAY 1----------------------------------------------------------------------------
def intro_sequence_day1():
    LIGHT_PURPLE = "\033[1;35m"
    yellow  = "\033[1;33m"
    RESET = '\033[0m'  # This resets the color back to default
    # Check for depleted resources
    if not check_depleted_resources(username):
        return False  # Exit if game over

    print(f"{LIGHT_PURPLE}======================================\n{yellow}DAY 1: Oh No, We’re Really Doing This{LIGHT_PURPLE}\n======================================{RESET}")
    print("""
                Disaster has struck your Martian spaceship, leaving you trapped and fighting for life.
                With only five days on the sun till your emergency systems fail, you must brave the harsh Martian world and find a means to survive.
                Exploration is one of your only hopes to make it.
      """)


#taya's code
#Introduction to the player to make a decision on exploration mars
#Explore mars fixed choice


#Syahirah
#Fix the spaceship fixed choice


def time_coded1():
    global energy
    #Time coded Day 1- Afternoon
    print("""
                    While you are looking outside the spaceship, you spot something shiny in the distance.
        """)
    print("Marvin : Wowowow what is that? It is either a rare Martian artifact or a huge rock. Probably the later. But hey why don't you go and take a look. You love shiny things, don't you?")
    print("Do you wish to take a look?")
    while True:
        take_a_look = input("Yes/No : ").lower()
        if take_a_look == "yes":
            print("""
                    You chose to investigate the shiny object. As you walk closer, you suddenly feel a strange sensation. The object, 
                    now clearly visible, is a small mineral, its surface reflecting light in unexpected ways. It glows faintly, casting a soft,
                    otherworldly light on the surroundings. It feels out of place, like it does not belong here. Without thinking, you reach out 
                    and decide to take it.
                """)
            inventory.append("shiny_rock")
            energy -= 20
            break
        elif take_a_look == "no":
            print("""
                    You chose to ignore the shiny object and focus on completing your task.
        """)
            print("Marvin : Wow you made a rather responsible choice. Well done bro! It must be hard for you to ignore the shiny thing.")
            break
        else:
            print("Please enter a valid input")
        print(f"----------------------------------------------------\noxygen:{oxygen} | water:{water} | food:{food} | energy:{energy} | score:{score}\n----------------------------------------------------")  
        # Check for depleted resources
        if not check_depleted_resources(username):
            return False  # Exit if game over


#--------------------------------------------------------------------------------------------------------------------------------------------------
#joy 
#going to try and follow exactly as in video. which isn't a good idea if you want to learn

def hidden_maze():
    #player_hp = random.randint(120,200)
    #max_hp = player_hp
    global energy
    location = 81
    message = 'MARVIN: Escape this maze and avoid the dust storm! Good luck trying to see anything though!'

    maze = ["#", "#", "#", "#", "#", "#", "#", "#", "@", "#", 
            "#", " ", "#", "#", "#", " ", " ", "#", " ", "#", 
            "#", " ", " ", " ", " ", " ", " ", "#", " ", "#", 
            "#", "#", " ", "#", " ", "#", " ", "#", " ", "#", 
            "#", " ", " ", "#", " ", "#", " ", "#", " ", "#", 
            "#", " ", " ", " ", " ", "#", " ", "#", " ", "#", 
            "#", "#", " ", "#", " ", "#", " ", "#", " ", "#", 
            "#", " ", " ", "#", "#", "#", " ", " ", " ", "#", 
            "#", " ", "#", "#", "#", "#", "#", "#", "#", "#", 
            "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]

    map = [' ' for i in range(100)]      #to hide above map by replacing everything with ' '

    def reveal(location):
    #squares revealed is 3-by-3 so from '*' position, top left is 81 - 11  
        map[location - 11] = maze[location - 11]
        map[location - 10] = maze[location - 10]
        map[location - 9] = maze[location - 9]
        map[location - 1] = maze[location - 1]
        map[location] = '*'
        map[location + 1] = maze[location + 1]
        map[location + 9] = maze[location + 9]
        map[location + 10] = maze[location + 10]
        map[location + 11] = maze[location + 11]

        a = 0                            # to help align map/maze so it is like what's drawn above
        b = 10                           # to help align map/maze so it is like what's drawn above
        for i in range(10):              #for loop, 10 times
            print(''.join(map)[a:b])     #show space joined with 0, for x position, and 10 for y position
            a += 10                      #and then add 10 to a and b, therefore adding 10 to x and y, drawing a perfect square
            b += 10


    while True:
        print(chr(27) + "[2J")           #ANSI escape sequence to clear the terminal window
        reveal(location)                 #create map
        print("---------------------")   #divide
        print(message) 
        message = ''                     #clear message in next move
        print("\nYour energy levels are", {energy})
        print("You start as a '*'")

        print("\nType w a s or d to move.")
        choose = input("\n> ")
        x = choose.lower()

        if maze[location] == '@':    #when reach exit
            message = 'MARVIN: Wow. We actually made it out. Congrats I guess.'
            break

        #up movement
        if x == 'w':
            if maze[location - 10] == '#':
                message = "You bumped into a wall."
                energy -=2
            else:
                location -=10

        #down movement
        elif x == 's':
            if maze[location + 10] == '#':
                message = "You bumped into a wall."
                energy -=2
            else:
                location +=10

        #left movement
        elif x == 'a':
            if maze[location - 1] == '#':
                message = "You bumped into a wall."
                energy -=2
            else:
                location -=1

        #down movement
        elif x == 'd':
            if maze[location + 1] == '#':
                message = "You bumped into a wall."
                energy -=2
            else:
                location +=1
        
        #if enter any key that is not w, a, s, and d
        else:
            message = "MARVIN: Where are you moving? 4th dimensional?"
            
def event_day_1():
    global energy, food, oxygen, water, score
    print("\nA massive dust storm looms on the horizon.")
    print("MARVIN: 'This is bad. Even I don’t have a sarcastic comment for this. Prepare or perish.")
    while True:
        choice = input("Escape (E) or Stay (S)? ").strip().lower()
        if choice == 'e':
            hidden_maze()
            print("\nYou run back to the spaceship just in time!")
            print("You got a food packet too!")
            inventory.append("food_packet")
            updated_inventory = inventory 
            print(f"Updated inventory: {updated_inventory}")
            break
        elif choice != 's' and choice != 'e':
            print("MARVIN: 'I don’t know what that means, but it doesn’t sound good. Try again.'")
            continue
        else:
            print("Great! You feel like a sandwich now. -20 everything")
            energy -= 20
            food -= 20
            oxygen -= 20
            water -= 20
            break
    print(f"----------------------------------------------------\noxygen:{oxygen} | water:{water} | food:{food} | energy:{energy} | score:{score}\n----------------------------------------------------")
    # Check for depleted resources
    if not check_depleted_resources(username):
        return False  # Exit if game over


#---------------------------------------END OF DAY 1----------------------------------------------------------------------------

#----------------------------------------------DAY 2----------------------------------------------------------------------------
def intro_sequence_day2():
    # Check for depleted resources
    if not check_depleted_resources(username):
        return False  # Exit if game over
    print("======================================\nDAY 2: Martian Mondays\n======================================")

def event_day_2(inventory):
    global energy, food, oxygen, water, score
    print("A distress signal from another crash site comes through. An alien is asking for help.")
    while True:
        choice = input("Investigate (I) or Ignore (X)? ").strip().lower()
        if choice == 'i':
            if 'shiny_rock' in inventory:
                print("\nYou gave them the shiny rock so the alien helps you and teaches survival tricks.")
                print("The alien draws a map in the dust and hands it to you. You gain 50 XP!")
                print("\nWait a damn minute...you followed the map and found a hidden place of water resources!")
                print("You have got some energy packet and in your inventory!\n")
                water += 50
                energy += 50
                score += 50
                inventory.append("energy_packet")
                updated_inventory = inventory  # this is referencing the inventory into a variable
                print(f"Updated inventory: {updated_inventory}")
                break
            else:
                print("The alien runs away!")
                break
        elif choice != 'i' and choice != 'x':
            print("MARVIN: 'what was that? Try again.'")
            continue
        else:
            print("MARVIN: 'Who needs friends anyway? You’ve got me. Forever. And ever.'")
            water -= 10
            food -= 10
            break
    print(f"----------------------------------------------------\noxygen:{oxygen} | water:{water} | food:{food} | energy:{energy} | score:{score}\n----------------------------------------------------")
    # Check for depleted resources
    if not check_depleted_resources(username):
        return False  # Exit if game over
 

def time_coded2():
    global energy
    global food
    global score
    #Time coded Day 2 - night
    print("""
                    You were sitting on your bed when you suddenly noticed it felt unusually cold. You got up and
                    walked over to the control panel, only to realize the temperature had dropped significantly.
        """)
    print("Marvin : I was going to suggest you to fix the heater but honestly, I am fine with watching you turn into a popsicle.")
    print("Do you wish to fix the heater?")
    while True:
        fix_heater = input("Yes/No : ").lower()
        if fix_heater == "yes":
            print("""
                    You chose to fix the heater. After a few adjustments, the system hummed to life, and the temperature gradually began to rise
                """)
            score += 50
            energy -= 20
            break
        elif fix_heater == "no":
            print("""
                    You chose not to fix the heater. As a result, you spent the rest of the night shivering under your blankets, 
                    the cold creeping into your bones no matter how tightly you curled up.
                """)
            energy -= 10 
            food -= 10
            break
        else:
            print("Please enter a valid input")
    print(f"----------------------------------------------------\noxygen:{oxygen} | water:{water} | food:{food} | energy:{energy} | score:{score}\n----------------------------------------------------")  
    # Check for depleted resources
    if not check_depleted_resources(username):
        return False  # Exit if game over

#---------------------------------------END OF DAY 2----------------------------------------------------------------------------

#----------------------------------------------DAY 3----------------------------------------------------------------------------
def intro_sequence_day3():
    # Check for depleted resources
    if not check_depleted_resources(username):
        return False  # Exit if game over
    print("======================================\nDAY 3: Midlife Crisis on Mars\n======================================")

def time_coded3():
    global energy
    global score
    #Time coded Day3-morning
    print("""
                    You are in the ship’s control room. The ship has been quiet, and the you has grown accustomed to the isolation.
                    The calm is abruptly shattered when the entire ship shakes violently. Items fall off shelves, and the ship’s
                    automated systems blare warnings. You rushed to the control panel and saw a message writen in red
                    'WARNING METEOR AHEAD!'
        """)
    print("Marvin : Good morning! Either that was an earthquake, or Mars is trying to evict us.")
    print("""
                    Breathing hard, an idea suddenly pop up in your head. You should move the spaceship to a safer location.
        """)
    print("Do you wish to move the spaceship to a safer location? Moving the ship will drain valuable resources, and you may not have enough to handle other issues later.")
    while True:
        move_spaceship = input("Yes/No : ").lower()
        if move_spaceship == "yes":
            print("""
                    You slam your hand down on the red emergency button, initiating the maneuvering sequence. The ship’s engines 
                    hum to life, but there’s a slight delay, and you hear the soft whine of the systems struggling to power up. 
                    You try again, pressing the button harder, but the engines fail to respond. A warning flashes across the screen: 
                    'Insufficient fuel. Maneuvering systems offline.' You fall on you knees, hoping the meteor is not heading towards you.
                """)
            energy -= 30
            break
        elif move_spaceship == "no":
            print("""
                    You take a deep breath, knowing the ship is already in a fragile state. Moving it would drain valuable resources, 
                    and with fuel and power reserves already low, you decide it’s safer to focus on stabilizing what you already have.
                    You look upwards, hoping the meteor is not heading towards you.
                """)
            score += 50
            break
        else:
            print("Please enter a valid input")
    print(f"----------------------------------------------------\noxygen:{oxygen} | water:{water} | food:{food} | energy:{energy} | score:{score}\n----------------------------------------------------")  
    # Check for depleted resources
    if not check_depleted_resources(username):
        return False  # Exit if game over


#changed to minesweeper
import re

def minesweeper():
    #player_hp = random.randint(120,200)
    #max_hp = player_hp
    global energy

    print("\nMARVIN: 'Scanning area --- Detected 10 spots with high-radioactivity across area of 9x9', starting from 0 of course.'")
    print("MARVIN: 'If I were you I'd avoid those spots. Unless you accidentally fell in, that'd be an 'explosive' surprise!'")
    print("\nFor every spot you choose to dig, if it's safe, numbers will appear to tell you how many bombs there are within an area of 3x3 squares for each number.")
    print("A little hint to help: Corners are usually safe. Note: single digit inputs will be considered as double digit (e.g if you types '0', the game will dig at location '0,0')")
    print("\nYour energy levels are", {energy})
    print("\n")
    #create board
    class Board:
        def __init__(self, dim_size, num_bombs):
            #track parameters
            self.dim_size = dim_size
            self.num_bombs = num_bombs

            #create board
            self.board = self.makeNewBoard()    #helper function; plants the bombs
            self.assignValues() 
            #so it was YOU! (I forgot to add this up here even though I had defined it below. That's why I hit the error-
            # "TypeError: '>' not supported between instances of 'NoneType' and 'int'" ...though I'm not really sure how they're related)
            
            #create set to track locations uncovered; (row, col) tuple
            self.dug = set()    # ex. if dug at 0, 0, self.dug = {(0, 0)}; tutorial jumps around a lot...

        def makeNewBoard(self):
                # construct new board based on dim_size and num of bombs
                # make list of lists? here
                # similar to connect4/radio fix game with 2 set lists to represent 2D board... I think

                #create board
                board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
                #creates array that's like this: [[None, None, ..., None],
                                                # [None, None, ..., None],
                                                #  [...                  ],
                                                #  [None, None, ..., None]]
                
                #plant the bombs
                bombs_planted = 0
                while bombs_planted < self.num_bombs:
                    location = random.randint(0, self.dim_size ** 2 - 1) #returns random integer n, such that a <= n <= b
                    row = location // self.dim_size
                    col = location % self.dim_size

                    if board[row][col] == "*":
                        # apparently betwn while and for loops, for loops still count the space even though we skip it, while while loops don't
                        continue

                    board[row][col] = '*' # plant the bombs
                    bombs_planted += 1

                return board

        def assignValues(self):
                for r in range(self.dim_size):
                    for c in range(self.dim_size):
                        if self.board[r][c] == '*':
                            continue
                        self.board[r][c] = self.getNum(r, c)

        def getNum(self, row, col):
                num_SideBombs = 0
                for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
                    for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                        if r == row and c == col:
                            continue
                        if self.board[r][c] == '*':
                            num_SideBombs +=1

                return num_SideBombs
                    
        def dig(self, row, col):
            #return True if no bomb, False if bombed
            self.dug.add((row, col)) #tuple to keep track of dug areas

            if self.board[row][col] == '*':
                return False
            elif self.board[row][col]>0:
                return True
            
            #self.board[row][col] = 0
            for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
                for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                    if (r, c) in self.dug:
                            continue
                    self.dig(r, c)
            
            # if before we didn't hit a bomb, we wouldn't hit a bomb here...?
            return True

        def __str__(self): #magic function I don't understand that would print the actual boardgame. bagus.
            #create array the represents what player sees
            showBoard = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
            for row in range(self.dim_size):
                for col in range(self.dim_size):
                    if (row,col) in self.dug:
                        showBoard[row][col] = str(self.board[row][col])
                    else:
                        showBoard[row][col] = ' '

            # put this together in a string
            #... excuse me- you had an /entire code/ for the css/boardgame view of this game and you completely skim pass it???
            # no wonder there's no_TypeStr smh
            string_rep = ''
            # get max col widths for printing
            widths = []
            for idx in range(self.dim_size):
                columns = map(lambda x: x[idx], showBoard)
                widths.append(
                        len(
                            max(columns, key = len)
                        )
                )

            #print the csv strings
            indices = [i for i in range(self.dim_size)]
            indices_row = '   '
            cells = []
            for idx, col in enumerate(indices):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            indices_row += '  '.join(cells)
            indices_row += '  \n'

            for i in range(len(showBoard)):
                row = showBoard[i]
                string_rep += f'{i} |'
                cells = []
                for idx, col in enumerate(row):
                        format = '%-' + str(widths[idx]) + "s"
                        cells.append(format % (col))
                string_rep += ' |'.join(cells)
                string_rep += ' |\n'
            
            str_len = int(len(string_rep) / self.dim_size)
            string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

            return string_rep
            

    #play the game? define a play function...?
    def play(dim_size=10, num_bombs=10):
        # Step 1: create board
        global energy
        board = Board(dim_size, num_bombs)

        # Step 2: show user the board and ask where they want to dig
        # Step 3a: if location is bomb, game over
        # Step 3b: if location not bomb, dig continuously until each square is near bomb 
        # Step 4: repeat step 2 and 3a/b until there are no more places to dig -> Victory
        safe = True

        while len(board.dug) < board.dim_size ** 2 - num_bombs:
            print(board)
            user_input = input("Where would you like to dig? Input as row,col: ")  # '0,3'

            try:
                user_input = re.split(r',\s*', user_input)  # Split input by comma and optional spaces
                row, col = int(user_input[0]), int(user_input[-1])

                if row < 0 or row >= board.dim_size or col < 0 or col >= dim_size:
                    print("MARVIN: 'Where in the WORLD are you going?' \nInvalid location. Try again.")
                    continue

            except (ValueError, IndexError):
                print("MARVIN: '... why do I even try.' \nInvalid input. Please enter numbers in the format row,col (e.g., 0,3).")
                continue  # Skip to the next loop iteration


            # If input is valid, proceed with digging
            safe = board.dig(row, col)
            if not safe:
                break  # Game over

            
        if safe:
            print("Congrats! We live!") 
        else:
            print("MARVIN: 'Well now look what you've done.' \nGame Over.")
            energy -= 10
            board.dug = [(r, c) for r in range(board.dim_size) for c in range(board.dim_size)]
            print(board)

    if __name__ == '__main__': #don't really understand this function
        play()
#===================================
def event_day_3():
    global energy, food, oxygen, water, score 
    print("BOOOOOOOOORRMMMMMMHHGG!!! An asteroid hit Mars.")
    while True:
        choice = input("Explore (E) or Stay (S)? ").strip().lower()
        if choice == 'e':
            minesweeper()
            print("MARVIN: Look at you, being all responsible. I’m almost impressed.")
            break
        elif choice != 'e' and choice != 's':
            print ("MARVIN : 'What was that? Try again'")
            continue
        else:
            print("-10 everything. MARVIN: 'Procrastination: the cornerstone of all great disasters.'")
            energy -= 10
            food -= 10  
            oxygen -= 10
            water -= 10
            break
    print(f"----------------------------------------------------\noxygen:{oxygen} | water:{water} | food:{food} | energy:{energy} | score:{score}\n----------------------------------------------------")
    # Check for depleted resources
    if not check_depleted_resources(username):
        return False  # Exit if game over


#---------------------------------------END OF DAY 3----------------------------------------------------------------------------

#----------------------------------------------DAY 4----------------------------------------------------------------------------
def intro_sequence_day4():
    # Check for depleted resources
    if not check_depleted_resources(username):
        return False  # Exit if game over
    print("======================================\nDAY 4: The Martian Blues\n======================================")

def event_day_4():
    global energy, food, oxygen, water, score
    print("\n📢 ALERT! Your Martian base AI is screaming:")
    print("🚨 “WARNING! SOLAR FLARE INCOMING! TAKE COVER!” 🚨")
    print("\nYou glance outside your tiny space window... the Sun looks extra spicy today. 🌞")
    print("What do you do?")
    while True:
        choice = input("Stay Indoors (S) or Go Out (G)? ").strip().lower()
        if choice == 's':
            print("Smart move. Wouldn’t want to have burnt to a crisp.")
            print("Can’t say the same for your ship though. You gain 20 energy.")
            energy += 20
            break
        elif choice != 's' and choice != 'g':
            print("MARVIN: 'What was that? Try again.'")
            continue
        else:
            print("You got fried by radiation. THE END.")
            exit()
            break
    print(f"----------------------------------------------------\noxygen:{oxygen} | water:{water} | food:{food} | energy:{energy} | score:{score}\n----------------------------------------------------")

def time_coded4():
    global food
    global energy
#Time coded Day 4
    print("""
                    'Grrr' your stomach suddenly grumbles, breaking the tense silence. It has been hours since you last ate, 
                    and the stress of everything happening around you is starting to take its toll. You walk towards the cabinet and open it.
                    However, there is only minimal amount of food left. Holding your hungry tummy, you glance over the door of the
                    spaceship, wodering if you should go out to the plantation place to harvest some food.
        """)
    print("Marvin : Fun fact, humans cannot survive without food. But hey, who needs facts when you have got bad decisions?")
    print("Do you head to the plantation to gather something to eat, or do you try to ration your food supply")
    while True:
        go_plantation = input("Yes/No : ").lower()
        if go_plantation == "yes":
            print("Marvin : Bold move. Let us hope the Martian wildlife is not hungry too.")
            print("""
                    You decided to head to the plantation as the hunger is too much to ignore. You head outside, trying to remember the 
                    path to the plantation place. It does not take long before you arrive. Strangely, the plant grow up well despite being
                    plant on Mars. Without wasting time, you began harvesting.
                """)
            food += 30
            energy -= 20
            break
        elif go_plantation == "no":
            print("""
                    You decide not to go out to the plantation and instead ration out the food left in the cabinet. You carefully portion out
                    what little you have. Each bite feels heavier than the last, the hunger gnawing at you, but at least you know you arre not
                    risking unnecessary exposure to whatever might be happening outside.
                """)
            print("Marvin : Yes, let us eat less and hope your stomach does not riot.")
            food += 10
            break
        else:
            print("Please enter a valid input")
    print(f"----------------------------------------------------\noxygen:{oxygen} | water:{water} | food:{food} | energy:{energy} | score:{score}\n----------------------------------------------------")  
    # Check for depleted resources
    if not check_depleted_resources(username):
        return False  # Exit if game over


#---------------------------------------END OF DAY 4----------------------------------------------------------------------------

#----------------------------------------------DAY 5----------------------------------------------------------------------------
def intro_sequence_day5():
    # Check for depleted resources
    if not check_depleted_resources(username):
        return False  # Exit if game over
    global score
    global food
    global energy
    print("======================================\nDAY 5: Rescue (or Not)\n======================================")
        #Time coded Day 5
    print("""
                    While exploring the depths of the spaceship, you find yourself wandering through hallways you haven’t ventured into before.
                    The ship has been your home for what feels like forever, and the routine is starting to get to you. You know the layout,
                    but today, you stumble upon a door you've never seen before. Slowly walking towards the room, you hold the handle. 
        """)
    print("Marvin : Good news! The rescue team is almost here. Bad news! Everything is falling apart- Hey what are you doing")
    print("Do you want to open the door to see what is inside?")
    while True:
        open_door = input("Yes/No : ").lower()
        if open_door == "yes":
            print("""
                    You chose to open the door. Slowly twisting the doorknob, you push the door slightly. As you peer inside, you’re shocked
                    by what you see: a pile of food stacked neatly on the shelves, more than you’ve ever seen on this ship before. How could 
                    you not have found this room sooner? The thought of all the times you’ve been starving, rationing every last bit,
                    only to discover this abundance of food now, feels like a cruel joke. You take a few items and feel a rush of relief.
                """)
            score += 30
            food += 50
            energy -= 20
            break
        elif open_door == "no":
            print("""
                    You decide not to take any chances and walk away from the room. But as you move down the hallway, you can’t 
                    help but wonder what’s behind that door. The curiosity lingers, and you start to question if you made the right decision.
                """)
            energy -= 10 
            break
        else:
            print("Please enter a valid input")
                
        print(f"----------------------------------------------------\noxygen:{oxygen} | water:{water} | food:{food} | energy:{energy} | score:{score}\n----------------------------------------------------")  
        # Check for depleted resources
        if not check_depleted_resources(username):
            return False  # Exit if game over

        print("""
                            This is it. The final ENDGAME. The culmination of your struggle against the unforgiving red planet. 
                            All your hopes, all your fears, all your decisions have led you to this moment. 
                            What desperate gamble will you make in this, your final stand against the indifferent expanse of Mars?
                """) #Narration part (not randomized)

#Connect Four utilized into fix radio game

#Import random to act as radio 'breaking down'
def fix_radio():
    print("MARVIN: Thi-Thi-This radio doesn't seem to wa-a-a-nt to- live any-any lon-n-n-g-ger.")
    print("O-o-o-oh, and me too. Good luck.")
    print("\nConnect blue dots (🔵) from one end to the other before the radio fills itself with red (🔴).")
    print("\nYou can start from anywhere.")
    print("------------------------------------------")



    #Columns, as represented by letters; rather than 7x6 connect4 boardgame, I'll try 6x6
    possibleLetters = ["A", "B", "C", "D", "E", "F"]

    #Making an array now, meaning we're looping through columns and rows; making the 'spaces' of our gameboard now    
    gameBoard = [["", "", "", "", "", ""], ["", "", "", "", "", ""], ["", "", "", "", "", ""], ["", "", "", "", "", ""], ["", "", "", "", "", ""], ["", "", "", "", "", ""]]
    rows = 6
    columns = 6

    #The board part
    def createGameBoard():
        print("\n     A    B    C    D    E    F", end = " ")
        for x in range(rows):   #Now to loop through the arrays; rows here is from up the 'rows = 6'
            print("\n   +----+----+----+----+----+----+")
            print(x, " |", end="")
            for y in range(columns):        #loop through by row and simultaniously check for chips (so the board refreshes everytime?)
                if gameBoard [x][y] == "🔵":
                    print("", gameBoard [x][y], end=" |")
                elif gameBoard [x][y] == "🔴":
                    print("", gameBoard [x][y], end=" |")
                else:
                    print(" ", gameBoard [x][y], end="  |")
        print("\n   +----+----+----+----+----+----+")

    def modifyArray(spacePicked, turn):  #tutorial called this a helper variable, will learn more in next part
        gameBoard[spacePicked[0]][spacePicked[1]] = turn

    def coordinateTranslate(inputString): #also known as check for winner
        if len(inputString) < 2:  # Check if input has at least two characters
            print("Invalid input. Please enter a valid coordinate.")
            return None

        letter = inputString[0].upper()  # Ensure case insensitivity
        number = inputString[1:]

        if letter not in possibleLetters:  # Validate column letter
            print("Invalid column letter.")
            return None

        if not number.isdigit():  # Ensure the second part is a digit
            print("Invalid row number.")
            return None

        row = int(number)

        if row < 0 or row >= rows:  # Ensure row is within valid range
            print("Row number out of range.")
            return None

        return [row, possibleLetters.index(letter)]


    def isSpaceAvailable(intendedCoordinate):
        if(gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == '🔴'):
            return False
        elif(gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == '🔵'):
            return False
        else:
            return True
        
    def blueWins():
        visited = set()  # Keep track of checked cells

        def dfs(row, col, visited):  #pathfinding function
            if (row, col) in visited:  # Prevent revisiting
                return False
            if gameBoard[row][col] != '🔵':  # Only travel through 🔵
                return False

            visited.add((row, col))  # Mark as visited

            # Possible directions (left-right-up-down)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            for dr, dc in directions:
                newRow, newCol = row + dr, col + dc
                if 0 <= newRow < rows and 0 <= newCol < columns:
                    dfs(newRow, newCol, visited)  # continues exploring

            # **NEW FIX**: Ensure at least **one** 🔵 in column A before checking paths
            blue_starts = [(r, 0) for r in range(rows) if gameBoard[r][0] == '🔵']

            # **Fix:** Only trigger game over if NO valid paths exist at all
            if not blue_starts:
                return False  # No blue pieces placed yet, so the game isn't blocked


        # Start DFS from any row in the first column (A)
        for startRow in range(rows):
            if gameBoard[startRow][0] == '🔵':
                dfs(startRow, 0, visited)
        
        #Check if any 🔵 in column F is part of the path
        for endRow in range(rows):
            if (endRow, columns - 1) in visited:  # (row, last column)
                return True  # 🔵 wins

        return False

    def gameBlocked():
        # If there are no 🔵 pieces on the board, the game just started
        if not any('🔵' in row for row in gameBoard):
            return False  # Don't falsely trigger at the start
        
        visited = set()  # Track visited cells

        def dfs(row, col):  # Depth-first search for 🔵 pathfinding
            #print(f"Visiting ({row}, {col})")  # Debug output
            if col == columns - 1:  # If we reach column F, it's not blocked
                return True
            if (row, col) in visited or gameBoard[row][col] != '🔵':  # Avoid revisiting and non-🔵 cells
                return False

            visited.add((row, col))

            # Check all 4 directions (up, down, left, right)
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in directions:
                newRow, newCol = row + dr, col + dc
                if 0 <= newRow < rows and 0 <= newCol < columns:
                    if dfs(newRow, newCol):  # Keep exploring
                        return True

            return False  # No path found

        # Check if any 🔵 in column A can reach column F
        for startRow in range(rows):
            if gameBoard[startRow][0] == ' ' or gameBoard[startRow][0] == '🔵':  # Consider empty or blue spaces
                if dfs(startRow, 0):
                    return False  # 🔵 can still win, so not blocked

        return True  # No path for 🔵 → The game is truly blocked

    #if gameBlocked():
        #print("No valid path for 🔵 to reach column F. Game is blocked!")
    def checkBoardFull():
        # Check if the board is full (no empty spaces left)
        for row in gameBoard:
            if '' in row:
                return False
        return True  # No empty spaces left

    def CheckWinner(chip):
        if chip == '🔵':
            if blueWins():  # Check if Blue wins
                return True
        #if gameBlocked():
                #if chip == '🔴':
                    #return True

        return False

    def checkForRedWin():
        # Similar to blueWins(), define this function to check for red's victory
        visited = set()

        def dfs(row, col):
            if col == columns - 1:
                return True
            if (row, col) in visited:
                return False
            if gameBoard[row][col] != '🔴':
                return False

            visited.add((row, col))

            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dr, dc in directions:
                newRow, newCol = row + dr, col + dc
                if 0 <= newRow < rows and 0 <= newCol < columns:
                    if dfs(newRow, newCol):
                        return True

            return False

        for startRow in range(rows):
            if gameBoard[startRow][0] == '🔴' and dfs(startRow, 0):
                return True

        return False

    def redAI():
        #Make two random moves (across two different columns)
        print("*radio crashing noises*")
        moves = []
        for _ in range(2):  # Loop twice to place two chips
            while True:
                cpuChoice = random.choice(possibleLetters) + str(random.randint(0, 5))
                cpuCoordinate = coordinateTranslate(cpuChoice)
                if cpuCoordinate and isSpaceAvailable(cpuCoordinate):
                    moves.append(cpuCoordinate)
                    break
        return moves


    turnCounter = 0

    while True:
        if turnCounter % 2 == 0:
            createGameBoard()

            while True:
                spacePicked = input("\nChoose a space (col,row): ")
                coordinate = coordinateTranslate(spacePicked)

                if coordinate is None:
                    continue #skip to next loop iteration

                try:
                    #Check if space available
                    if(isSpaceAvailable(coordinate)):
                        modifyArray(coordinate, '🔵')
                        break
                    else:
                        print("Not a valid coordinate.")
                except:
                    print("Error occured. Please try again.")

            winner = CheckWinner('🔵')  # 🔵 now needs to connect left to right
            if winner:
                createGameBoard()
                print("Blue wins!")
                print("MARVIN:'We're saved!'")
                break  # End the game if Blue wins

            if gameBlocked() and checkBoardFull():
                createGameBoard()
                print("The board is full, and no valid path exists for blue.")
                break  # End the game if the board is full and no path exists for blue

            turnCounter += 1
        else:
            redMoves = redAI()  # Red AI's turn (returns a list of two moves)
            for move in redMoves:
                modifyArray(move, '🔴')  # Apply both red moves

            winner = checkForRedWin() # Check if red wins after both moves
            if winner:
                    createGameBoard()
                    print("The radio screen freezes and the lights flicker")
                    print("\nMARVIN:'Well-well-well-well, it's-s-s-s been a good run, cap-cap-taaaaaain-' System: 'MARVIN' is down.")
                    break  # End the game if Red wins
            
            if gameBlocked() and checkBoardFull():
                createGameBoard()
                print("The board is full, and no valid path exists for red.")
                break  # End the game if the board is full and no path exists for red

            turnCounter += 1


def event_day_5():
    global energy, food, oxygen, water, score
    print("A weird noise is coming from somewhere.")
    while True:
        choice = input("Check it out (C) or Wait (W)? ").strip().lower()
        if choice == 'c':
            fix_radio()
            print("You won the mini-game! You are rescued after being on strings of hope on calling the earth!")
            break
        elif choice !='w' and choice != 'c':
                print("What was that? Try again.")
                continue
        else:
            print("Well... I guess this is it. You were... an adequate companion. Goodbye...")
            print("MARVIN...is DEAD. You are alone now""")
            print(""" And for the first time, the universe feels truly empty...
            """)
            break
    print(f"----------------------------------------------------\noxygen:{oxygen} | water:{water} | food:{food} | energy:{energy} | score:{score}\n----------------------------------------------------")
    # Check for depleted resources
    if not check_depleted_resources(username):
        return False  # Exit if game over

#---------------------------------------END OF DAY 5----------------------------------------------------------------------------

#Run the main function
main()   
