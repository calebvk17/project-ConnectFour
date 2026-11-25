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

        # Stack to keep track of previous moves
        self.move_history = []

    # Check if the player chooses to save, load or place a piece
    def get_move(self):

        # Keep asking until the player enters a valid option
        while True:

            # Get the current player's symbol
            player = self.players[self.current_player]

            # Ask the player to choose a column
            choice = input(f"\nPlayer {player}, choose a column (1-7), or type 'save' or 'load': ").strip().lower()

            # Allow the player to save or load a game
            if choice == "save" or choice == "load":
                return choice

            # Check if the player entered a valid column
            if choice in ["1", "2", "3", "4", "5", "6", "7"]:

                # Convert 1-7 into Python indexes 0-6
                return int(choice) - 1

            print("Invalid input. Enter in a column from 1 to 7.")

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

            # Push the new move onto the stack
            self.move_history.append((row, column, self.current_player))

        return row

    # Checks if the selected column has space for another piece
    def is_valid_move(self, board, column):

        return board.board[0][column] == " "

    # Switches between player X and player O
    def switch_player(self):

        self.current_player = 1 - self.current_player

    # Undoes the most recent move
    def undo_move(self, board):

        if len(self.move_history) > 0:

            # Pop the most recent move off of the stack
            row, column, player = self.move_history.pop()

            # Make that position empty again
            board.board[row][column] = " "

            # Return the turn to the previous player
            self.current_player = player

            return True

        return False

    # Checks if placing a place in a column would create four in a row
    def would_win(self, board, column, symbol):

        row = self.find_open_row(board, column, self.rows - 1)

        if row == None:
            return False

        # Temporarily place the piece
        board.board[row][column] = symbol

        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

        won = False

        for dr, dc in directions:

            count = 1

            # Check both directions from the placed piece
            for direction in [1, -1]:

                r = row + dr * direction
                c = column + dc * direction

                while (0 <= r < board.rows and 0 <= c < board.cols and board.board[r][c] == symbol):

                    count += 1

                    r += dr * direction
                    c += dc * direction

            if count >= 4:
                won = True

        # Remove the temporary piece
        board.board[row][column] = " "

        return won

    # Gives a score to a possible board position
    def evaluate_board(self, board, symbol):

        opponent = self.players[1 - self.current_player]

        score = 0

        # Give the centre column extra points
        for row in range(board.rows):

            if board.board[row][3] == symbol:
                score += 3

        # Check every possible group of four spaces
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]

        for row in range(board.rows):
            for col in range(board.cols):
                for dr, dc in directions:

                    cells = []

                    for i in range(4):

                        r = row + dr * i
                        c = col + dc * i

                        if 0 <= r < board.rows and 0 <= c < board.cols:
                            cells.append(board.board[r][c])

                    if len(cells) == 4:

                        own = 0
                        enemy = 0
                        empty = 0

                        for cell in cells:

                            if cell == symbol:
                                own += 1
                            elif cell == opponent:
                                enemy += 1
                            elif cell == " ":
                                empty += 1

                        # Reward groups that could lead to four in a row
                        if enemy == 0:

                            if own == 3 and empty == 1:
                                score += 100
                            elif own == 2 and empty == 2:
                                score += 10
                            elif own == 1 and empty == 3:
                                score += 1

                        # Check positions where the opponent has three connected pieces
                        if own == 0 and enemy == 3 and empty == 1:
                            score -= 80
        return score
    
    # Finds the best column to recommend to the player
    def get_hint_column(self, board):

        player = self.players[self.current_player]
        opponent = self.players[1 - self.current_player]

        # Find all columns that still have space
        available_columns = []

        for col in range(board.cols):

            if self.is_valid_move(board, col):
                available_columns.append(col)

        if len(available_columns) == 0:
            return None

        # First, check if the player can win immediately
        for col in available_columns:

            if self.would_win(board, col, player):
                return col

        # Check if the opponent can win on their next turn
        opponent_wins = []

        for col in available_columns:

            if self.would_win(board, col, opponent):
                opponent_wins.append(col)

        # Block an immediate opponent win if possible
        if len(opponent_wins) == 1:
            return opponent_wins[0]

        # Check every possible move and give it a score
        best_column = None
        best_score = -1000000

        for col in available_columns:

            row = self.find_open_row(board, col, self.rows - 1)

            # Temporarily place the player's piece
            board.board[row][col] = player

            # Check how many winning moves the opponent would have
            opponent_threats = 0

            for next_col in range(board.cols):
                if self.is_valid_move(board, next_col):
                    if self.would_win(board, next_col, opponent):
                        opponent_threats += 1

            # Evaluate the resulting bvoard
            score = self.evaluate_board(board, player)

            # Discourage moves that allow the opponent to win
            score -= opponent_threats * 1000

            # Prefer the move with the highest score
            if score > best_score:
                best_score = score
                best_column = col

            # Remove trhe temporary piece
            board.board[row][col] = " "

        return best_column

