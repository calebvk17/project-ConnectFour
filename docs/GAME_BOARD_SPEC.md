# Game Board, Player/Move System, and Save/Load

## What It Does

This feature will manage the Connect Four board, player turns, and moves. It will check whether moves are valid, it will place player pieces on the board, keep track of the game state, and it will allow the game state to be saved and loaded.

## Data Needed

- A 2D list for the 6x7 game board.
- Player names or numbers.
- Current player.
- Selected column.
- Player piece (`X` or `O`).
- Saved game state.

## Steps

1. Create an empty 6x7 board.
2. Display the board in the terminal.
3. Ask the current player for a column.
4. Check if the move is valid.
5. Place the piece in the lowest available space.
6. Update the game state.
7. Switch to the other player.
8. Allow the current game state to be saved.
9. Allow a previously saved game to be loaded.
10. Continue until the game ends.

## Functions

- `display_board()` - Displays the current board.
- `get_move()` - Gets the player's move.
- `is_valid_move()` - Checks if a move is valid.
- `make_move()` - Places a piece in the lowest available space.
- `switch_player()` - Changes the current player.
- `save_game()` - Saves the current game state.
- `load_game()` - Loads a previously saved game state.

Breaking the feature into smaller functions will make it easier for me to build and test.