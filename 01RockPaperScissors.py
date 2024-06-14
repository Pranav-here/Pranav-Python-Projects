import random

comp_score = 0
player_score = 0
again = "yes"


while again == "yes":
    player_choice = input("Rock, Paper or Scissors: ")
    choices = ["Rock", "Paper", "Scissors"]
    comp_choice = random.choice(choices)

    if player_choice == comp_choice:
        again = input("Draw! Do you want to play again?")
    elif player_choice == "Rock" and comp_choice == "Scissors":
        again = input("You win! Do you want to play again?")
        player_score = player_score + 1
    elif player_choice == "Paper" and comp_choice == "Rock":
        again = input("You win! Do you want to play again?")
        player_score = player_score + 1
    elif player_choice == "Scissors" and comp_choice == "Paper":
        again = input("You win! Do you want to play again?")
        player_score = player_score + 1
    elif comp_choice == "Scissors" and player_choice == "Paper":
        again = input("Computer wins! Do you want to play again")
        comp_score = comp_score + 1
    elif comp_choice == "Paper" and player_choice == "Rock":
        again = input("Computer wins! Do you want to play again")
        comp_score = comp_score + 1
    elif comp_choice == "Rock" and player_choice == "Scissors":
        again = input("Computer wins! Do you want to play again")
        comp_score = comp_score + 1
    else:
        again = "yes"
        print("Irrelevant Output! Try again")


print("Final Score: " + str(comp_score) + " - " + str(player_score))
