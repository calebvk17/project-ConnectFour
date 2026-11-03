"""Entry point for the group project.

`python main.py` must run your project at every milestone, so keep this file working
from Milestone 1 onward. Replace the placeholder below with your own core loop.
"""

from game_board import *
from Leaderboard import *
import argparse

def show_menu():
    print("\n=== Connect Four ===")
    print("1. Play a game")
    print("2. View leaderboard")
    print("3. Quit")
 
    while True:
        choice = input("\nChoose an option (1-3): ")
 
        if choice in ["1", "2", "3"]:
            return choice
 
        print("\nInvalid option. Please enter 1, 2, or 3.")

def get_args():
    parser = argparse.ArgumentParser(description="Connect Four")
    
    parser.add_argument(
        "--stats-file", 
        default="leaderboard.csv",
        help="CSV file where the leaderboard is saved"
    )

    return parser.parse_args()

def main():
    args = get_args()

    leaderboard = Leaderboard(args.stats_file)
    leaderboard.load()
 
    while True:
        choice = show_menu()

        if choice == "1":
            print("\nOpening Connect Four...")

            board = Board()
            move = Move()
            save_load = SaveLoad()

            game = GameGUI(board, move, save_load)
            game.mainloop()

        elif choice == "2":
            leaderboard.leaderboardGUI()
            
        elif choice == "3":
            leaderboard.save()
            print("\nLeaderboard saved. Goodbye!")
            break

if __name__ == '__main__':
    main()