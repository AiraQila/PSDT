oxygen = 100
energy = 0
water_packet = 0
energy_packet = 0
water = 0
food = 100
XP = 0
inventory_item = ["water_packet", "energy_packet"]

#Day 1- Afternoon
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
        inventory_item.append("shiny_rock")
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
print("total energy : ", energy, "total oxygen : ", oxygen, "total water : ", water, "total food : ", food, "energy packet : ", energy_packet, "water packet : ", water_packet)



#Day 2 - night
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
        XP += 50
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
print("total energy : ", energy, "total oxygen : ", oxygen, "total water : ", water, "total food : ", food, "energy packet : ", energy_packet, "water packet : ", water_packet)

#Day3-morning
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
    fix_heater = input("Yes/No : ").lower()
    if fix_heater == "yes":
        print("""
      You slam your hand down on the red emergency button, initiating the maneuvering sequence. The ship’s engines 
      hum to life, but there’s a slight delay, and you hear the soft whine of the systems struggling to power up. 
      You try again, pressing the button harder, but the engines fail to respond. A warning flashes across the screen: 
      'Insufficient fuel. Maneuvering systems offline.' You fall on you knees, hoping the meteor is not heading towards you.
              """)
        energy -= 30
        break
    elif fix_heater == "no":
        print("""
      You take a deep breath, knowing the ship is already in a fragile state. Moving it would drain valuable resources, 
      and with fuel and power reserves already low, you decide it’s safer to focus on stabilizing what you already have.
      You look upwards, hoping the meteor is not heading towards you.
              """)
        XP += 50
        break
    else:
        print("Please enter a valid input")
print("total energy : ", energy, "total oxygen : ", oxygen, "total water : ", water, "total food : ", food, "energy packet : ", energy_packet, "water packet : ", water_packet)



#Day 4
print("""
      'Grrr' your stomach suddenly grumbles, breaking the tense silence. It has been hours since you last ate, 
      and the stress of everything happening around you is starting to take its toll. You walk towards the cabinet and open it.
      However, there is only minimal amount of food left. Holding your hungry tummy, you glance over the door of the
      spaceship, wodering if you should go out to the plantation place to harvest some food.
      """)
print("Marvin : Fun fact, humans cannot survive without food. But hey, who needs facts when you have got bad decisions?")
print("Do you head to the plantation to gather something to eat, or do you try to ration your food supply")
while True:
    take_a_look = input("Yes/No : ").lower()
    if take_a_look == "yes":
        print("Marvin : Bold move. Let us hope the Martian wildlife is not hungry too.")
        print("""
      You decided to head to the plantation as the hunger is too much to ignore. You head outside, trying to remember the 
      path to the plantation place. It does not take long before you arrive. Strangely, the plant grow up well despite being
      plant on Mars. Without wasting time, you began harvesting.
            """)
        food += 30
        energy -= 20
        break
    elif take_a_look == "no":
        print("""
      You decide not to go out to the plantation and instead ration out the food left in the cabinet. You carefully portion out
      what little you have. Each bite feels heavier than the last, the hunger gnawing at you, but at least you know you arre not
      risking unnecessary exposure to whatever might be happening outside.
              """)
        print("Marvin : Yes, let us eat less and hope your stomach does not riot.")
        break
    else:
        print("Please enter a valid input")
print("total energy : ", energy, "total oxygen : ", oxygen, "total water : ", water, "total food : ", food, "energy packet : ", energy_packet, "water packet : ", water_packet)


#Day 5
print("""
      While exploring the depths of the spaceship, you find yourself wandering through hallways you haven’t ventured into before.
      The ship has been your home for what feels like forever, and the routine is starting to get to you. You know the layout,
      but today, you stumble upon a door you've never seen before. Slowly walking towards the room, you hold the handle. 
      """)
print("Marvin : Good news! The rescue team is almost here. Bad news! Everything is falling apart- Hey what are you doing")
print("Do you want to open the door to see what is inside?")
while True:
    fix_heater = input("Yes/No : ").lower()
    if fix_heater == "yes":
        print("""
      You chose to open the door. Slowly twisting the doorknob, you push the door slightly. As you peer inside, you’re shocked
      by what you see: a pile of food stacked neatly on the shelves, more than you’ve ever seen on this ship before. How could 
      you not have found this room sooner? The thought of all the times you’ve been starving, rationing every last bit,
      only to discover this abundance of food now, feels like a cruel joke. You take a few items and feel a rush of relief.
              """)
        XP += 30
        food += 50
        energy -= 20
        break
    elif fix_heater == "no":
        print("""
      You decide not to take any chances and walk away from the room. But as you move down the hallway, you can’t 
      help but wonder what’s behind that door. The curiosity lingers, and you start to question if you made the right decision.
              """)
        energy -= 10 
        break
    else:
        print("Please enter a valid input")
