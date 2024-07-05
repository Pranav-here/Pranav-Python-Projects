# The first to reach 21 loses, first to reach a multiple of 4 eventually wins
# you can choose upto 3 numbers

import random

def player_input(l):
    player = int(input("How many numbers do you want to play: "))
    while player>3:
        player = int(input("Enter a number between 0 and 3: "))
    for i in range(player):
        number = input("Enter your number: ")
        l.append(int(number))
    return l


def computer_output(l):
    last_value = l[-1]
    num_of_values = abs(4-(last_value%4))
    for i in range(last_value+1, last_value+num_of_values+1):
        l.append(i)
    return l


def game_over():
    print("The computer won")
    print("We have reached the end of the game, thank you for playing it!")


print("Welcome to the 21 number game!")
print("Please pick upto 3 consecutive numbers")

l = []

player_input(l)
computer_output(l)
print(f"The sequence after the computer's turn is {l}")

player_input(l)
computer_output(l)
print(f"The sequence after the computer's turn is {l}")

player_input(l)
computer_output(l)
print(f"The sequence after the computer's turn is {l}")

player_input(l)
computer_output(l)
print(f"The sequence after the computer's turn is {l}")

player_input(l)
computer_output(l)
print(f"The sequence after the computer's turn is {l}")

game_over()

