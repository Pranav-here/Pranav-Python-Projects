import random

number = random.randint(1, 100)
again = "yes"

while again == "yes":
    player_guess = int(input("Guess the number between 1 to 100!\n"))
    if player_guess is number:
        print("You've guessed the number: " + str(number))
        again = "no"
    if player_guess > number:
        print("Try guess again!(Hint: Go for a lower number)")
    if player_guess < number:
        print("Try guess again!(Hint: Go for a higher number)")
