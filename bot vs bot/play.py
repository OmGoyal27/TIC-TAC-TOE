from win import is_game_over, check_winner
from bot_O import bot_move
from bot_X import human_bot_move

# Function to print the Tic-Tac-Toe board
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Main function to play the game
def play_game():
    board = [" "] * 9
    
    while not is_game_over(board):
        print_board(board)
        print()

        # Human's turn
        human_bot_move(board)

        if is_game_over(board):
            break

        # Bot's turn (unbeatable)
        bot_move(board)

    # Game over - print final board and result
    print_board(board)
    if check_winner(board, "X"):
        print("Congratulations! You win!")
    elif check_winner(board, "O"):
        print("Bot wins. Better luck next time!")
    else:
        print("It's a tie!")

# Start the game
play_game()
