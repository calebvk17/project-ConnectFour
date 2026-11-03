"""Entry point for the group project.

`python main.py` must run your project at every milestone, so keep this file working
from Milestone 1 onward. Replace the placeholder below with your own core loop.
"""

# Import the classes needed for the game and leaderboard
from game_board import *
from Leaderboard import *
import argparse

# Displays the main menu and lets the user choose an option
def show_menu():
    print("\n=== Connect Four ===")
    print("1. Play a game")
    print("2. View leaderboard")
    print("3. Quit")

    # Keep asking until the user enters a valid option
    while True:
        choice = input("\nChoose an option (1-3): ")

        # Return the choice if it is valid
        if choice in ["1", "2", "3"]:
            return choice

        # Tell the user if they entered something invalid
        print("\nInvalid option. Please enter 1, 2, or 3.")

# Gets the command-line arguments when the program starts
def get_args():
    parser = argparse.ArgumentParser(description="Connect Four")

    # Lets the user choose which CSV file to save the leaderboard to
    parser.add_argument(
        "--stats-file", 
        default="leaderboard.csv",
        help="CSV file where the leaderboard is saved"
    )

    # Return the arguments entered by the user
    return parser.parse_args()

# Runs the main program
def main():
    # Get the command-line arguments
    args = get_args()

     # Create the leaderboard and load any saved player stats
    leaderboard = Leaderboard(args.stats_file)
    leaderboard.load()

    # Keep showing the menu until the user chooses to quit
    while True:
        choice = show_menu()

        # Start a new game
        if choice == "1":
            print("\nOpening Connect Four...")

            # Create the objects needed to run the game
            board = Board()
            move = Move()
            save_load = SaveLoad()

            # Open the game window
            game = GameGUI(board, move, save_load)
            game.mainloop()

        # Open the leaderboard window
        elif choice == "2":
            leaderboard.leaderboardGUI()

        # Save the leaderboard and close the program
        elif choice == "3":
            leaderboard.save()
            print("\nLeaderboard saved. Goodbye!")
            break

if __name__ == '__main__':
    main()