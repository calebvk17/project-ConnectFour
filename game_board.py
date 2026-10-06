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

print("\nWelcome to Connect Four!")

game_over = False

while game_over == False:

    display_board()

    column = get_move()

    if is_valid_move(column):
        make_move(column, rows)
        current_player = switch_player(current_player)
    else:
        print("\nThat column is full. Choose another column.")