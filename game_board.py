rows = 6
cols = 7

board = [[" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "]
    ]

saved_board = [
        board[0][:],
        board[1][:],
        board[2][:],
        board[3][:],
        board[4][:],
        board[5][:]
    ]

players = ["X", "O"]
current_player = 0
saved_player = current_player

def display_board():

    print("\n  1   2   3   4   5   6   7")
    print("+---+---+---+---+---+---+---+")

    for row in board:
        line = "|"

        for cell in row:
            line += " " + cell + " |"

        print(line)
        print("+---+---+---+---+---+---+---+")

def get_move():

    while True:
        choice = input(f"\nPlayer {players[current_player]}, choose a column (1-7), or type 'save' or 'load': ").lower()

        if choice == "save":
            return "save"
        elif choice == "load":
            return "load"
        elif choice in "1234567":
            return int(choice) - 1
        else:
            print("\nInvalid column. Please choose a number from 1 to 7.")

def is_valid_move(column):
    
    return board[0][column] == " "

def make_move(column, rows):

    for row in range(rows - 1, -1, -1):

        if board[row][column] == " ":
            board[row][column] = players[current_player]
            return

def switch_player(current_player):

    current_player = 1 - current_player
    return current_player

def save_game(board, current_player):
    
    saved_board[:] = [
        board[0][:],
        board[1][:],
        board[2][:],
        board[3][:],
        board[4][:],
        board[5][:]
    ]

    saved_player = current_player

    return saved_player

def load_game(board, saved_board, saved_player):

    board[:] = [
        saved_board[0][:],
        saved_board[1][:],
        saved_board[2][:],
        saved_board[3][:],
        saved_board[4][:],
        saved_board[5][:]
    ]

    current_player = saved_player

    return current_player

print("\nWelcome to Connect Four!")
print("Type 'save' to save your game or 'load' to load a saved game.")

game_over = False

while game_over == False:

    display_board()

    choice = get_move()

    if choice == "save":
        saved_player = save_game(board, current_player)
        print("\nGame saved!")
    elif choice == "load":
        current_player = load_game(board, saved_board, saved_player)
        print("\nGame loaded!")
    elif is_valid_move(choice):
        make_move(choice, rows)
        current_player = switch_player(current_player)
    else:
        print("\nThat column is full. Choose another column.")