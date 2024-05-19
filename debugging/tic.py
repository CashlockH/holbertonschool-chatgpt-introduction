#!/usr/bin/python3
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " " or \
           board[0][i] == board[1][i] == board[2][i] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " " or \
       board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

def validate_input(prompt, valid_inputs):
    while True:
        user_input = input(prompt)
        if user_input.isdigit() and int(user_input) in valid_inputs:
            return int(user_input)
        print("Invalid input. Please enter a valid choice.")

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        row = validate_input("Enter row (0, 1, or 2) for player " + player + ": ", [0, 1, 2])
        col = validate_input("Enter column (0, 1, or 2) for player " + player + ": ", [0, 1, 2])
        if board[row][col] == " ":
            board[row][col] = player
            if player == "X":
                player = "O"
            else:
                player = "X"
        else:
            print("That spot is already taken! Try again.")

    print_board(board)
    if check_winner(board):
        if player == "X":
            print("Player O wins!")
        else:
            print("Player X wins!")

tic_tac_toe()
