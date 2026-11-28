import random

def display_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board, player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False


def ai_move(board):
    
    for i in range(9):
        if board[i] not in ["X", "O"]:
            board[i] = "O"
            if check_winner(board, "O"):
                return
            board[i] = str(i + 1)

    
    for i in range(9):
        if board[i] not in ["X", "O"]:
            board[i] = "X"
            if check_winner(board, "X"):
                board[i] = "O"
                return
            board[i] = str(i + 1)

    
    if board[4] == "5":
        board[4] = "O"
        return

    corners = [0, 2, 6, 8]
    available_corners = [i for i in corners if board[i] not in ["X", "O"]]

    if available_corners:
        board[random.choice(available_corners)] = "O"
        return

    
    available = [i for i in range(9) if board[i] not in ["X", "O"]]

    if available:
        board[random.choice(available)] = "O"


def tic_tac_toe():
    board = ["1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]

    print("TIC-TAC-TOE")
    print("You are X. Computer is O.")

    for turn in range(9):
        display_board(board)

    
        while True:
            try:
                position = int(input("Enter your position (1-9): "))

                if position < 1 or position > 9:
                    print("Enter a number between 1 and 9.")
                elif board[position - 1] in ["X", "O"]:
                    print("That position is already occupied.")
                else:
                    break

            except ValueError:
                print("Please enter a valid number.")

        board[position - 1] = "X"

        if check_winner(board, "X"):
            display_board(board)
            print("You win!")
            return

        if turn == 8:
            break

        print("\nComputer is thinking...")
        ai_move(board)

        if check_winner(board, "O"):
            display_board(board)
            print("Computer wins!")
            return

    display_board(board)
    print("It's a draw!")



tic_tac_toe()