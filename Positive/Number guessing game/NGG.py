import random
number = random.randint(1, 10)
print("Welcome to the game of the year")

guess = int(input("Enter your guess"))
trials = 1
while number != guess:
    print("Ooopsie wrong guess")
guess = int(input("Another trial please."))

