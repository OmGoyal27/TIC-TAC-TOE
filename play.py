from win import is_game_over, check_winner
from bot import bot_move

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
    human_player = "X"
    
    while not is_game_over(board):
        print_board(board)

        # Human's turn
        move = input(f"Player {human_player}, choose a position (1-9): ")
        if not move.isdigit() or int(move) < 1 or int(move) > 9 or board[int(move) - 1] != " ":
            print("Invalid move. Try again.")
            continue
        board[int(move) - 1] = human_player

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
