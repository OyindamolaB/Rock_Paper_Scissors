import random

R = 1
P = 2 
S = 3

def RPS():
    player = input("Enter a choice(R, P, S):")
    possible_options = [R, P, S]

    computer_action = random.choice(possible_options)
    if player == computer_action:
        print(f"Both players selected {player}. It's a tie! Repeat")
    elif player == "R":
        if computer_action == "S":
            print("Rock beats scissors! You win!")
        else:
            print("Paper beats rock! You lose.")
    elif player == "P":
        if computer_action == "R":
            print("Paper beats rock! You win!")
        else:
            print("Scissors beats paper! You lose.")
    elif player == "S":
        if computer_action == "P":
            print("Scissors beats paper! You win!")
        else:
            print("Rock beats scissors! You lose.")
    restart = input("Would you like to restart this program?")
    if restart == "yes" or restart == "y":
        RPS()
    if restart == "n" or restart == "no":
        print ("Script terminating. Goodbye.")
RPS()
