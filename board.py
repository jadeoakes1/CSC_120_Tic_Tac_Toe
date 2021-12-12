#
# Jade Oakes
# 12/10/21
# Tic Tac Toe game:
# allows two users to take turns and place X's and O's
#


# Function to display game board
def print_board(game_board):
    print("Showing board:")
    for row in game_board:
        print(row)


# Function to get user input
def get_user_input():
    row = int(input("Enter row number (0-2): "))
    col = int(input("Enter column number (0-2): "))
    return row, col


# Function to check if mark can be placed at requested location on the board
def check_mark(row, col, game_board):  # Check if number is in range 0-1
    if (row < 0 or row > 2) or (col < 0 or col > 2):
        print("***Invalid row or column. Numbers must be between 0-2.***")
        print("***Please mark again.***")
        print_board(game_board)
        print()
        return False
    elif game_board[row][col] != "-":  # Check if row/column has already been selected
        print(f"***The location {row},{col} has already been selected.***")
        print("***Please mark somewhere else on the board.***")
        print_board(game_board)
        print()
        return False
    else:
        return True


# Function to place X or O on the board
def place_mark(player_id, game_board, row, col):
    if player_id == 1:
        game_board[row][col] = "X"
    elif player_id == 2:
        game_board[row][col] = "O"


# Function to determine if a player got three in a row
def check_row_win(game_board):
    # Player 1 win possibilities
    if game_board[0][0] == "X" and game_board[0][1] == "X" and game_board[0][2] == "X":
        print("Player 1 wins!")
        return True
    elif game_board[1][0] == "X" and game_board[1][1] == "X" and game_board[1][2] == "X":
        print("Player 1 wins!")
        return True
    elif game_board[2][0] == "X" and game_board[2][1] == "X" and game_board[2][2] == "X":
        print("Player 1 wins!")
        return True
    # Player 2 win possibilities
    elif game_board[0][0] == "O" and game_board[0][1] == "O" and game_board[0][2] == "O":
        print("Player 2 wins!")
        return True
    elif game_board[1][0] == "O" and game_board[1][1] == "O" and game_board[1][2] == "O":
        print("Player 2 wins!")
        return True
    elif game_board[2][0] == "O" and game_board[2][1] == "O" and game_board[2][2] == "O":
        print("Player 2 wins!")
        return True
    else:
        return False


# Function to determine if a player got three in a column
def check_col_win(game_board):
    # Player 1 win possibilities
    if game_board[0][0] == "X" and game_board[1][0] == "X" and game_board[2][0] == "X":
        print("Player 1 wins!")
        return True
    elif game_board[0][1] == "X" and game_board[1][1] == "X" and game_board[2][1] == "X":
        print("Player 1 wins!")
        return True
    elif game_board[0][2] == "X" and game_board[1][2] == "X" and game_board[2][2] == "X":
        print("Player 1 wins!")
        return True
     # Player 2 win possibilities
    elif game_board[0][0] == "O" and game_board[1][0] == "O" and game_board[2][0] == "O":
        print("Player 2 wins!")
        return True
    elif game_board[0][1] == "O" and game_board[1][1] == "O" and game_board[2][1] == "O":
        print("Player 2 wins!")
        return True
    elif game_board[0][2] == "O" and game_board[1][2] == "O" and game_board[2][2] == "O":
        print("Player 2 wins!")
        return True
    else:
        return False


# Function to determine if a player got three in a diagonal
def check_diag_win(game_board):
    # Player 1 win possibilities
    if game_board[0][0] == "X" and game_board[1][1] == "X" and game_board[2][2] == "X":
        print("Player 1 wins!")
        return True
    elif game_board[0][2] == "X" and game_board[1][1] == "X" and game_board[2][0] == "X":
        print("Player 1 wins!")
        return True
    # Player 2 win possibilities
    elif game_board[0][0] == "O" and game_board[1][1] == "O" and game_board[2][2] == "O":
        print("Player 2 wins!")
        return True
    elif game_board[0][2] == "O" and game_board[1][1] == "O" and game_board[2][0] == "O":
        print("Player 2 wins!")
        return True
    else:
        return False


# Function to determine if there was a tie
def check_tie(game_board):
    if not check_row_win(game_board) and not check_col_win(game_board) and not check_diag_win(game_board) and\
            game_board[0][0] != "-" and game_board[0][1] != "-" and game_board[0][2] != "-" and\
            game_board[1][0] != "-" and game_board[1][1] != "-" and game_board[1][2] != "-" and\
            game_board[2][0] != "-" and game_board[2][1] != "-" and game_board[2][2] != "-":
        print("Tie!")
        return True


def main():
    # Create an empty board
    board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
    # Initialize variables
    player1 = 1
    player2 = 2
    curr_player = player1  # Set current player to player1
    choice = "y"

    print("Welcome to Tic Tac Toe!\n")
    print("Player 1 is X")
    print("Player 2 is O\n")

    # Loop for continuous play until game is over
    while choice == "y":
        # Display empty board
        print_board(board)
        # Get user input from player
        print()
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

        # Toggle between player1 and player2
        if curr_player == player1:
            curr_player = player2
        else:
            curr_player = player1

        # Check if there is a winner
        if check_row_win(board) or check_col_win(board) or check_diag_win(board) or check_tie(board):
            print_board(board)  # Reset the board
            board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
            curr_player = player1  # Reset current player to player1
            # Check if users want to play again
            choice = input("\nAnother game (y/n)? ").lower()
    else:
        return False


main()
