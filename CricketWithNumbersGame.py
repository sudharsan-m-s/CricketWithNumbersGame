#Cricket With Numbers Game
#Coded by Sudharsan.M.S

# Importing required libraries: random for randomness, time for delays
import random
import time

# --- Beginning of the game, displaying welcome message for user ---
print ("Welcome to the game 'Cricket With Numbers' \n It's time for the toss ")
time.sleep(2)
#Explaining the rules for toss....
print(" \n Toss Rule: You have to choose a toss choice : ODD or EVEN \n Then , You and computer will be choosing a number between 1 to 10 simulatneously.. \n If the sum of two numbers equals your toss choice(odd or even),.. then you win the toss ! \n Otherwise computer wins ! ")
time.sleep(10)

#------ TOSS LOGIC----------------------------
#Asking the user's toss preference
player_toss_choice = input("\n Enter ODD or EVEN :")
if player_toss_choice == "EVEN" or "ODD" :
    print ("OK")
#Checking for any invalid toss preferences
else :
    print("Enter a valid toss choice!")
    exit("TRY AGAIN")
#Asking the user to choose a number from 1 to 10 for the toss
player_toss_number = int(input("Enter a number between 0 and 11 : "))
if player_toss_number > 0 and player_toss_number < 11 :
    print("DONE!")
#Checking for any input numbers, that is out of given range!
else :
    print("Number should be more than 0 as well as less than 11! ")    
    exit("TRY AGAIN")
#Making the computer to pick a number from the same range for the toss
computer_toss_number = random.randint(1,10)
time.sleep(2)
#Displaying the computer's chosen toss number
print("The computer has chosen", computer_toss_number )

#----------------------TOSS RESULT--------------------------------------
#Providing the arithmetic formula to add up user's number and computer's number 
# checking whether the sum is odd or even, to determine the toss result 
toss_sum = player_toss_number + computer_toss_number
toss = "EVEN" if int(toss_sum) % 2 == 0 else "ODD"
time.sleep(3)

#Listing out the available playing options for user as well as computer, 
# after winning the toss
computer_choices = ['BAT', 'BOWL']
player_choices = ['BAT', 'BOWL']
computer_choice = random.choice(computer_choices)
player_choice = input("YOU won the toss!! \n Would you like to BAT or BOWL? ") if player_toss_choice == toss else print("You have lost the toss!")
if player_choice in player_choices:
    time.sleep(1)
    print ("Alright! Let's begin the game!")
elif (player_choice in player_choices) or (player_toss_choice != toss and computer_choice in computer_choices) :
    print("Waiting for computer's decision...")
    time.sleep(1.5)
else:
    print("Invalid play option.. Try Again")
    exit()
print("Computer opted to bat first \n Let's begin the game!") if computer_choice == player_choices[0] and player_toss_choice != toss else print("Computer opted to bowl first.. \n Let's begin the game!") if computer_choice == player_choices[1] and player_toss_choice != toss else print("")
time.sleep(2)

#------------------RULES-----------------------------------------
#Printing the rules to the user, how to play this gamw\e
print(" \n Rules of the Game: \n You and computer are opted to choose a number between 0 and 11 \n Whoever bats, their numbers would be added to their score.. \n When the numbers opted by you and computer matches(likely numbers), then whoever bats gets out and then bowler gets his chance to chase down the target posted by batter.. \n If the target chased down successfully, game won by the chaser , otherwise opponent wins.")

time.sleep(10)

