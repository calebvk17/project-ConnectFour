rows = 6
cols = 7

board = [[" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "]
    ]

players = ["X", "O"]
current_player = 0

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
        column = int(input(f"\nPlayer {players[current_player]}, choose a column (1-7): "))

        column -= 1

        if 0 <= column < cols:
            return column

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

def check_win(rows, cols):

    piece = players[current_player]

    for row in range(rows):
        for column in range(cols - 3):
            if board[row][column] == piece and board[row][column + 1] == piece and board[row][column + 2] == piece and board [row][column + 3] == piece:
                return True

    for row in range(rows - 3):
        for column in range(cols):
            if board[row][column] == piece and board[row + 1][column] == piece and board[row + 2][column] == piece and board [row + 3][column] == piece:
                return True

    for row in range(rows - 3):
        for column in range(cols - 3):
            if board[row][column] == piece and board[row + 1][column + 1] == piece and board[row + 2][column + 2] == piece and board [row + 3][column + 3] == piece:
                return True

    for row in range(3, rows):
        for column in range(cols - 3):
            if board[row][column] == piece and board[row - 1][column + 1] == piece and board[row - 2][column + 2] == piece and board [row - 3][column + 3] == piece:
                return True

    return False

def check_draw():

    for column in range(cols):

        if board[0][column] == " ":
            return False
    
    return True

print("\nWelcome to Connect Four!")

game_over = False

while game_over == False:

    display_board()

    column = get_move()

    if is_valid_move(column):
        make_move(column, rows)

        if check_win(rows, cols):
            display_board()
            print(f"\nPlayer {players[current_player]} wins!")
            game_over = True

        elif check_draw():
            display_board()
            print("\nThe game is a draw!")
            game_over = True

        else:
            current_player = switch_player(current_player)

    else:
        print("\nThat column is full. Choose another column.")