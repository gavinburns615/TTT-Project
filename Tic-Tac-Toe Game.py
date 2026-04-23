# Tic-Tac-Toe Game

def print_board(board):
    """
    - Function to print the current state of the game board
    - This function takes a 2D list representing the game board and prints it in a formatted manner, showing the current positions of X's and O's
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """"
    - Function to check if a player has won the game
    - This function checks all possible winning combinations (rows, columns, diagonals) for the specified player and returns True if a winning combination is found, otherwise it returns False
    """
    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def is_draw(board):
    """
    - Function to check if the game has resulted in a draw
    """
    for row in board:
        for spot in row:
            if spot == " ":
                return False
    return True

def print_score(score):
    """
    - Function to print the current score of the game
    - This function takes a dictionary containing the scores for both players and the number of draws, and prints it in a formatted manner
    """
    print(f"Score X: {score['X']}  |  O: {score['O']}  |  Draws: {score['Draw']}\n")

def main():
    """
    - Main function to run the Tic-Tac-Toe game
    - This function initializes the game, manages the game loop, and handles user input for playing the game
    - It keeps track of the score for both players and the number of draws, and allows players to play multiple rounds until they choose to stop
    - The game board is displayed after each move, and the function checks for a winner or a draw after each turn
    - Players are prompted to enter their moves by specifying the row and column numbers, and input validation ensures that moves are valid
    - After each game, players can choose to play again or exit the game
    """
    score = {"X": 0, "O": 0, "Draw": 0}
    play_again = True
    print("\nGavin Tic-Tac-Toe Game\n")
    while play_again == True:
        board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
        current_player = "X"
        game_over = False
        while game_over == False:
            print_board(board)
            print_score(score)
            print(f"Player {current_player}'s turn\n")
            valid_input = False
            while valid_input == False:
                try:
                    row = int(input("Enter row (0-2): "))
                    col = int(input("Enter column (0-2): "))
                    if row not in range(3) or col not in range(3):
                        print("Must enter values between 0 and 2.")
                    elif board[row][col] != " ":
                        print("That cell is already taken, pick another one")
                    else:
                        valid_input = True
                except ValueError:
                    print("Please enter a number from 0-2")
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins")
                score[current_player] += 1
                print_score(score)
                game_over = True
            elif is_draw(board):
                print_board(board)
                print("It is a draw")
                score["Draw"] += 1
                print_score(score)
                game_over = True
            else:
                if current_player == "X":
                    current_player = "O"
                else:
                    current_player = "X"

        answer = input("Play again? (yes/no): ")
        if answer != "yes":
            play_again = False
# main()