print("total energy : ", energy, "total oxygen : ", oxygen, "total water : ", water, "total food : ", food, "energy packet : ", energy_packet, "water packet : ", water_packet)







# d2- if they choose not to fix the heater, find out how to minus 10 for every other night
#Double check if the inventory is supposed to be printed like that






oxygen = 100
energy = 0
water_packet = 0
energy_packet = 0
water = 0
food = 100
XP = 0 #nanti add xp for game yang menang
inventory_item = ["water_packet", "energy_packet"]


#introduction everytime the player choose to fix the spaceship
Instruction = """
You are required to fix the spaceship. 
There are 5 things to repair and you can only choose one per day. 
Where do you wish to go?
\nChoose your action : 
a. power supply room
b. oxygen tank
c. main room
d. spaceship body
e. toilet
"""

#asking the player where do they wish to fix. Each place have different problems and the player need to fix them.
def InsideSpaceShip():
    directions = ["a", "b", "c", "d", "e"]
    print(Instruction)
    while True:
        InputDirection = input("Enter your choice : ").lower()
        if InputDirection == "a":
            PowerSupplyRoom()
            break
        elif InputDirection == "b":
            OxygenTank()
            break
        elif InputDirection == "c":
            MainRoom()
            break
        elif InputDirection == "d":
            SpaceshipBody()
            break
        elif InputDirection == "e":
            Toilet()
            break
        else:
            print("Please enter correct directions")
            
        
#if player choose to fix the power supply room           
def PowerSupplyRoom():
    global energy
    global water_packet
    import time

    print("You went into the power supply room. Suddenly, the light started flickering.")
    print("Marvin : Dude did you forget to pay the electric bill? How am I supposed to charge myself you human")
    time.sleep(2)
    # Code for the game
    def math_puzzle(sequence, correct_answer):
        attempts = 3  # maximum incorrect answer
        
        while attempts > 0:
            try:
                answer = int(input(f"Solve the sequence: {sequence} (What’s the next number?): "))
            except ValueError:
                print("Enter a valid integer!")
                continue

            # --- Check the player's answer ---
            if answer == correct_answer:
                print("Correct!")
                return True
            else:
                attempts -= 1
                print(f"Incorrect. You have {attempts} attempts left.")

        print("You lose!")
        time.sleep(4)
        print("Suddenly, the lights are back on")
        print("Marvin : Dang, you played for nothing")
        return False

    def main():
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
        
        # --- Success ---
        print("\nYou solved all the puzzles! The lights are fully restored.")

    main()


    energy -= 20
    water_packet += 2
    print("total energy : ", energy, "total oxygen : ", oxygen, "total water : ", water, "total food ;", food, "energy packet : ", energy_packet, "water packet : ", water_packet)
    


