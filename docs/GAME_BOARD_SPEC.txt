# Game Board and Player/Move System

## What It Does

This feature will manage the Connect Four board, player turns, and moves. It will also check if the moves are valid and it will keep track of the game state.

## Data Needed

- A 2D list for the 6x7 game board.
- Player names or numbers.
- Current player.
- Selected column.
- Player piece (`X` or `O`).

## Steps

1. Create an empty 6x7 board.
2. Display the board in the terminal.
3. Ask the player for a column.
4. Check if the move is valid.
5. Place the piece in the lowest available space.
6. Switch to the other player.
7. Check for a win or draw.
8. Continue until the game ends.

## Functions

- `display_board()` - Displays the board.
- `get_move()` - Gets the player's move.
- `is_valid_move()` - Checks if a move is valid.
- `make_move()` - Places a piece.
- `switch_player()` - Changes turns.
- `check_win()` - Checks for a win.
- `check_draw()` - Checks for a draw.

Breaking the feature into smaller functions will make it easier to build and test.