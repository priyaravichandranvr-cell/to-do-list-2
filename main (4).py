# Rock Paper Scissors Game

import random

print("---- ROCK PAPER SCISSORS ----")

options = ["rock", "paper", "scissors"]

while True:
    user = input("Enter rock / paper / scissors: ").lower()

    comp = random.choice(options)
    print("Computer chose:", comp)

    if user == comp:
        print("It's a tie")

    elif user == "rock":
        if comp == "scissors":
            print("You win")
        else:
            print("You lose")

    elif user == "paper":
        if comp == "rock":
            print("You win")
        else:
            print("You lose")

    elif user == "scissors":
        if comp == "paper":
            print("You win")
        else:
            print("You lose")

    else:
        print("Wrong input")

    again = input("Play again? (yes/no): ")
    if again != "yes":
        print("Game ended")
        break