""" written by John Halloran. Please acknowledge if used """

""" below, there are spaces for you to add comments. You may want to add more comments than this, which is fine """


# draws board for tic-tac-toe

def main():
    win = 0
    boardsize = 3  # define board dimension
    board = defineBoard(boardsize)
    createBoardLabels(board, boardsize)
    drawBoard(board, boardsize)
    Player_1(board, boardsize)


def defineBoard(boardsize):
    board = [[""] * boardsize for i in range(boardsize)]  # make the basic (non-drawable) version of theboard
    return board


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

def check_hoz(board): # FUNCTION TO CHECK ALL HORIZONTAL WIN STATES
    """a win is assumed, this function checks to see
    if the cells are not the same and sets win flag to false """
    """return data type is a string"""

    win = "true"

    # CHECKING THE TOP ROW
    i = 0
    for j in range(2):
        if board[i][j] != board[i][j+1]:
            win = "false"

    # CHECKING THE MIDDLE ROW
    i = 1
    for j in range(2):
        if board[i][j] != board[i][j+1]:
            win = "false"

    # CHECKING THE BOTTOM ROW
    i = 2
    for j in range(2):
        if board[i][j] != board[i][j+1]:
            win = "false"

    return win

def check_vert(board): # FUNCTION TO CHECK ALL VERTICAL WIN STATES
    """a win is assumed, this function checks to see if cells are not
    the same and checks the same ans sets win flag to false
    return data type is a string
    """

    win = 'true'

    #LEFT VERTICAL
    j = 0
    for i in range(2):
        if board[i][j] != board[i+1][j]:
            win = 'false'

    # MIDDLE VERTICAL
    j = 1
    for i in range(2):
        if board[i][j] != board[i + 1][j]:
            win = "false"
            # print ("win is {}".format(win))

    # RIGHT VERTICAL
    j = 2
    for i in range(2):
        if board[i][j] != board[i + 1][j]:
            win = "false"
            # print ("win is {}".format(win))

    return win


def check_diag(board):
    """

    """
    win = "true"
    # CHECK FROM TOP LEFT TO BOTTOM RIGHT
    j = 0
    for i in range(2):
        if board[i][j] != board[i+1][j+1]:
            win = "false"
        j = j+1

    #CHECKS FROM TOP RIGHT TO BOTTOM LEFT
    j = 2
    for i in range (2):
        if (board[i][j] != board[i+1][j-1]):
            win = "false"
        j = j-1

    return win




def check_win_all(board):

    if check_hoz(board) is "true" or check_vert(board) is "true" or check_diag(board) is "true":
        return "true"
    else:
        return "false"

def Player_1(board,boardsize):
    elem = 'X'
    chosenCell = inputChosenCell_1()
    board = setElem(elem, chosenCell, board, boardsize)
    drawBoard(board,boardsize)
    win = check_win_all(board)
    if win is "false":

        Player_2(board,boardsize)
    else:
        print('Congratulations Player 1! You win!')

def Player_2(board, boardsize):
    elem = 'o'
    chosenCell = inputChosenCell_2()
    board = setElem(elem, chosenCell, board, boardsize)
    drawBoard(board, boardsize)
    win = check_win_all(board)
    if win is "false":

        Player_1(board, boardsize)
    else:
        print('Congratulations Player 2! You win!')

def inputChosenCell_1():
    """prompts the player for input and returns their chosen move."""

    chosenCell = int(input("Player 1!! Pick a position"))
    if chosenCell > 9:
         #checking if player 1 enters a number bigger than 9
        print("Position invalid. Please pick another position that is displayed on the board")
    else:
        return chosenCell

def inputChosenCell_2():
    chosenCell = int(input("Player2!! pick a position"))
    if chosenCell > 9:
        #checking if player 2 enters a number grater than 9
        print("position invalid. Please pick another position that is displayed on the board ")
    else:
        return chosenCell


def setElem(elem, chosenCell, board, boardsize):
    for j in range(3):
        for i in range(3):
            if chosenCell == board[i][j]:
                board[i][j] = elem
                return board


#def checkwin(board, boardsize):
 #   if check_win_all(board) is "true":

main()  # run the program


