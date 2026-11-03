import json
import tkinter as tk

# Handles the game board
class Board:

    def __init__(self):
        # Set the number of rows and columns on the board
        self.rows = 6
        self.cols = 7

        # Create an empty 6 by 7 game board
        self.board = [
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "]
        ]
    
    # Clears the board and makes every spot empty again
    def reset(self):

        self.board = [
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "]
        ]

# Handles player turns and placing pieces on the board
class Move:

    def __init__(self):
        # X and O are the two players
        self.players = ["X", "O"]
        self.current_player = 0
        self.rows = 6

    # Recursively looks for an empty spot in the selected column
    def find_open_row(self, board, column, row):

        # Stop searching if there are no more rows left
        if row < 0:
            return None

        # Return the row if the spot is empty
        if board.board[row][column] == " ":
            return row

        # Check the row above until an empty spot is found
        return self.find_open_row(board, column, row - 1)

    # Places the current player's piece in the selected column
    def make_move(self, board, column):

        # Find the lowest empty spot in the column
        row = self.find_open_row(board, column, self.rows - 1)

        # Place the player's piece if an empty spot was found
        if row != None:
            board.board[row][column] = self.players[self.current_player]

        return row

    # Checks if the selected column has space for another piece
    def is_valid_move(self, board, column):

        return board.board[0][column] == " "

    # Switches between player X and player O
    def switch_player(self):

        self.current_player = 1 - self.current_player

# Handles saving and loading the game using a .json file
class SaveLoad:

    # Saves the current board and player turn to a file
    def save_game(self, board, move):

        # Stores the board and current player in a dictionary
        saved_data = {
            "board": board.board,
            "current_player": move.current_player
        }

        # Write the saved game data to the .json file
        with open("savegame.json", "w") as file:
            json.dump(saved_data, file)

    # Loads the previously saved game from the .json file
    def load_game(self, board, move):

        try:
            # Open the file and read the saved game data
            with open("savegame.json") as file:
                saved_data = json.load(file)
            # Restore the board and whose turn it is
            board.board = saved_data["board"]
            move.current_player = saved_data["current_player"]

            return True
        
        # Return False if there is no saved game file
        except FileNotFoundError:
            return False

# Creates the Connect Four game window using Tkinter
class GameGUI(tk.Tk):

    def __init__(self, board, move, saved_load, load_on_start=False):

        super().__init__()

        # Store the game objects so that they can be used throughout the class
        self.board = board
        self.move = move
        self.saved_load = saved_load
        self.game_over = False

        # Set the title of the game window
        self.title("Connect Four")

        # Display whose turn it is at the top of the window
        self.status = tk.Label(
            self,
            text="Player X's turn",
            font=("Arial", 18, "bold")
        )

        self.status.grid(row=0, column=0, columnspan=7, pady=15)

        # Create a button for each column so players can drop their pieces
        self.column_buttons = []

        for col in range(self.board.cols):

            button = tk.Button(
                self,
                text=f"Column {col + 1}",
                font=("Arial", 10),
                command=lambda c=col: self.play_move(c)
            )

            button.grid(row=1, column=col, padx=3, pady=5)

            # Keep track of all the column buttons
            self.column_buttons.append(button)

        # Create the labels that display the pieces on the game board
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

                # Position each cell in the correct row and column
                cell.grid(
                    row=row + 2,
                    column=col,
                    padx=3,
                    pady=3
                )

                label_row.append(cell)

            self.cell_labels.append(label_row)

        # Button to save the current game
        tk.Button(
            self,
            text="Save Game",
            command=self.save_game,
            width=12
        ).grid(row=8, column=0, columnspan=2, pady=15)

        # Button to load a previously saved game
        tk.Button(
            self,
            text="Load Game",
            command=self.load_game,
            width=12
        ).grid(row=8, column=2, columnspan=2, pady=15)

        # Button to start a new game
        tk.Button(
            self,
            text="New Game",
            command=self.new_game,
            width=12
        ).grid(row=8, column=4, pady=15)

        # Button to close the game window
        tk.Button(
            self,
            text="Quit",
            command=self.destroy,
            width=12
        ).grid(row=8, column=5, columnspan=2, pady=15)

        # Update the board so it displays the current game state
        self.refresh_board()

        # Load a saved game automatically if this option is enabled
        if load_on_start:
            self.load_game()

    # Handles a player clicking one of the column buttons
    def play_move(self, column):

        # Do not allow any more moves if the game is over
        if self.game_over == True:
            return

        # Check if the selected column has an empty spot
        if self.move.is_valid_move(self.board, column):

            # Place the current player's piece on the board
            self.move.make_move(self.board, column)

            # Update the GUI to show the new piece
            self.refresh_board()

            # Check if the board is completely full
            if self.check_board_full():

                self.game_over = True

                # Display a message when the board is full
                self.status.config(
                    text="The board is full! Game over!"
                )

                # Disable the column buttons because the game is over
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