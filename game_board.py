import json

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
        self.players = ["X", "O"]
        self.current_player = 0
        self.rows = 6
    
    def get_move(self):

        while True:
            choice = input(f"\nPlayer {self.players[self.current_player]}, choose a column (1-7), or type 'save', 'load', or 'quit': ").strip().lower()

            if choice == "save":
                return "save"
            elif choice == "load":
                return "load"
            elif choice == "quit":
                return "quit"
            elif choice in ["1", "2", "3", "4", "5", "6", "7"]:
                return int(choice) - 1
            else:
                print("\nInvalid column. Please choose a number from 1 to 7.")

    def is_valid_move(self, board, column):
        
        return board.board[0][column] == " "

    def find_open_row(self, board, column, row):

        if row < 0:
            return

        if board.board[row][column] == " ":
            return row

        return self.find_open_row(board, column, row - 1)

    def make_move(self, board, column):

        row = self.find_open_row(board, column, self.rows - 1)

        if row != None:
            board.board[row][column] = self.players[self.current_player]

        return row

    def switch_player(self):

        self.current_player = 1 - self.current_player

class SaveLoad:
    
    def save_game(self, board, move):

        saved_data = {
            "board": board.board,
            "current_player": move.current_player
        }

        with open("savegame.json", "w") as file:
            json.dump(saved_data, file)

    def load_game(self, board, move):

        try:
            with open("savegame.json") as file:
                saved_data = json.load(file)

            board.board = saved_data["board"]
            move.current_player = saved_data["current_player"]

            return True

        except FileNotFoundError:
            print("\nNo saved game found.")
            return False