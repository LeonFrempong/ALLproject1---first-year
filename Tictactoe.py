""" written by John Halloran. Please acknowledge if used """

""" below, there are spaces for you to add comments. You may want to add more comments than this, which is fine """


# draws board for tic-tac-toe

def main():
    boardsize = 3  # define board dimension
    board = defineBoard(boardsize)
    createBoardLabels(board, boardsize)
    drawBoard(board, boardsize)

    check_win_all(board)


def defineBoard(boardsize):
    board = [[""] * boardsize for i in range(boardsize)]  # make the basic (non-drawable) version of theboard
    return board


def inputBoardSize():  # this is so we can make a board of any dimension we like
    boardsize = input('enter board dimension: ')  # not used in this version, but if it was, how?
    return int(boardsize)


def createBoardLabels(board, boardsize):  #
    counter = 0
    for i in range(boardsize):
        for j in range(boardsize):
            counter += 1
            board[i][j] = counter
    return (board)


def print_divider(boardsize):  # this part shows that the user can enter x in the game

    print ('|'.join(['____' for x in range(boardsize)]))


def print_blank(boardsize):
    print ('|'.join(['    ' for x in range(boardsize)]))  # it allows the data in the print function to be printed
                                                        #on the screen.


def print_labels(counter, board, boardsize):  # this sections loops out the board
    row = ' | '.join(['%2s' % board[counter][x] for x in range(boardsize)])
    row = ' ' + row
    print(row)


def drawBoard(board, boardsize):  # <your comment>
    for i in range(boardsize):
        print_blank(boardsize)
        print_labels(i, board, boardsize)
        if (i == boardsize - 1):
            print_blank(boardsize)
        else:
            print_divider(boardsize)
            
#board = [["1", "x", "3"],
        #["x", "5", "x"],
        #["7", "x", "9"]]

def check_win_left_vertical (board):
    win = 'true'
    j = 0
    for i in range (2):
        if board[i][j] != board[i+1][j]:
            win = 'false'
            
    return (win)
    
def check_win_mid_vertical(board):
    win = "true"
    j = 1
    for i in range (2):
        if board[i][j] != board[i+1][j]:
            win = "false"
            #print ("win is {}".format(win))
    
    return (win)
        
def check_win_right_vertical(board):
    win = "true"
    j = 2
    for i in range (2):
        if board[i][j] != board[i+1][j]:
            win = "false"
            #print ("win is {}".format(win))
    
    return (win)

def check_win_top_hoz(board):
    win = "true"
    i = 0
    for j in range (2):
        if board[i][j] != board[i][j+1]:
            win = "false"

    return (win)

def check_win_mid_hoz(board):
    win = "true"
    i = 1
    for j in range (2):
        if board[i][j] != board[i][j+1]:
            win = "false"

    return (win)

def check_win_bottom_hoz(board):
    win = "true"
    i = 2
    for j in range (2):
        if board[i][j] != board[i][j+1]:
            win = "false"

    return (win)

def check_win_first_diag(board):
    win = "true"
    j = 0
    for i in range(2):
        if board [i][j] != board[i+1][j+1]:
            win = "false"
        j = j+1
    return (win)

def check_win_second_diag(board):
    win ="true"
    j = 2
    for i in range (2):
        if (board[i][j] != board[i+1][j-1]):
            win = "false"
        j = j-1
    return(win)

def check_win_all(board):

    check_win_left_vertical(board)
    check_win_mid_vertical(board)
    check_win_right_vertical(board)
    check_win_top_hoz(board)
    check_win_mid_hoz(board)
    check_win_bottom_hoz(board)
    check_win_first_diag(board)
    check_win_second_diag(board)

main()  # run the program


