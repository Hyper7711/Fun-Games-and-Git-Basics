# Tic-Tac-Toe game in Python

# Function to print the game board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")


# Function to check if there's a winner
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
                      (0, 4, 8), (2, 4, 6)]  # diagonals
    for condition in win_conditions:
        if (board[condition[0]] == board[condition[1]] ==
                board[condition[2]] == player):
            return True
    return False


# Function to check if the board is full (i.e., a tie)
def check_tie(board):
    return ' ' not in board


# Main game loop
def tic_tac_toe():
    board = [' '] * 9  # A list to represent the board (9 empty spaces)
    current_player = "X"  # Player X starts first

    while True:
        print_board(board)
        move = int(
            input(f"Player {current_player}, enter your move (1-9): ")
            ) - 1

        # Check if the move is valid
        if board[move] == ' ':
            board[move] = current_player
        else:
            print("Invalid move, try again.")
            continue

        # Check if the current player wins
        if check_winner(board, current_player):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break

        # Check if the game is a tie
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch to the other player
        current_player = "O" if current_player == "X" else "X"


# Run 
if __name__ == "__main__":
    tic_tac_toe()
    
