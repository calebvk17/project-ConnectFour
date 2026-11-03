import json
import argparse

def check_horizontal(board, piece):
    #Get the number of rows and columns in the board
    rows = len(board)
    cols= len(board[0]) # Counts elements in first row to get number of columns

    #Go through each row in the board
    for row in range(rows):

        #Go through each column in the row, stopping 3 columns before the end
        for column in range(cols -3):

            #Check if the 4 spaces beside each other contain the same X or O piece
            if (board[row][column] == piece and
                board[row][column + 1] == piece and
                board[row][column + 2] == piece and
                board[row][column + 3] == piece):
                return True # Return true if a horizontal win is found
    return False # else return false

def check_vertical(board, piece):
    
    rows = len(board)
    cols= len(board[0])

    
    for column in range(cols):

        #Go through each row in the column, stopping 3 rows before the end
        for row in range(rows - 3):

            #Check if the 4 spaces above each other contain the same X or O piece
            if (board[row][column] == piece and
                board[row + 1][column] == piece and
                board[row + 2][column] == piece and
                board[row + 3][column] == piece):
                return True # Return true if a vertical win is found
    return False # else return false

def check_diagonal(board, piece):
    rows = len(board)
    cols = len(board[0])

    #Check for diagonal wins from top left to bottom right
    for row in range(rows -3):
        for column in range(cols -3):

            if (board[row][column] == piece and
                board[row + 1][column +1] == piece and
                board[row + 2][column + 2] == piece and
                board[row + 3][column + 3] == piece):
                return True 
            

    #Check for diagonal wins from bottom left to top right
    for row in range(3, rows): # start at 3 and start checking upwards
        for column in range(cols -3):

            if (board[row][column] == piece and 
                board[row -1][column + 1] == piece and
                board[row -2][column + 2] == piece and
                board[row -3][column + 3] == piece):
                return True
    return False

def check_win(board, piece):

    #Check horizontal win
    if check_horizontal(board, piece):
        return True

    #Check vertical win
    if check_vertical(board, piece):
        return True

    #Check diagonal win
    if check_diagonal(board, piece):
        return True

    return False

def check_draw(board):

    cols = len(board[0])

    for column in range (cols):
        if board[0][column] == " ":
            return False # If there is an empty space in the top row, the game is not a draw

    return True # the board is full




class WinChecker:

    def __init__(self, board, win_length = 4):
        self.board = board
        self.winner = None  # No winner when the checker is created
        self.win_length = win_length 

    # Check for a win and remember who won
    
    def check_win(self, piece):

        # Use our recursive method to check for a win
        if self.check_win_recursive(piece):
            self.winner = piece
            return True

        return False

    # Check whether the board is full
    def check_draw(self):
        return check_draw(self.board)

    #Count matching pieces using recursion
    def count_pieces(self, row, column, row_step, col_step, piece):

        #Check if current pos is out of bounds (row)
        if row < 0 or row >= len(self.board):
            return 0

        #Check if current pos is out of bounds (column)
        if column < 0 or column >= len(self.board[0]):
            return 0

        #Check if the current position contains the piece we are counting
        if self.board[row][column] != piece:
            return 0

        
        # Count the current piece, then check the next position
        return 1 + self.count_pieces(
            row + row_step,       # Move up/down or stay in the same row
            column + col_step,    # Move left/right or stay in the same column
            row_step,             # Keep the same row direction
            col_step,             # Keep the same column direction
            piece                 # Keep checking for the same X or O
        )

   
    # Check if a player has 4 consecutive pieces using recursion
    def check_win_recursive(self, piece):

        # Get the number of rows and columns on the board
        rows = len(self.board)
        cols = len(self.board[0])

        # Each pair tells us how to move (row_step, col_step)
        # Right, down, down-right, up-right
        directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]

        # Loop through every row and column on the board
        for row in range(rows):
            for column in range(cols):

                # Only start checking if this position has our player's piece
                if self.board[row][column] == piece:

                    # Check all 4 directions starting from this position
                    for row_step, col_step in directions:

                        # Recursively count matching pieces in this direction
                        count = self.count_pieces(
                            row,         # Starting row
                            column,      # Starting column
                            row_step,    # How much to move up or down
                            col_step,    # How much to move left or right
                            piece        # The X or O we are looking for
                        )

                        # If we found 4 or more in a row, the player wins
                        if count >= self.win_length:
                            return True

        # No 4 consecutive pieces were found anywhere
        return False

    
    # Save game statistics to a JSON file
    def save_stats(self, stats, filename="game_stats.json"):

        # Open the file for writing
        with open(filename, "w") as file:
            json.dump(stats, file, indent=4)

        
    # Load saved statistics from the JSON file
    def load_stats(self, filename="game_stats.json"):

        try:
            # Try opening and reading the saved file
            with open(filename, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            # If the file doesn't exist, start with zero statistics
            return {"X": 0, "O": 0, "draws": 0}

    
    # Update and save statistics after a game ends
    def update_stats(self, result):
        stats = self.load_stats()

        # Increase the count for the winner or a draw
        if result in stats: #Check if the result is a valid key in the stats 
            stats[result] += 1

        # Save the updated statistics
        self.save_stats(stats)

    #Display saved game stats in the terminal
    def display_stats(self): 

        #Load the saved statistics from the JSON file
        stats = self.load_stats()

        print("\n===== CONNECT FOUR STATISTICS =====")
        print("Player X wins:", stats["X"])
        print("Player O wins:", stats["O"])
        print("Draws:", stats["draws"])
        print("===================================")


# Run this code only when win_check.py is executed directly
if __name__ == "__main__":

    # Create a parser to read commands entered in the terminal
    parser = argparse.ArgumentParser(
        description="Connect Four Win Checker"
    )

    # Create a terminal option called --win-length
    parser.add_argument(
        "--win-length",          
        type=int,                
        default=4,               
        choices=range(3, 8),     
        metavar="{3,4,5,6,7}",   
        help="Number of consecutive pieces needed to win (3-7)"
    )

    # Read the user's terminal arguments and store them in args
    args = parser.parse_args()

    # Create an empty Connect Four board with 6 rows and 7 columns
    board = [[" " for column in range(7)] for row in range(6)]

    # Create a WinChecker using the winning length chosen by the user
    checker = WinChecker(board, args.win_length)
    checker.display_stats()
    # Display the selected winning length in the terminal
    print("Win length:", checker.win_length)




       

        