# Handles saving and loading the game using a .json file
class SaveLoad:

    # Saves the current board and player turn to a .json file
    def save_game(self, board, move):

        # Stores the board and current player in a dictionary
        saved_data = {
            "board": board.board,
            "current_player": move.current_player,
            "move_history": move.move_history
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

            # Restore the move history
            move.move_history = []

            # Add each saved move back onto the stack
            for item in saved_data.get("move_history", []):
                move.move_history.append((item[0], item[1], item[2]))

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
        self.resizable(False, False)

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

        tk.Button(
            self,
            text="Save Game",
            command=self.save_game,
            width=12
        ).grid(row=8, column=0, padx=3, pady=15)

        # Button to load a previously saved game
        tk.Button(
            self,
            text="Load Game",
            command=self.load_game,
            width=12
        ).grid(row=8, column=1, columnspan=2, padx=3, pady=15)

        # Button to start a new game
        tk.Button(
            self,
            text="New Game",
            command=self.new_game,
            width=12
        ).grid(row=8, column=3, padx=3, pady=15)

        # Button to close the game window
        tk.Button(
            self,
            text="Quit",
            command=self.destroy,
            width=12
        ).grid(row=8, column=4, columnspan=2, padx=3, pady=15)

        # Button to undo the most recent move
        tk.Button(
            self,
            text="Undo",
            command=self.undo_move,
            width=12
        ).grid(row=8, column=6, padx=3, pady=15)

        # Button to give the player a suggested column
        tk.Button(
            self,
            text="Hint",
            command=self.show_hint,
            width=12
        ).grid(row=9, column=3, padx=3, pady=5)

        # Make all columns equal in size
        for col in range(7):
            self.grid_columnconfigure(col, weight=1)

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

            # Update the GUI so that it shows the new piece
            self.refresh_board()

            # Switch to the other player's turn
            self.move.switch_player()
            player = self.move.players[self.move.current_player]

            # Update the message at the top of the window
            self.status.config(text=f"Player {player}'s turn")
        else:
            # Let the player know that the selected column is full
            self.status.config(text=f"Column {column + 1} is full! Choose another column.")

    # Updates the GUI to match what is currently on the game board
    def refresh_board(self):

        for row in range(self.board.rows):

            for col in range(self.board.cols):

                # Get the value stored in the current board cell
                value = self.board.board[row][col]

                # Give player X's pieces the colour red
                if value == "X":
                    text_color = "red"
                # Give player O's pieces the colour blue
                elif value == "O":
                    text_color = "blue"
                else:
                    text_color = "black"

                # Update the cell with the correct piece and colour
                self.cell_labels[row][col].config(
                    text=value,
                    fg=text_color
                )

        # Enable the column buttons again
        for button in self.column_buttons:

            button.config(state="normal")

        # Keep the buttons disabled if the game is over
        if self.game_over == True:

            for button in self.column_buttons:
                button.config(state="disabled")

    # Saves the current game when the save button is clicked
    def save_game(self):

        self.saved_load.save_game(self.board, self.move)

        # Show a message to confirm that the game was saved
        self.status.config(text="Game saved!")

    # Loads the last saved game when the load button is clicked
    def load_game(self):

        # Check if a saved game was successfully loaded
        if self.saved_load.load_game(self.board, self.move):
            # Update the board to show the loaded game
            self.refresh_board()

            # Get the player whose turn it is after loading
            player = self.move.players[self.move.current_player]

            # Show that the game was loaded and whose turn it is
            self.status.config(text=f"Game loaded! Player {player}'s turn.")
        else:
            # Show a message if there is no saved game to load
            self.status.config(text="No saved game found.")

    # Resets everything to start a fresh new game
    def new_game(self):

        self.board.reset()
        self.move.current_player = 0
        self.move.move_history = []
        self.game_over = False

        # Refresh the board so all the pieces disappear
        self.refresh_board()

        # Set the turn back to player X
        self.status.config(text="New game! Player X's turn.")

    # Undoes the most recent move
    def undo_move(self):

        if self.move.undo_move(self.board):
            # Update the board to remove the undone piece
            self.refresh_board()

            # Update whose turn it is
            player = self.move.players[self.move.current_player]
            self.status.config(text=f"Player {player}'s turn")
        else:
            self.status.config(text="There are no moves to undo.")

    # Shows the player which column is recommended
    def show_hint(self):

        column = self.move.get_hint_column(self.board)

        if column != None:
            self.status.config(text=f"Suggested move: Column {column + 1}!")
        else:
            self.status.config(text="No available moves!")