""" written by John Halloran. Please acknowledge if used """

""" below, there are spaces for you to add comments. You may want to add more comments than this, which is fine """


# draws board for tic-tac-toe

def main():
    boardsize = 4  # define board dimension
    board = defineBoard(boardsize)
    createBoardLabels(board, boardsize)
    drawBoard(board, boardsize)


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


main()  # run the program


