import random

options = ["rock", "paper", "scissors"]

user = input("Enter choice (rock/paper/scissors): ").lower()

if user not in options:
    print("Invalid choice")

else:
    computer = random.choice(options)

    print("Computer:", computer)

    if user == computer:
        print("Tie")

    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You Win!")

    else:
        print("Computer Wins!")