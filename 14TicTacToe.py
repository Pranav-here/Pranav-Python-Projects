# Without using Modules

# This method is for printing the board

def print_board(spots):
    print(f"{spots[0]} | {spots[1]} | {spots[2]}\n---------\n{spots[3]} | {spots[4]} | {spots[5]}\n---------\n{spots[6]} | {spots[7]} | {spots[8]}")

def play_again(final_score):
    reply = input("Do you want to play again?(1,Yes)/(2,No)\n").strip().lower()
    while reply not in ["1", "yes", "2", "no"]:
        reply = input("Try Again, Choose from the options here(1,Yes)/(2,No)\n").strip().lower()


    if reply in ["1", "yes"]:
        play_game(final_score)

    elif reply in ["2", "no"]:
        print("Thank you for playing the game!")
        print(f"Here are the final scores\n Player 1: {final_score[0]}\n Player 2: {final_score[1]}")

def check_spot(spots, player_input):
    if spots[int(player_input)-1] == " ":
        return True
    else:
        return False
    # return True or False

def invalid_input(player_input, number, spot, n):
    # (1-9)
    numbers = ["1","2","3","4","5","6","7","8","9"]
    while player_input not in numbers:
        player_input = input(f"Spot not on board, Player {number} turn, playing for {spot[n % 2]} (Enter for an empty box): ")
        # if player_input in numbers:
        #     break
    return player_input

def game_over(spots, player_number, XO, final_score):
    '''
        To win : We need [1,2,3], [4,5,6], [7,8,9]
        1 2 3            [1,4,7], [2,5,8], [3,6,9]
        4 5 6            [1,5,9], [3,5,7]
        7 8 9
    '''
    win_condition = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
    for wc in win_condition:
        if spots[wc[0] - 1] == spots[wc[1] - 1] == spots[wc[2] - 1] != " ":
            print_board(spots)
            print(f"Game over! Player {player_number} wins, playing for {XO}")
            final_score[player_number-1] = final_score[player_number-1] + 1
            return True

        elif all(spot in ["X", "O"] for spot in spots):
            print_board(spots)
            print("Draw game!!! Well played!")
            return True

    print("\n")
    return False

def player_turn(n, spots, final_score):
    # win = False
    # while win == False:
    number = n % 2 + 1
    spot = ["O", "X"]
    print_board(spots)
    player_input = input(f"Player {number}'s turn, playing for {spot[n % 2]} [1-9]: ")
    player_input = invalid_input(player_input, number, spot, n)

    while check_spot(spots, player_input) == False:
        player_input = input(f"Spot Unavailable, Player {number}'s turn, playing for {spot[n % 2]} (Enter for an empty box): ")
        player_input = invalid_input(player_input, number, spot, n)

    spots[int(player_input) - 1] = spot[n % 2]
    return (game_over(spots, number, spot[n % 2], final_score))

    # return win

def play_game(final_score = [0, 0]):
    spots = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    # win = False
    n = 0
    while True:
        if player_turn(n, spots, final_score):
            break
        n += 1
    play_again(final_score)

print("Welcome to Two-Player Tic-Tac-Toe")
play_game()


