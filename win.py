# Function to check if there's a winner
def check_winner(board, player):
    win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # rows
                        (0, 3, 6), (1, 4, 7), (2, 5, 8), # columns
                        (0, 4, 8), (2, 4, 6)]            # diagonals
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_combinations)

# Function to check if the board is full (tie)
def check_tie(board):
    return all(space != " " for space in board)

# Function to check if the game is over (either a win or tie)
def is_game_over(board):
    return check_winner(board, "X") or check_winner(board, "O") or check_tie(board)
