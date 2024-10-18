# TIC-TAC-TOE GAME

# Printing the game board

def print_board(board):
    print(f"{board[0]}  |  {board[1]}  |  {board{2}}")
    print("--+---+--")
    print(f"{board[3]}  |  {board[4]}  |  {board{5}}")
    print("--+---+--")
    print(f"{board[6]}  |  {board[7]}  |  {board{8}}")
    
# checking if there is a winner

def check_winner(board,player):
    win_conditions = 
    [(0, 1, 2), (3, 4, 5) (6, 7, 8),]    #rows
    [(0, 3, 6), (1, 4, 7), (2, 5, 8)]    #columns
    [(0, 4, 8), (6, 4, 2)]               #diagonals
    
    for conditions in win_conditions :
        if board[condition[0]] == [condition[1]] == [condition[2]] == player:
            return True
        return False