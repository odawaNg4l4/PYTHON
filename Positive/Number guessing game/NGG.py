import random
number_to_guess = random.randint(1, 10)
print("Welcome to the game of the year")

guess = int(input("Enter your guess"))
trials = 1
while number_to_guess != guess:
    print("Oopsie wrong guess")
    if trials == 4:
            break
    elif guess < number_to_guess:
            print("Your guess is lower")
    else:
            print("The guess is higher")

    guess = int(input("Please guess again"))
    trials += 4

if number_to_guess == guess:
    print("Well done you won")
    print("You took", trials, "goes to  complete the game")
else:
    print("Sorry - you lose")
    print("The number you were to guess", number_to_guess)
print("Game over")
