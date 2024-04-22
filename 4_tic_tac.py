import random as rm

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board , player):
    for row in board:
        if row.count(player) == 3:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

def is_board_full(board):
    for row in board:
        for i in row:
            if i == " ":
                return False
    return True

def player_move(board):
    while True:
        try:
            row = int(input("Enter row (1, 2, 3): ")) 
            col = int(input("Enter column (1, 2, 3): "))
            if (0 <= row <= 2) and (0 <= col <= 2) and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move, please try again.")
        except ValueError:
            print("Invalid input, please enter a number.")

def computer_move(board):
    while True:
        row = rm.randint(0, 2)
        col = rm.randint(0, 2)
        if board[row][col] == " ":
            return row, col

def main():
    board = [[" " for i in range(3)] for i in range(3)]
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    while True:
        row, col = player_move(board)
        board[row][col] = "X"
        print_board(board)
        if check_winner(board,"X"):
            print("You won!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break
        
        print("Computer's Turn:")
        row, col = computer_move(board)
        board[row][col] = "O"
        print_board(board)

        if check_winner(board, "O"):
            print("Computer wins")
            break
        if is_board_full(board):
            print("Match Draw")
            break

if __name__ == "__main__":
    main()
