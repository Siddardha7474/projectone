import random
number = random.randint(1, 100)
while True:
    guess = int(input("Enter your guess: "))
    if guess == number:
        print("Correct Guess!")
        break
    elif guess < number:
        print("Too Low")
    else:
        print("Too High")