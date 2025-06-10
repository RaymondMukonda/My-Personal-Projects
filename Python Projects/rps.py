import sys
import random
from enum import Enum

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    while True:
        print("")
        playerchoice = input("Enter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")
        player = int(playerchoice)

        if player < 1 or player > 3:
            sys.exit("You must enter 1, 2, 3.")

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print("")
        print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
        print("Pyton chose " + str(RPS(computer)).replace('RPS.', '') + ".")
        print("")
        if player == 1 and computer == 3:
            print("You have won!😲🔥 ")
        elif player == 2 and computer == 1:
            print("You have won!😊👌 ")
        elif player == 3 and computer == 2:
            print("You have won!😆✨ ")
        elif player == computer:
            print("It's a tie!😒")
        else:
            print("Python has won🐍🐍 ")

        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing!")
            break

# sys.exit("Bye! 👋")

play_rps()
