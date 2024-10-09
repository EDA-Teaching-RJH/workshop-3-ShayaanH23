import random

secret_number = random.randint(1, 10)

guess = int(input("Guess a random number"))
if guess >= 10:
    print("Too High")
elif guess < 1:
    print("Too Low")

