"""Entry point for the Connect Four project."""

# Import the classes needed for the game and leaderboard
from game_board import *
from Leaderboard import *
from win_check import WinChecker
import argparse

# Displays the main menu and lets the user choose an option
def show_menu():
    print("\n=== Connect Four ===")
    print("1. Play a game (GUI)")
    print("2. Play a game (Terminal)")
    print("3. View leaderboard")
    print("4. Quit")

    # Keep asking until the user enters a valid option
    while True:
        choice = input("\nChoose an option (1-4): ")

        # Return the choice if it is valid
        if choice in ["1", "2", "3", "4"]:
            return choice

        # Tell the user if they entered something invalid
        print("\nInvalid option. Please enter 1, 2, 3, or 4.")

# Gets the command-line arguments when the program starts
def get_args():
    parser = argparse.ArgumentParser(description="Connect Four")

    # Lets the user choose which CSV file to save the leaderboard to
    parser.add_argument(
        "--stats-file",
        default="leaderboard.csv",
        help="CSV file where the leaderboard is saved"
    )
    parser.add_argument(
        "--load",
        action="store_true",
        help="Load a previously saved game when starting"
    )

    # Return the arguments entered by the user
    return parser.parse_args()

# Runs the terminal game using WinChecker
def play_terminal_game():
    # Create the board, move handler, and save/load handler
    board = Board()
    move = Move()
    saveLoad = SaveLoad()

    # Create the win checker using the current board
    checker = WinChecker(board.board)

    game_over = False

    print("\nWelcome to Connect Four!")
    print("Type 'save' to save or 'load' to load a game.")

    while game_over == False:
        board.display_board()

        # Get the player's column choice
        choice = move.get_move()

        if choice == "save":
            saveLoad.save_game(board, move)
            print("\nGame saved!")

        elif choice == "load":
            if saveLoad.load_game(board, move):
                checker.board = board.board
                print("\nGame loaded!")
            else:
                print("\nNo saved game found.")

        elif move.is_valid_move(board, choice):
            # Place the current player's piece
            move.make_move(board, choice)

            player = move.players[move.current_player]

            # Check for a win before checking for a draw
            if checker.check_win(player):
                board.display_board()
                print(f"\nPlayer {player} wins!")

                # Update the saved player statistics
                checker.update_stats(player)
                game_over = True

            elif checker.check_draw():
                board.display_board()
                print("\nIt's a draw!")

                # Update the saved draw statistics
                checker.update_stats("draws")
                game_over = True

            else:
                # Switch players if the game is not over
                move.switch_player()

        else:
            print("\nThat column is full. Choose another column.")

# Runs the main program
def main():
    # Get the command-line arguments
    args = get_args()
    # Create the leaderboard and load any saved player stats
    leaderboard = Leaderboard(args.stats_file)
    leaderboard.load()

    # Create the game objects
    board = Board()
    move = Move()
    save_load = SaveLoad()

    # Check whether the user wants to load a saved game
    loaded_game = False

    if args.load:

        if save_load.load_game(board, move):
            print("\nSaved game loaded!")
            loaded_game = True

        else:
            print("\nNo saved game found. Starting a new game.")

    # Keep showing the menu until the user chooses to quit
    while True:

        choice = show_menu()

        # Start a new game unless a saved game was loaded
        if choice == "1" or choice == "2":

            if loaded_game == False:

                board = Board()
                move = Move()
                save_load = SaveLoad()

            # The loaded game has now been used
            loaded_game = False

        # Option 1: Start Caleb's GUI
        if choice == "1":
            
            print("\nOpening Connect Four...")

            # Open the game window
            game = GameGUI(board, move, save_load)
            game.mainloop()

        # Option 2: Play using terminal and WinChecker
        elif choice == "2":

            play_terminal_game()

        # Option 3: Open the leaderboard window
        elif choice == "3":

            leaderboard.leaderboardGUI()

        # Option 4: Save the leaderboard and quit
        elif choice == "4":

            leaderboard.save()

            print("\nLeaderboard saved. Goodbye!")
            break

if __name__ == "__main__":
    main()