#------------BEGINNING OF THE GAMEPLAY---------------------------------------
#Here,we code for the playing options opted by computer or user, so that we could determine
#who's gonna bat first and posting their targets to the opponent
if (computer_choice == player_choices[0] and player_toss_choice != toss) or (player_choice == player_choices[1]) :
    print("\n \n The computer will be batting now!")  
    time.sleep(2)

    #***********************************************************************1st INNINGS******************************************************************************************************************************************************
    #In this case, computer's input will be successively added if, 
    # either computer opted to bat first or user opted to bowl first.
    computer_score = 0
    while True:
        #Introducing an infinite while loop here to ask input from the user, 
        #until the user input number and computer input matches and
        #computer loses its wicket to the user
        computer_num_bt = random.randint(1,10)
        player_num_bl = int(input("\n Your number to bowl: "))
        if (player_num_bl > 0 and player_num_bl < 11 ):
            print("OK! Let's check what computer have chosen..")
        else:
            print("Number should be between 0 and 11")
            exit()
        time.sleep(1.7)
        print("Computer chose",computer_num_bt)
        #Successive addition of computer's input until computer loses its wicket 
        #in order to calculate the score of computer...
        computer_score += computer_num_bt
        print("Computer have scored",computer_score) if computer_num_bt != player_num_bl else print("Total score of computer is",((computer_score - computer_num_bt)),"runs!")
        #Here we use two different outputs for different possibilities
        #If the inputs from both (user and computer) doesn't matches, then computer's last input would be added to its total score
        #But if those inputs matches, then the computer's last input number won't be considered for calculating the computer's score
        #So that we are subtracting the computer's last input from the total computer score to get the final score of computer
        if computer_num_bt == player_num_bl :
            print("Yes! That's a wicket! \n Your score target is",((computer_score-computer_num_bt)+1),"runs to win the game!") if computer_score != 0 else print("Yes! That's a wicket! \n Your score target is just 1 run to win the game!")
        #Generally, in cricket, target runs for the opponent would be one run more than their total score
        #According to this,here the user needs to get one run more than the computer's final score

     #***********************************************************************2nd INNINGS******************************************************************************************************************************************************   
            
            time.sleep(3)
            print("\n \n You will be batting now!")
            #Now it's time for the user to bat 
            your_score = 0
            while True :
                computer_num_bl = random.randint(1,10)
                player_num_bt = int(input("\n Enter your number to score: "))
                if (player_num_bt > 0 and player_num_bt < 11 ):
                    print("OK! Let's check what computer have chosen..")
                else:
                    print("Number should be between 0 and 11")
                    exit()
                time.sleep(1)
                print("Computer chose",computer_num_bl)
                #Asusual successive addition of user inputs to get user's total score
                your_score += player_num_bt
                print("You have scored",your_score,"runs") if computer_num_bl != player_num_bt  else print("You have scored",((your_score- player_num_bt)),"runs") if computer_num_bl == player_num_bt else "" 
                #When the user's score surpassed the computer's final score, then user wins the game!
                if (computer_num_bl != player_num_bt  and your_score > (computer_score-computer_num_bt)) :
                    print("YES! You have surpassed the computer's score of",(computer_score-computer_num_bt),"runs! \n You won this game! Congratulations!!")
                    exit()
                #When the user gets out after their score lower than computer's final score,
                #Then, user loses the game here....
                elif (computer_num_bl == player_num_bt and (your_score - player_num_bt) < (computer_score-computer_num_bt)) :
                    print("Oh no! That's a wicket! You didn't surpassed the computer score of",(computer_score-computer_num_bt),"runs \n You have lost this game!! Better luck next time!")
                    exit()
                #The condition of tie breaker if both of the final scores equalizes...........
                elif (computer_num_bl == player_num_bt and (your_score - player_num_bt) == (computer_score-computer_num_bt)):
                    print("Oh no! That's a tie! Scores level! Let's see who gonna win this game with a tie breaker!")
                    time.sleep(1.9)
                    #Explaining the rules of the tie breaker
                    print("RULES FOR THE TIE BREAKER ROUND! \n In this round, only the numbers from 1 to 4 are allowed. \n You are allowed to bat first in this tie breaker! \n As per the game rule, you and computer allowed to choose a number from 1 to 4 \n You will be scoring till you lose your wicket, and then computer will start score! \n  If computer fails to chase your target, you win this game! Else, computer wins! \n NOTE: If there's a tie in this tie breaker, then the match will be declared drawn !")
                    time.sleep(15)
        
        
        #****************************************************************TIE BREAKER****************************************************************************************************************************************************
                    #Successive addition of user's score in the tie breaker round
                        #Until the inputs match, game continues
                        #If inputs match, user is out and computer's turn begins

                    print("\n \n You will be batting now!")
                    your_score_tb = 0
                    while True:
                        computer_num_tb_bl = random.randint(1,4)
                        your_num_tb_bat = int(input("\n Enter your number to score(only from 1 to 4): "))
                        if (your_num_tb_bat > 0 and your_num_tb_bat < 5 ):
                            print("OK! Let's check what computer have chosen..")
                        else:
                            print("Number should be from 1 to 4")
                            exit()
                        time.sleep(1.3)
                        print("Computer chose",computer_num_tb_bl)
                        your_score_tb += your_num_tb_bat
                        print("You have scored", your_score_tb,"runs.") if your_num_tb_bat != computer_num_tb_bl else print("Your total score in this tie breaker is",((your_score_tb - your_num_tb_bat)),"runs.") if your_num_tb_bat == computer_num_tb_bl else ""
                        if computer_num_tb_bl == your_num_tb_bat :
                            print("OOPS! You have lost your wicket !\n Computer needs just",((your_score_tb - your_num_tb_bat)+1), "runs to win this tie breaker as well as the game!") if your_score_tb != 0 else print("You have lost your wicket for a duck! Computer needs just 1 run to win this tie breaker!")                            # 
                    
                    
                    #****************************************************************TIE BREAKER(2nd INNINGS)****************************************************************************************************************************************************
                    #Computer's batting turn in tie breaker begins now
                        print("\n \n Computer will be batting now!")
                        computer_score_tb = 0
                    #Introducing infinite loop for computer's tie breaker batting round
                        while True:
                            computer_num_tb_bat = random.randint(1,4)
                            your_num_tb_bl = int(input("\n Enter your number to bowl: "))
                            if (your_num_tb_bl > 0 and your_num_tb_bl < 5 ):
                                print("OK! Let's check what computer have chosen..")
                            else:
                                print("Number should be from 1 to 4")
                                exit()
                            time.sleep(1.3)
                            print("Computer chose",computer_num_tb_bat)
                            computer_score_tb += computer_num_tb_bat
                            #Calculating total score of computer in tie breaker
                            print("Computer have scored",computer_score_tb,"runs.") if your_num_tb_bl != computer_num_tb_bat else print("Total score of computer in this tie breaker is",((computer_score_tb-computer_num_tb_bat)),"runs.")
                            #Conditions to determine match result based on computer's score
                            if (computer_num_tb_bat == your_num_tb_bl) and (computer_score_tb < (your_score_tb-your_num_tb_bat)) :
                                print("Yes! You have succesfully defended your score! Congratulations ! You won this game via tie breaker round!")
                            #If computer fails to chase user score, user wins    
                                exit()
                            elif (computer_num_tb_bat == your_num_tb_bl) and (computer_score_tb - computer_num_tb_bat) > (your_score_tb-your_num_tb_bat):
                                print("Oh no! The computer surpassed your score in this tie breaker! You have lost this game! Better luck, next time!")
                            #If computer surpasses user score, computer wins
                                exit()
                            elif (computer_num_tb_bat == your_num_tb_bl and (computer_score_tb - computer_num_tb_bat) == (your_score_tb-your_num_tb_bat)):
                                print("Again! Scores level in a tie breaker too! So , this match has been drawn now! Well played !")
                            #If scores level, match is drawn    
                                exit()
                            else:
                                print()

