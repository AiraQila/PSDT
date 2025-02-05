#Initialise value of resources and inventory items
oxygen = 100
energy = 100
water_packet = 0
energy_packet = 0
water = 0
food = 100
XP = 0 
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
        InputDirection = input("Enter your choice :").lower()
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
            print("Please enter correct directions")
            
        
#if player choose to fix the power supply room           
def PowerSupplyRoom():
    global energy
    global water_packet
    import time

    print("You went into the power supply room. Suddenly, the light started flickering.")
    print("Marvin : Dude did you forget to pay the electric bill? How am I supposed to charge myself you human")
    #add delay in the execution of a program.
    time.sleep(2)
    # Code for the game
    def math_puzzle(sequence, correct_answer):
        attempts = 3  # maximum incorrect answer
        global XP
        #The player can only play if the attempts is more than 0
        while attempts > 0:
            try:
                answer = int(input(f"Solve the sequence: {sequence} (What’s the next number?): "))
            except ValueError: #If player enter invalid value
                print("Enter a valid integer!")
                continue

            #Check the player's answer
            if answer == correct_answer:
                print("Correct!")
                XP += 20
                return True
            else:
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
    water_packet += 2
    print(f"\nUpdated Resources: oxygen: {oxygen}, water: {water}, food: {food}, energy: {energy}")
    


#if player choose to fix the oxygen tank
def OxygenTank():
    global oxygen
    global energy
    global XP
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
    timer = datetime.datetime.now() + datetime.timedelta(seconds=30) #setting the timer in 30 seconds
    target = random.randrange(51) #generating a number between 0 to 50

    print("\nOh I forgot to mention that you only have 30 seconds")
    while True:
        try:
            guess = int(input("Enter a number between 0 to 50: "))
        except ValueError: #if player enter invalid value
            print("Enter an interger!")
            continue
        remaining = (timer - datetime.datetime.now()).total_seconds() #calculating the remaining time
        if remaining < 0:
            print("Too late!  You lost!")
            energy -= 20
            print(f"\nUpdated Resources: oxygen: {oxygen}, water: {water}, food: {food}, energy: {energy} ")
            break
        if guess < target:
            print("Too low!") # the number guessed is too low
        elif guess > target:
            print("Too high!") # the number guessed is too high
        else:
            print("You got it!")
            oxygen += 100
            XP += 50
            print(f"\nUpdated Resources: oxygen: {oxygen}, water: {water}, food: {food}, energy: {energy} ")
            break
        print(f"{remaining:.0f} seconds left before you lose!")
      

#if player choose to go to the main room
def MainRoom():
    global energy
    global water_packet
    global food
    global XP
    import time

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

    answers = ("C", "D", "A", "A", "B")
    guesses = []
    score = 0
    question_num = 0

    # for each 'question' in the list, print the questions
    for question in questions:
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter (A, B, C, D): ").upper()
        while guess not in ["A", "B", "C", "D"]:
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
        message = input("Enter your message here : ")
        print("Sending...")
        time.sleep(1)
        print("Your message is sent.")
        energy -= 10
        water_packet += 1
        XP += 50
    else:
        print ("Your score didn't reach 60%")
        energy -= 20
        food -= 5
    print(f"\nUpdated Resources: oxygen: {oxygen}, water: {water}, food: {food}, energy: {energy} ")



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
      global XP
    # The correct order of words to form a sentence
      correctAnswer = ['I', 'am', 'playing', 'lost', 'in', 'Mars']
      print("Rearrange the words to repair the spaceship! You can only attempt once")
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
          XP += 50

      else:
          print(f"Incorrect! The correct order was: {' '.join(correctAnswer)}.") #display the correct order
          energy -= 20
          food -= 10
    OrderPuzzle()

    print(f"\nUpdated Resources: oxygen: {oxygen}, water: {water}, food: {food}, energy: {energy} ")

# if player choose to go to the toilet
def Toilet():
    global energy
    global food
    global water

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
    print(f"\nUpdated Resources: oxygen: {oxygen}, water: {water}, food: {food}, energy: {energy} ")


InsideSpaceShip()



#Check how to print inventory