def print_board(board):
    """Prints the current state of the Tic Tac Toe board."""
    print("Current board:")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Checks if there is a winner."""
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]  # Row winner
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]  # Column winner
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]  # Diagonal winner
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]  # Diagonal winner
    
    return None 

def is_draw(board):
    """Checks if the game is a draw."""
    for row in board:
        if ' ' in row:
            return False
    return True  

def tic_tac_toe():
    """Main function to run the Tic Tac Toe game."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    # Get player names
    player1 = input("Enter the name of Player 1 (X): ")
    player2 = input("Enter the name of Player 2 (O): ")
    
    current_player = player1  # Start with Player 1
    current_symbol = 'X'  # Player 1 is 'X'

    while True:
        print_board(board)
        try:
            row = int(input(f"{current_player}, enter your row (0, 1, or 2): ")) 
            col = int(input(f"{current_player}, enter your column (0, 1, or 2): ")) 
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid position. Please choose from 0, 1, or 2.")
            continue

        if board[row][col] != ' ':
            print("This spot is already taken. Choose another one.")
            continue

        # Place the player's mark on the board
        board[row][col] = current_symbol

        # Check for a winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"{current_player} wins!")
            break

        # Check for a draw
        if is_draw(board):
            print_board(board)
            print("The game is a draw!")
            break

        # Switch players
        if current_player == player1:
            current_player = player2
            current_symbol = 'O'
        else:
            current_player = player1
            current_symbol = 'X'

if __name__ == "__main__":
    tic_tac_toe()