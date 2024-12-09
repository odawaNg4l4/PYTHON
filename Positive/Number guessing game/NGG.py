import random
number = random.randint(1, 10)
print("Welcome to the game of the year")

number_guess = int(input("Enter your guess"))
trials = 1
while number != number_guess:
    print("Oopsie wrong guess")
    if trials == 4:
        break
    elif number_guess < number:
        print("Your guess is lower")
    else:
        print("The guess is higher")


