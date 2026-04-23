# Tic-Tac-Toe Game

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
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
    for row in board:
        for spot in row:
            if spot == " ":
                return False
    return True

def main():
    board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    current_player = "X"
    print("\nGavin Tic-Tac-Toe Game")
    game_over = False
    while game_over == False:
        print_board(board)
        print(f"Player {current_player}'s turn")
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
            game_over = True
        elif is_draw(board):
            print_board(board)
            print("It is a draw")
            game_over = True
        else:
            if current_player == "X":
                current_player = "O"    
            else:
                current_player = "X"
#main()