#if player choose to fix the oxygen tank
def OxygenTank():
    global oxygen
    global energy
    print("You enter the room with the oxygen tank and notice it's old and rusted. As you approach it, the machine suddenly starts to smoke.")
    print("""

 ---------------------------------------------------::@.  :--:       :*    -------------------------------------------- 
 ----------------------------------------------------: -@:     @@@ @@. :@@ -------------:     :------------------------ 
 --------------------------:::::::--------------------:  :@  @@ @@ @@ .    -------------  @@@  ------------------------ 
 --::---------------------:     :   :-------------:.      @@@@@.      :---------------:  @=:@@ -------------------:---- 
 -----------------------:   @@% @@@  ------------:  =@@@%-@@@%:::@@@%    :-----------:  @@@@@  ------------------------ 
 ---:-------------------: @@ @  @  @ ----------:   @-   .@@@@@@@@   =@@@       :::::.  @      :--------------------:--- 
 ------------------------  @%     @@ ----------  @@:@@@@-.     .%@@@: %@@@@@@@        @   :---------------------------- 
 ------------------------:   @% @#   ---------- %@@:     ....     *@@* @.   @@@@@=@@=@@@@    :------------------------- 
 --------------------------: @  @   :---------: @: .+@@@@@@@@@@@@%.  ..@ :.@   +  @  @ @::@@   :----------------------- 
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
 ----------------   =@@@ :----         .- @@=@@@ @@@:-: ....:::  @@@:== @ .+@ ...  .. .@@@%@@% =@   :------------------ 
 ---------------- @@#@@@=:---- @@ @@@ # - @@@@@@   .:===++=++=+*=:..:== @ ..@ ..:=====:.  @  @@@  :-------------------- 
 ----------------  @@@*  :---  @  -  @@        @-.-==================== @: *@@@@+-:.      -@@         :---------------- 
 ----------------:      ::--- @@ @@@  @@       @@#-:..:==============-. @#:@*    .%@@@@@@@#    @@  @@  :--------------- 
 ----------------------------  :@ +@ @  =@@@@@    %@@@@+-:.     ..::=+@@@@*    @@@@@        . @ @@@ @@ :--------------- 
 -----------------------------:  = .   @=:@@@@@@        +@@@@@@@@@@%=       :- #@@@  ...:---.:@ @@@@@@ :--------------- 
 ----------------:.:.::::------:    @@@@@:    %@@    @@@@         @@*@@  .:.             :--:  @@@@@@  :--------------- 
 ----------------: . .   :---:   @@@::. .:@@@:  @= @@@@@@@ -:  @@@=:@-@@ -- @= @@@@:@*@@     .        :---------------- 
 ---------------- .@:=%@ .--:  @@:..:====-::...@@   @:*@*  :  @@@@. +@   :- :@@@@%@@@@@@@@@@-:------------------------- 
 ---------------- @@*@@@ .--: @*  :---:.. ..:@@    %@@    :  @     @#  :---:                 :------------------------- 
 ----------------  *==.  :--: =@@@@%%%@@@@@%%%@@@@+@@ *@  - @@ @@@@@               :----------------------------------- 
 ----------------:.    ::----.          %@@%:.. @:  @@ @@ -  @@    :@@@*  :@@=@@@@  :---------------------------------- 
 :::::::-:-------------------.   @@@@@@*:.@. == -@  %@@@@ -:  @@:+@-  =@@@@ :@.  -@ .:::::::-----------------------:--- 
 :-::-:-::------------------- *@-:. #@ :-..@  ::@@@@%           *@@+=@@ @= @@..=:.@ .::-:--:--------------------------- 
 ----------------------------  @@-.: @:   =@@@@@        @@@@  -.      .@* @@ :==.:@ .---------------------------------- 
 ----------------------------: @ @.::@@@@@=      :: @@@@@-  @ ----::.  @ =@ :=-. @@ :---------------------------------- 
 -----------------------------  *@@@@*     .:-----: @@@-@@@@= ------- @@ @*.=:.-@@  ----------------------------------- 
 -----------------------------:        ::---------:          :------- @@ @...:@@   ------------------------------------ 
 -----------------:-------------------------------------------------- =@-@:@@@   :-------------------:----------------- 
  
          """)
    print("Quick! To fix the oxygen tank, you need to guess the correct number starting from 0 to 50")
    print("Marvin : Oh, sure, no pressure. Just win if you really want to stay alive.")
    
    import datetime
    import random

  #code for the game
    timer = datetime.datetime.now() + datetime.timedelta(seconds=30) #setting the timer in 15 minutes
    target = random.randrange(51) #generating a number between 0 to 50

    print("\nOh I forgot to mention that you only have 30 seconds")
    while True:
        try:
            guess = int(input("Enter a number between 1 to 50: "))
        except ValueError:
            print("Enter an interger!")
            continue
        remaining = (timer - datetime.datetime.now()).total_seconds()
        if remaining < 0:
            print("Too late!  You lost!")
            energy -= 20
            print("total energy : ", energy, "total oxygen : ", oxygen, "total water : ", water, "total food : ", food, "energy packet : ", energy_packet, "water packet : ", water_packet)
            break
        if guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")
        else:
            print("You got it!")
            oxygen += 100
            print("total energy : ", energy, "total oxygen : ", oxygen, "total water : ", water, "total food : ", food, "energy packet : ", energy_packet, "water packet : ", water_packet)
            break
        print(f"{remaining:.0f} seconds left before you lose!")
      
     

#check how to print the inventory item



