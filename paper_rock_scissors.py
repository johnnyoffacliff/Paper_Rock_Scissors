import random

choices = ["paper", "rock", "scissors"]
player_score = 0
computer_score = 0

while True:
    while player_score < 3 and computer_score < 3:
        player_choice = input("Choose paper, rock or scissors ").lower()

        computer_choice = (random.choice(choices))

        if player_choice not in choices:
            print(f"{player_choice} is an invalid entry")
        elif player_choice == computer_choice:
            print(f"Computer chooses {computer_choice}, it's a draw")
        elif (player_choice == "paper" and computer_choice == "rock" or
              player_choice == "rock" and computer_choice == "scissors" or
              player_choice == "scissors" and computer_choice == "paper"):
            print(f"Computer chooses {computer_choice}! {player_choice} beats {computer_choice}!")
            player_score += 1
        else:
            print(f"Computer chooses {computer_choice}! {player_choice} loses to {computer_choice}!")
            computer_score += 1
        print(f"Computer score: {computer_score} \nPlayer score: {player_score}")

    print(f"Final score is: \nComputer Score:{computer_score} \nPlayer Score {player_score}")
    if player_score > computer_score:
        print("****YOU WIN****")
    else:
        print("You lose :(")
    play_again = input("Play again? Y/N ").lower()

    if play_again != "y":
        print("goodbye")
        break
