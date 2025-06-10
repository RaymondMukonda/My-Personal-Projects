import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins


        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        while True:
            print("")
            playerchoice = input("Enter...\n1 for Rock, \n\n2 for Paper, or \n\n3 for Scissors:\n\n")
            player = int(playerchoice)

            if player < 1 or player > 3:
                sys.exit("You must enter 1, 2, 3.")

            computerchoice = random.choice("123")
            computer = int(computerchoice)

            print("")
            print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
            print("Pyton chose " + str(RPS(computer)).replace('RPS.', '') + ".")
            print("")
            def decide_winner(player, computer):
                nonlocal player_wins
                nonlocal python_wins
                if player == 1 and computer == 3:
                    player_wins += 1
                    return "You have won!😲🔥"
                elif player == 2 and computer == 1:
                    player_wins += 1
                    return "You have won!😊👌" 
                elif player == 3 and computer == 2:
                    player_wins += 1
                    return "You have won!😆✨" 
                elif player == computer:
                    return "It's a tie!😒"
                else:
                    python_wins += 1
                    return "Python has won🐍🐍"

            game_result = decide_winner(player, computer)
            print(game_result)

            nonlocal game_count
            game_count += 1
            print("\nGame Count: " + str(game_count))
            print("\nPlayer wins: " + str(player_wins))
            print("\nPyton wins: " + str(python_wins))

            play_again = input("\nWould you like to play again? (y/n): ").lower()
            if play_again != "y":
                print("Thanks for playing!")
                break

    return play_rps

    # sys.exit("Bye! 👋")

play = rps()

play()