#If player wins the toss and opts to bat first, or computer opts to bowl first
    #Then, player bats first
elif (player_choice == player_choices[0]) or (computer_choice == player_choices[1] and player_toss_choice != toss):
    print("\n \n You will be batting now!")
   
    #******************************************1st INNINGS*******************************************************************************************************
    
    your_score = 0
    #Loop begins for player's batting innings
    while True:
        computer_num_bl = random.randint(1,10)
        player_num_bt = int(input("\n Your number to score: "))
        if (player_num_bt > 0 and player_num_bt <11) :
            print("OK! Let's check what computer have chosen!")
        else:
            print("The number should be between 0 and 11")
            exit()
        time.sleep(1.7)
        print("Computer chose",computer_num_bl)
        #User's score accumulates unless computer number matches with user's number
        your_score += player_num_bt
        print("You have scored", your_score) if player_num_bt != computer_num_bl else print(" Your total score is",(your_score - player_num_bt),"runs!")
        #On matching, user is out and computer's innings starts
        if computer_num_bl == player_num_bt:
            print("Oh no! You have lost your wicket for",((your_score-player_num_bt)),"runs. Defend the computer score below this to win the game")
            print("\n \n Computer will be batting now!")


            #****************************2nd INNINGS*************************************************************************************************************
            #Computer's turn to chase down the target set by user
            computer_score = 0
            while True :
                #Loop to accumulate computer score until computer gets out or surpasses player score
                computer_num_bt = random.randint(1,10)
                player_num_bl = int(input("\n Enter your number to bowl: "))
                if (player_num_bl > 0 and player_num_bl < 11 ):
                    print("OK! Let's check what computer have chosen..")
                else:
                    print("Number should be between 0 and 11")
                    exit()
                time.sleep(1.7)
                print("Computer chose", computer_num_bt)
                computer_score += computer_num_bt
                print("Computer have scored",computer_score, "runs.") if computer_num_bt != player_num_bl else print("Total score of computer is",((computer_score - computer_num_bt)),"runs") if computer_num_bt == player_num_bl else ""
                #Conditions to determine winner or tie based on score comparison
                if (computer_num_bt != player_num_bl  and your_score < computer_score) :
                    print("Oh no! Computer have surpassed your total score of",your_score,"runs! \n You have lost this game! Better luck next time!")
                    #Computer wins if it surpasses the player's score
                    exit()
                elif (computer_num_bt == player_num_bl and your_score > computer_score) :
                    print("Yes! That's a wicket! You have successfully defended your score of",(your_score-player_num_bl),"runs \n You have won this game by",((your_score-player_num_bl)-(computer_score-computer_num_bt)),"runs. Congratulations!!")
                    #Player wins if they take computer's wicket before score is surpassed
                    exit()
                elif (computer_num_bt == player_num_bl and your_score == computer_score):
                    #If scores level, tie breaker will be triggered
                    print("Oh no! That's a tie! Scores level! Let's see who gonna win this game with a tie breaker!")
                    time.sleep(1.9)
                    print("RULES FOR THE TIE BREAKER ROUND! \n In this round, only the numbers from 1 to 4 are allowed. \n Computer will be allowed to bat first in this tie breaker! \n As per the game rule, you and computer allowed to choose a number from 1 to 4 \n Computer will be scoring till you take it's wicket, and then you will start score! \n  If computer fails to defend its score, you win this game! Else, computer wins! \n NOTE: If there's a tie in this tie breaker, then the match will be declared as DRAWN !")
                    time.sleep(15)
                    #Explaining the tie breaker rules if scores are level
                    
                    #******************************TIE BREAKER*********************************************************************************************************************************************************************
                    #Tie breaker begins - computer bats first
                    print("\n \n Computer will be batting now!")
                    computer_score_tb = 0
                    while True:
                        computer_num_tb_bt = random.randint(1,4)
                        your_num_tb_bl= int(input("\n Enter your number to score(only from 1 to 4): "))
                        if (your_num_tb_bl > 0 and your_num_tb_bl < 5 ):
                            print("OK! Let's check what computer have chosen..")
                        else:
                            print("Number should be from 1 to 4")
                            exit()
                        time.sleep(1.3)
                        print("Computer chose",computer_num_tb_bt)
                        computer_score_tb += computer_num_tb_bt
                        #Runs get added unless inputs match (wicket falls)
                        #Once out, it's user's turn to bat
                        print("Computer have scored",computer_score_tb,"runs.") if computer_num_tb_bt != your_num_tb_bl else print("Total score of computer in this tie breaker is",((computer_score_tb - computer_num_tb_bt)),"runs.") if computer_num_tb_bt == your_num_tb_bl else ""
                        if your_num_tb_bl == computer_num_tb_bt :
                            print("Yes! You have made computer out for",((computer_score_tb -computer_num_tb_bt)),"runs. You need",((computer_score_tb -computer_num_tb_bt)+1),"runs to win this tie breaker!")                            # 
                        
                        #*******************************TIE BREAKER(2nd INNINGS)******************************************************************************************************************************************************
                        
                        #User's turn to chase target in tie breaker
                        #User needs to surpass computer's score to win
                        print("\n You will be batting now!")
                        your_score_tb = 0
                        while True:
                            computer_num_tb_bl = random.randint(1,4)
                            your_num_tb_bat = int(input("\n Enter your number to bowl: "))
                            if (your_num_tb_bat > 0 and your_num_tb_bat < 5 ):
                                print("OK! Let's check what computer have chosen..")
                            else:
                                print("Number should be from 1 to 4")
                                exit()
                            time.sleep(1.3)
                            print("Computer chose",computer_num_tb_bl)
                            your_score_tb += your_num_tb_bat
                            print("You have scored",your_score_tb,"runs.") if computer_num_tb_bl != your_num_tb_bat else print("Your total score in this tie breaker is",((your_score_tb-your_num_tb_bat)),"runs.")
                            if (your_num_tb_bat == computer_num_tb_bl) and ((computer_score_tb - computer_num_tb_bt) < (your_score_tb-your_num_tb_bat)) :
                                print("Yes! You have succesfully chased down the target! Congratulations ! You won this game via tie breaker round!")
                                exit()
                            elif (your_num_tb_bat == computer_num_tb_bl) and ((computer_score_tb - computer_num_tb_bt) > (your_score_tb-your_num_tb_bat)):
                                print("Oh no! You didn't surpassed the computer's score in this tie breaker! You have lost this game! Better luck, next time!")
                                #If score less than target,computer wins the game
                                exit()
                            elif (your_num_tb_bat == computer_num_tb_bl and (computer_score_tb - computer_num_tb_bt) == (your_score_tb-your_num_tb_bat)):
                                print("Again! Scores level in a tie breaker too! So ,this match has been drawn now! Well played !")
                                #If score equals, match drawn
                                exit()
                            else:
                                print()
                else:
                    print()
        else:
            print()
else:
   print()         
                
#THE END!
