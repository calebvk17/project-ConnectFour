"""Entry point for the group project.

`python main.py` must run your project at every milestone, so keep this file working
from Milestone 1 onward. Replace the placeholder below with your own core loop.
"""

import game_board

def main():

    print("\nWelcome to Connect Four!")
    print("\nType 'save' to save your game or 'load' to load a saved game.")

    game_over = False

    while game_over == False:

        game_board.display_board()

        choice = game_board.get_move()

        if choice == "save":
            game_board.saved_player = game_board.save_game(game_board.board, game_board.current_player)
            print("\nGame saved!")
        elif choice == "load":
            game_board.current_player = game_board.load_game(game_board.board, game_board.saved_board, game_board.saved_player)
            print("\nGame loaded!")
        elif game_board.is_valid_move(choice):
            game_board.make_move(choice, game_board.rows)
            game_board.current_player = game_board.switch_player(game_board.current_player)
        else:
            print("\nThat column is full. Choose another column.")

if __name__ == '__main__':
    main()