"""Entry point for the group project.

`python main.py` must run your project at every milestone, so keep this file working
from Milestone 1 onward. Replace the placeholder below with your own core loop.
"""

import argparse
import game_board

def main():

    parser = argparse.ArgumentParser(description="Connect Four game")

    parser.add_argument(
        "--load",
        action="store_true",
        help="Load a previously saved game when starting"
    )

    args = parser.parse_args()

    print("\nWelcome to Connect Four!")
    print("\nType 'save' to save your game or 'load' to load a saved game.")
    print("Type 'quit' to exit the game.")

    board = game_board.Board()
    move = game_board.Move()
    saved_load = game_board.SaveLoad()

    if args.load:

        if saved_load.load_game(board, move):
            print("\nSaved game loaded!")
        else:
            print("\nStarting a new game.")

    game_over = False

    while game_over == False:

        board.display_board()

        choice = move.get_move()

        if choice == "save":

            saved_load.save_game(board, move)
            print("\nGame saved!")

        elif choice == "load":

            if saved_load.load_game(board, move):
                print("\nGame loaded!")

        elif choice == "quit":

            print("\nThanks for playing!")
            game_over = True

        elif move.is_valid_move(board, choice):

            move.make_move(board, choice)
            move.switch_player()

        else:

            print("\nThat column is full. Choose another column.")

if __name__ == '__main__':
    main()