#if player choose to go to the main room
def MainRoom():
    global energy
    global water_packet
    global food

    print("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@%%%%@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@%%%%@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%@@@%@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@%%@@%@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@%@@@%%@@@@@@@@@@@@@@
@@@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%@@@@@@@@@@@@@
@@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@%@@@@@@@@@@@@@
@@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@%@@@@@@@@@@@@
@@@@@@@@@@@@%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@%@@@@@@@@@@@@
@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@%%@@@@@@@@@@@@
@@@@@@@@@@@%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%@@@@@@@@@@@
@@@@@@@@%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%@@@@@@@@
@@@@@@%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@%@%%@%@%@%@%@%@%@%@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%@@@@@@@@
@@@@@@%@%%%%%@%@@%@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@%@@%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@%@%@%@@%%%%@%@%@%%%%%
@@@@@@%@%%%@%@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@%%@%%@%@@@%@%@%
@@@@@@%@%%@@%@@@@@@@@@@@%%%@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@%@%%@%@@@@@@@@
%%%%%@%@@%@@@@@@@@@@@%%%%%%@@@@%%@%%%%%%%%@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@%%%%%%%@%%%%%%%%%%@@@@@@@@@@@%@@%%@@@@@@@
@@%%%@%%%%%%@@@@@@%%%%%%%%%@@@%%%%%%%%%%%@%@@%%%%%%@@%%%%%%%%%%%@%%@@@%%%%%%@%%%%%%%%@%%%%%%%%%%%@@@@%%%%%@@@@@%%@@@@@@@
@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@%%%%%%%%%@@%%%%%%@@@@%%%%%@%%%%%%@%@@@%%%%%@@%@%%%%%%%@%%%%%%%%%@%@@@@%%%%%@@@@@%%@@@@@
@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@%%%%%%%@@%%%%%%%%%%@%%%@@@@@%%%%%%%@%%%%%%%%%%%%%%%%%%%%@@@@@@@@@%%%%%%%%@@@@
@@%%@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%@%%%%@@@@%@%@@@@@@@@@@%%%%%%%%@%%%
%%%%%%%%%%%%%%%%%%%%%%@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@%%%%%%%%@%%%%
%%%%%%%%%%%%%@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@%%%%%%%%%%%%%%@@@%%%@%%%%
%%%%%%@@@@%%%%%%%%%%%%%%%@%%%%%%%%%%%%%%%%%%%%@%%%@%%%@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%@@@@@@@@@@%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@%%%%%%%%%
%%%%%%%%%%%@@@@@@%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%@%%%%@@@@@%
%%%%@@@@@@%%%%%%%%@@@@@%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@%%%%%%%%%%%%%%%%%%
%%@@@%%%%%%%@@@@@@%%%%%%%%%%@%%@%%@%@%%@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@%@@%@%@%@%%%%%@@%@@@@@@@@%%%%%%%%%%%%
%@@@@%@%@%@@%%%%%%%%%%%%%%%%%@@%@@%@%@@%@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@%%@%%@%@%@%%%%%%%%%@%@%%@%@@@%@@%@%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@%%%%%@%%%%%%%@%%%%%%@%%%@@%@%%@%%%@%%%@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    """)
    energy -= 20
    water_packet -= 1
    print("You are now in the main room. You are allowed to call someone and ask for their help.")
    print("Marvin : So who are you calling? Are you ?")
    print("""
    Welcome! In this game, you are required to guess the correct answer to all the questions.
    """)
  #code gor quiz
    questions = ("How many planets are there in our solar system: ",
                          "Which planets in our solar system are NOT made of rock?: ",
                          "Mars is 2 times ____ than the Earth?: ",
                          "How many moon(s) does Mars have?: ",
                          "Which planet in the solar system is the hottest?: ")

    options = (("A. 5", "B. 10", "C. 8", "D. 14"),
                      ("A. Mercury", "B. Mars", "C. Earth", "D. Jupiter"),
                      ("A. smaller", "B. bigger", "C. Taller"),
                      ("A. 2", "B. 5", "C. 1", "D. 15"),
                      ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

    answers = ("C", "D", "A", "A", "B")
    guesses = []
    score = 0
    question_num = 0

    for question in questions:
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter (A, B, C, D): ").upper()
        guesses.append(guess)
        if guess == answers[question_num]:
            score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{answers[question_num]} is the correct answer")
        question_num += 1


    print("       RESULTS        ")
    print("answers: ", end="")
    for answer in answers:
        print(answer, end=" ")
    print()

    print("guesses: ", end="")
    for guess in guesses:
        print(guess, end=" ")
    print()

    score = int(score / len(questions) * 100)
    print(f"\nYour score is: {score}%\n")

    if score >= 60:
        message = input("Enter your message here : ")
        energy -= 10
        water_packet += 1
    else:
        print ("Your score didn't reach 60%")
        energy -= 20
        food -= 5
    print("total energy : ", energy, "total water packet : ", water_packet, "total water : ", water, "total food : ", food, "energy packet : ", energy_packet, "water packet : ", water_packet)



def SpaceshipBody():
    import time 

    print("""
  You’re casually gazing outside the spaceship, when, out of nowhere, you spot it.
  A massive meteor, speeding toward you from the vast galaxy. 
  Your heart stops. You freeze in terror.
  In a panic, you scramble under the table, waiting for the inevitable collision.
    """)
    print("One...")
    time.sleep(2)
    print("Two...")
    time.sleep(2)
    print("Three...")
    time.sleep(3)
    print("""
  You can’t take it anymore. You rise, cautiously walking towards the window.
  You peek outside, holding your breath.
  BOOM!
  The spaceship shudders violently, and before you can even brace yourself, you’re sent sprawling to the floor.
    """)
    print("Marvin : OMG, WHAT WAS THAT?! I swear I nearly had a heart attack! I’m WAY too young to be facing my dramatic demise like this!")

    print("""
                                                                                                                                                                                                                                  
                                                                                                                        
             %:                                                                                                         
               =%*-===:-::.                                                                                             
                  @#*%-##=*=-=**#%%+=                                                                                   
                   =%%@#:= =:=+ :+**@@+++.                                                                              
                     @=:%.*#=-  :#@-:::+#=*%@%                                                                          
                      -@%+:-@@@@%%::::::=%#%@*#%%-                                                                      
                        *%%%-===***=:::#@*@**=+@@@@%%=.                                :-                               
                          *@@*+@===-:=@@-+@@%@@@+-=*@@@%%#*#                      .%*.:  .*+=+:                         
                            =%*@=-:=-=%-.%@@@@@@@@*%*%@%%@@%=@@=                    %+=       .@##:=.      %+           
                               #%%%+-=@:=@*::##+%@%%%*+@@*%@%#@@#=*+                .:--       **%#   :@=#= .=          
                                  #**@@:*=    =:#@@%#@@@%#%##*%@@*+*+=*=             :%@%+:      =%  :+:-%+             
                                     *@*-::.   :%#.. - =@@@@@@@@@*:      :=-=-=*#%*- :====*%@%=.  =  *:%%@              
                                        =%#=--. =    -   := ..:. :==-     :  :**:             +%:*#+%**#@=              
                                           .#%#--:  *===       .::.     :        :**          *                         
                                               +%@*+%:  **             =       .     :#:     #:                         
                                                   *@@*=: ..:%#.      +        .*%#+-.   :=  *                          
                                                      .*@#=.:::=:*  .:          :@%*:       ::+=-:                      
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

    def OrderPuzzle():
      global energy
      global water_packet
      global food
    # The correct order of words to form a sentence
      correctAnswer = ['I', 'am', 'playing', 'lost', 'in', 'Mars']
      print("Rearrange the words to repair the spaceship!")
      print("You have the following words (in random order):")
      print("playing, in, am, Mars, I, lost")
      
      # Ask the player to input the words in the correct order
      player_guess = input("Enter the words in the correct order (separate by spaces): ").split()
      
      # Check if the player's input matches the correct order
      if player_guess == correctAnswer:
          print("Correct! The spaceship is repaired!")
          energy -= 10
          water_packet += 1
          food += 10

      else:
          print(f"Incorrect! The correct order was: {' '.join(correctAnswer)}.")
          energy -= 20
          food -= 10
    OrderPuzzle()

    print("total energy : ", energy, "total oxygen : ", oxygen, "total water : ", water, "total food : ", food, "energy packet : ", energy_packet, "water packet : ", water_packet)


def Toilet():
    global energy

    print("""                                                                                                                                                                                                                                          
                                                                                                                        
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

    energy -=50
    food -= 10
    water -= 10
    print("Marvin : What are you even doing here? Stop wasting my precious time and go do something beneficial")
    print("total energy : ", energy, "total oxygen : ", oxygen, "total water : ", water, "total food : ", food, "energy packet : ", energy_packet, "water packet : ", water_packet)


InsideSpaceShip()
