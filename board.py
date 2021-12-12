#
# Jade Oakes
# 12/10/21
# This program is a Tic Tac Toe game and allows two users to take turns and make moves
#

# user_input --> something 1-9
# if they enter anything else, tell them to go again
# check if user_input is already taken
# add it to the board
# check if user won (rows, columns, diagonals)
# toggle between users upon successful moves


# Function to display game board
def print_board(game_board):
    print("Showing board:")
    for row in game_board:
        print(row)
    print()


# Function to get user input
def get_user_input():
    row = int(input("Enter row number (0-2): "))
    col = int(input("Enter column number (0-2): "))
    return row, col


# Function to check if mark can be placed at requested location on the board
def check_mark(row, col, game_board):
    if (row < 0 or row > 2) or (col < 0 or col > 2):
        print("***Invalid row or column. Numbers must be between 0-2.***")
        print("***Please mark again.***")
        print_board(game_board)
        return False
    elif game_board[row][col] != "-":
        print(f"***The location {row},{col} has already been selected.***")
        print("***Please mark somewhere else on the board.***")
        print_board(game_board)
    else:
        return True


def place_mark(player_id, game_board, row, col):
    if player_id == 1:
        game_board[row][col] = "X"
    elif player_id == 2:
        game_board[row][col] = "O"


def check_win():
    pass


def main():
    # Create an empty board
    board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

    # Display empty board
    print_board(board)

    # Initialize player variable
    player1 = 1
    player2 = 2
    curr_player = player1
    while curr_player:
        # Get user input from player
        print(f"Player {curr_player}, make your move")
        row_input, col_input = get_user_input()
        # Check if input is a number between 0-2
        while not check_mark(row_input, col_input, board):
            row_input, col_input = get_user_input()

        # Display the row and column numbers
        print()
        print(f"Player {curr_player} added mark at the location {row_input},{col_input}")
        # Place the correct mark on the board
        place_mark(curr_player, board, row_input, col_input)
        # Display board after each turn
        print_board(board)

        # Toggle between player1 and player2
        if curr_player == player1:
            curr_player = player2
        else:
            curr_player = player1


main()
