# Win and Draw Detection

## What it Does

This feature will check the Connect Four board to determine if a player has won or the game has ended in a draw.

## Data Needed

- The 2D list containing the 6x7 game board.
- Player pieces 'X' or 'O'
- Row and column positions.
- The current player

## Steps

1. Check the board after a player has places a piece.
2. Check for four matching pieces horizontally
3. Check for four matching pieces diagonally
4. Check for four matching pieces vertically
5. If four matching pieces are found, declare the current player the winner.
6. If the board is full and there is no winner, declare the game a draw.
7. Otherwise continue the game

## Functions

- 'check_horizontal()' - Checks for four matching pieces horizontally.
- 'check_diagonal()' - Checks for four matching pieces diagonally.
- 'check_vertical()' - Checks for four matching pieces vertically.
- 'check_win()' - Checks if the current player has won.
- 'check-draw()' - Checks if the board is full without a winner.
