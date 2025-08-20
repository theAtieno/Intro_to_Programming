# Rock Paper Scissors Game
# Build a Human-versus-Computer Rock-Paper-Scissors Game
# In this project, you will create a script to allow the user to play rock-paper-scissors against the computer. For starters, if you are not familiar with the game, you need to understand that: rock beats scissors, scissors beats paper, and paper beats rock. Here are the steps to follow in build your game:

# Utilise the Random Python Library to allow the computer to randomly choose rock, paper, or scissors in each round
# Allow the user to now input their choice and compare it directly with the computer’s choice. You can then declare the winner of the round based on the rules of the game
# You can now freely play rock-paper-scissors with your computer and see how well you perform against the computer’s randomised choices.
# # Now, instead of declaring the winner, just assign a point to the winner of a round. This should allow you to utilise loops to increase the rounds within a game to 3 or 5. Your program will assign points to the winner of each round and declare the winner after all rounds i.e the one with the most points.

import random

options = ("rock", "paper", "scissors")

rounds = int(input("Enter number of rounds (5 or 3) "))

my_score = 0
computer_score = 0

for i in range(rounds) :
    computer_choice = random.choice(options)
    my_choice = input("Enter a choice between rock/paper/scissors: ")
    
    print("You chose:", my_choice)
    print("Computer chose:" , computer_choice)

    if my_choice == computer_choice :
        print("Tie. No points")
    elif (
        (my_choice == "rock" and computer_choice == "scissors") or
        (my_choice == "scissors" and computer_choice == "paper") or
        (my_choice == "paper" and computer_choice == "rock")
        ):
        print("You win this round")
        my_score +=1
    else :
        print("Computer wins this round")  
        computer_score += 1

print("My total score is" , my_score)
print("Computer total score is" , computer_score)

if my_score < computer_score :
    print("Computer wins this round")
elif my_score > computer_score :
    print("You win this round")
else :
    print("Its a tie")
    
# To make the game more efficient, stop the game and declare the winner immediately a user guess 2 points out of 3 in a 3-round game or 3 out of 5 points in a 5-round game. This should stop the game from continuing when there’s already a clear winner even if all rounds have not been completed.

import random

options = ("rock", "paper", "scissors")

rounds = int(input("Enter number of rounds (5 or 3): "))

while rounds not in [3,5] :
    print("Invalid entry. Enter 3 or 5")
    rounds = int(input("Enter number of rounds (5 or 3): "))


current_round = 1
winning_round = rounds//2 + 1

my_score = 0
computer_score = 0

while current_round <= rounds :
    computer_choice = random.choice(options)
    my_choice = input("Enter a choice between rock/paper/scissors: ")
    
    print("You chose:", my_choice)
    print("Computer chose:" , computer_choice)

    if my_choice == computer_choice :
        print("Tie. No points")
    
    elif (
        (my_choice == "rock" and computer_choice == "scissors") or
        (my_choice == "scissors" and computer_choice == "paper") or
        (my_choice == "paper" and computer_choice == "rock")
        ):
        print("You win this round")
        my_score +=1
    
    else :
        
        print("Computer wins this round")  
        computer_score += 1

    print("Your score:", my_score , "Computer score:" , computer_score)

    if my_score == winning_round or computer_score == winning_round :
        break
    current_round += 1

print("Final score")
print("My final score" , my_score , computer_score, "Computer final score")
