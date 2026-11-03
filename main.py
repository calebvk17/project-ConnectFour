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
 
        print("Invalid option. Please enter 1, 2, or 3.")

def get_args():
    parser = argparse.ArgumentParser(description="Connect Four")
    parser.add_argument("--stats-file", default="leaderboard.csv",
    help="CSV file where the leaderboard is saved")
    return parser.parse_args()

def main():
    args = get_args()
    leaderboard = Leaderboard(args.stats_file)
    leaderboard.load()

    choice = show_menu()
 
    while choice == "2":
        leaderboard.leaderboardGUI()
        choice = show_menu()
 
    if choice == "3":
        leaderboard.save()
        print("\nLeaderboard saved. Goodbye!")
        return
 
    # Added menu to view leaderboard before starting the game - Loaghan
 
    print("\nWelcome to Connect Four!")
    print("\nType 'save' to save your game or 'load' to load a saved game.")

    board = Board()
    move = Move()
    saveLoad = SaveLoad()

    game_over = False

    while game_over == False:

        board.display_board()

        choice = move.get_move()

        if choice == "save":
            saveLoad.save_game(board, move)
            print("\nGame saved!")

        elif choice == "load":
            if saveLoad.load_game(board, move):
                print("\nGame loaded!")

        elif move.is_valid_move(board, choice):
            move.make_move(board, choice)
            symbol = move.players[move.current_player]

            # TODO (Alvin): win/draw detection goes here. After each move, check
            # whether the current player won or the board is full, then set
            # game_over = True and print the result.
            # Also break the loop when game over

        else:
            print("\nThat column is full. Choose another column.")

    leaderboard.save()

if __name__ == '__main__':
    main()