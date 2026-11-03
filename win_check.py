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







