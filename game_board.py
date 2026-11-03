import json
import tkinter as tk

class Board:

    def __init__(self):
        self.rows = 6
        self.cols = 7

        self.board = [
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "]
        ]

    def reset(self):

        self.board = [
            [" ", " ", " ", " ", " ", " ", " "],
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

        # Keep asking until the player enters a valid option
        while True:

            # Get the current player's symbol
            player = self.players[self.current_player]

            # Ask the player to choose a column
            choice = input(
                f"\nPlayer {player}, choose a column (1-7), or type 'save' or 'load': "
            ).strip().lower()

            # Allow the player to save or load a game
            if choice == "save" or choice == "load":
                return choice

            # Check if the player entered a valid column
            if choice in ["1", "2", "3", "4", "5", "6", "7"]:

                # Convert 1-7 into Python indexes 0-6
                return int(choice) - 1

            print("Invalid input. Enter a column from 1 to 7.")


    def find_open_row(self, board, column, row):

        if row < 0:
            return None

        if board.board[row][column] == " ":
            return row

        return self.find_open_row(board, column, row - 1)

    def make_move(self, board, column):

        row = self.find_open_row(board, column, self.rows - 1)

        if row != None:
            board.board[row][column] = self.players[self.current_player]

        return row

    def is_valid_move(self, board, column):

        return board.board[0][column] == " "

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
            return False


class GameGUI(tk.Tk):

    def __init__(self, board, move, saved_load, load_on_start=False):

        super().__init__()

        self.board = board
        self.move = move
        self.saved_load = saved_load
        self.game_over = False

        self.title("Connect Four")

        self.status = tk.Label(
            self,
            text="Player X's turn",
            font=("Arial", 18, "bold")
        )

        self.status.grid(row=0, column=0, columnspan=7, pady=15)

        self.column_buttons = []

        for col in range(self.board.cols):

            button = tk.Button(
                self,
                text=f"Column {col + 1}",
                font=("Arial", 10),
                command=lambda c=col: self.play_move(c)
            )

            button.grid(row=1, column=col, padx=3, pady=5)

            self.column_buttons.append(button)

        self.cell_labels = []

        for row in range(self.board.rows):

            label_row = []

            for col in range(self.board.cols):

                cell = tk.Label(
                    self,
                    text=" ",
                    font=("Arial", 22, "bold"),
                    width=4,
                    height=2,
                    bg="white",
                    relief="solid"
                )

                cell.grid(
                    row=row + 2,
                    column=col,
                    padx=3,
                    pady=3
                )

                label_row.append(cell)

            self.cell_labels.append(label_row)

        tk.Button(
            self,
            text="Save Game",
            command=self.save_game,
            width=12
        ).grid(row=8, column=0, columnspan=2, pady=15)

        tk.Button(
            self,
            text="Load Game",
            command=self.load_game,
            width=12
        ).grid(row=8, column=2, columnspan=2, pady=15)

        tk.Button(
            self,
            text="New Game",
            command=self.new_game,
            width=12
        ).grid(row=8, column=4, pady=15)

        tk.Button(
            self,
            text="Quit",
            command=self.destroy,
            width=12
        ).grid(row=8, column=5, columnspan=2, pady=15)

        self.refresh_board()

        if load_on_start:
            self.load_game()

    def play_move(self, column):

        if self.game_over == True:
            return

        if self.move.is_valid_move(self.board, column):

            self.move.make_move(self.board, column)

            self.refresh_board()

            if self.check_board_full():

                self.game_over = True

                self.status.config(
                    text="The board is full! Game over!"
                )

                for button in self.column_buttons:
                    button.config(state="disabled")

            else:

                self.move.switch_player()

                player = self.move.players[self.move.current_player]

                self.status.config(text=f"Player {player}'s turn")

        else:

            self.status.config(
                text=f"Column {column + 1} is full! Choose another column."
            )

    def check_board_full(self):

        for col in range(self.board.cols):

            if self.board.board[0][col] == " ":
                return False

        return True

    def refresh_board(self):

        for row in range(self.board.rows):

            for col in range(self.board.cols):

                value = self.board.board[row][col]

                if value == "X":
                    text_color = "red"

                elif value == "O":
                    text_color = "blue"

                else:
                    text_color = "black"

                self.cell_labels[row][col].config(
                    text=value,
                    fg=text_color
                )

        for button in self.column_buttons:

            button.config(state="normal")

        if self.game_over == True:

            for button in self.column_buttons:
                button.config(state="disabled")

    def save_game(self):

        self.saved_load.save_game(self.board, self.move)

        self.status.config(text="Game saved!")

    def load_game(self):

        if self.saved_load.load_game(self.board, self.move):

            self.game_over = self.check_board_full()

            self.refresh_board()

            if self.game_over == True:

                self.status.config(text="The board is full! Game over!")

            else:

                player = self.move.players[self.move.current_player]

                self.status.config(
                    text=f"Game loaded! Player {player}'s turn."
                )

        else:

            self.status.config(text="No saved game found.")

    def new_game(self):

        self.board.reset()
        self.move.current_player = 0
        self.game_over = False

        self.refresh_board()

        self.status.config(text="New game! Player X's turn.")