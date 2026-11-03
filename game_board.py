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

class Board:

    def __init__(self):
        self.rows = 6
        self.cols = 7

        self.board = [[" ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " ", " "]
                ]


    def display_board(self):

        print("\n  1   2   3   4   5   6   7")
        print("+---+---+---+---+---+---+---+")

        for row in self.board:
            line = "|"

            for cell in row:
                line += " " + cell + " |"

            print(line)
            print("+---+---+---+---+---+---+---+")

class Move:

    def __init__(self):
        self.players = ["X", "O"] # Need a way to switch turns
        self.current_player = 0
        self.rows = 6
    
    def get_move(self):
        while True:
            choice = input(f"\nPlayer {self.players[self.current_player]}, choose a column (1-7), or type 'save' or 'load': ").lower()

            if choice == "save":
                return "save"
            elif choice == "load":
                return "load"
            elif choice in "1234567":  # Bug here, entering " " causes error - Loaghan
                return int(choice) - 1
            else:
                print("\nInvalid column. Please choose a number from 1 to 7.")

    def is_valid_move(self, board, column):
        
        return board.board[0][column] == " "

    def make_move(self, board, column):

        for row in range(self.rows - 1, -1, -1):

            if board.board[row][column] == " ":
                board.board[row][column] = self.players[self.current_player]
                return

    def switch_player(self):

        self.current_player = 1 - self.current_player

class SaveLoad:

    def __init__(self):
        self.saved_board = []
        self.saved_player = 0
    
    def save_game(self, board, move):
    
        self.saved_board[:] = [
            board.board[0][:],
            board.board[1][:],
            board.board[2][:],
            board.board[3][:],
            board.board[4][:],
            board.board[5][:]
        ]

        self.saved_player = move.current_player

    def load_game(self, board, move):

        if self.saved_board == []:
            print("\nNo saved game found.")
            return

        board.board = [
            self.saved_board[0][:],
            self.saved_board[1][:],
            self.saved_board[2][:],
            self.saved_board[3][:],
            self.saved_board[4][:],
            self.saved_board[5][:]
        ]

        move.current_player = self.saved_player