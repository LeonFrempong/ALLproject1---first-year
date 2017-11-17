""" written by John Halloran. Please acknowledge if used """

""" below, there are spaces for you to add comments. You may want to add more comments than this, which is fine """


# draws board for tic-tac-toe

def main():
    # statuslist is used like a register and pass between player 1 and player 2.
        # when the player makes their turn, statusList is marked with their element(x or o)
        # to control what cells the player can select.
        # it also makes it easier for detecting a draw,
    statusList = ["", 1,2,3,4,5,6,7,8,9] # used to check available numbers in the board
    boardsize = 3  # define board dimension
    board = defineBoard(boardsize)
    createBoardLabels(board, boardsize)
    drawBoard(board, boardsize)
    Player_1(board, boardsize, statusList)


def defineBoard(boardsize):
    board = [[""] * boardsize for i in range(boardsize)]
    return board


def createBoardLabels(board, boardsize):  #
    counter = 0
    for i in range(boardsize):
        for j in range(boardsize):
            counter += 1
            board[i][j] = counter
    return (board)


def print_divider(boardsize):

    print ('|'.join(['____' for x in range(boardsize)]))


def print_blank(boardsize):
    print ('|'.join(['    ' for x in range(boardsize)]))

def print_labels(counter, board, boardsize):
    row = ' | '.join(['%2s' % board[counter][x] for x in range(boardsize)])
    row = ' ' + row
    print(row)


def drawBoard(board, boardsize):
    for i in range(boardsize):
        print_blank(boardsize)
        print_labels(i, board, boardsize)
        if (i == boardsize - 1):
            print_blank(boardsize)
        else:
            print_divider(boardsize)


def check_win_left_vertical(board):
    """
    the first function below (check_win_left_vertical)
    shows that the function needs to check the left side of the
    board, if there is a win, by using the return function
    and the calling the function
    """
    win = 'true'
    j = 0
    for i in range(2):
        if board[i][j] != board[i + 1][j]:
            win = 'false'

    return (win)


def check_win_mid_vertical(board):
    """
    function checks the middle column for matches
    """
    win = "true"
    j = 1  # value has changed from 0-1 to detect the
    # j variable of 1 in the mid vertical column
    for i in range(2):
        if board[i][j] != board[i + 1][j]:
            win = "false"
            # print ("win is {}".format(win))

    return (win)  # shows whether win is true or false


def check_win_right_vertical(board):
    """
    function checks right most column for matches
    return data type: string
    """
    win = "true"
    j = 2  # value has changd to 2 to check if the third column is win true
    # or false
    for i in range(2):
        if board[i][j] != board[i + 1][j]:
            win = "false"
            # print ("win is {}".format(win))

    return (win)



def check_win_top_hoz(board):
    """
    function checks top row for matches
    return data type: string
    """
    win = "true"
    i = 0  # this shows that the variable has changed to j, to check win
    # in the horizontal top column
    for j in range(2):
        if board[i][j] != board[i][j + 1]:
            win = "false"

    return (win)


def check_win_mid_hoz(board):
    """
    function checks middle row for matches
    return data type: string

    """
    win = "true"
    i = 1  # this shows that the variable has changed to j, to check win
    # in the mid horizontal column
    # the value has changed to one to to check the mid row in the horizontal
    # column
    for j in range(2):
        if board[i][j] != board[i][j + 1]:
            win = "false"

    return (win)


def check_win_bottom_hoz(board):
    """
    function checks bottom row for matches
    return data type: string
    """
    win = "true"
    i = 2  # this shows that the variable has changed to j, to check win
    # in the horizontal top column
    # the value has changed to 2 to check win the bottom row
    for j in range(2):
        if board[i][j] != board[i][j + 1]:
            win = "false"

    return (win)


def check_win_first_diag(board):
    """
    function checks from top left to bottom right
    return data type: string
    """
    win = "true"
    j = 0
    for i in range(2):
        if board[i][j] != board[i + 1][j + 1]:  # the [j] adds one, so that the
            # diagonal can match the code on the board.
            win = "false"
        j = j + 1  # the j counts up from 0
    return (win)


def check_win_second_diag(board):
    """
    function checks from top right to bottom left
    return data type: string
    """
    win = "true"
    j = 2
    for i in range(2):
        if (board[i][j] != board[i + 1][j - 1]):
            win = "false"
        j = j - 1  # j counts down from two .....
    return (win)


def check_win_all(board):
    """
    function calls all win checking functions
    return data type: string
    """
    leftVert = check_win_left_vertical(board)
    midVert = check_win_mid_vertical(board)
    rightVert = check_win_right_vertical(board)
    topHoz = check_win_top_hoz(board)
    midHoz = check_win_mid_hoz(board)
    bottomHoz = check_win_bottom_hoz(board)
    firstDiag = check_win_first_diag(board)
    secDiag = check_win_second_diag(board)

    if leftVert == "true" or midVert == "true" or rightVert == "true" or topHoz == "true" or midHoz == "true" or bottomHoz == "true" or firstDiag == "true" or secDiag == "true":
        return "true"
    else:
        return "false"

def Player_1(board,boardsize, statusList):
    elem = 'X'
    chosenCell, statusList = inputChosenCell_1(elem, statusList)
    board = setElem(elem, chosenCell, board, boardsize)
    drawBoard(board,boardsize)
    win = check_win_all(board)
    if win == "false":
        intCounter = 0
        for item in statusList:     # checking if there are any integers left in statusList
            if type(item) == int:
                intCounter = intCounter + 1
        if intCounter == 0:     # if not, then the game is a draw
            print("Game is a draw")
            return
        Player_2(board,boardsize, statusList)
    else:
        print('Congratulations Player 1! You win!')

def Player_2(board, boardsize, statusList):
    elem = 'O'
    chosenCell, statusList = inputChosenCell_2(elem, statusList)
    board = setElem(elem, chosenCell, board, boardsize)
    drawBoard(board, boardsize)
    win = check_win_all(board)
    if win == "false":
        intCounter = 0
        for item in statusList:     # checking if there are any integers left in statusList
            if type(item) == int:
                intCounter = intCounter + 1
        if intCounter == 0:     # if not, then the game is a draw
            print("Game is a draw")
            return
        Player_1(board, boardsize, statusList)
    else:
        print('Congratulations Player 2! You win!')

def inputChosenCell_1(elem, statusList):
    """prompts the player for input and returns their chosen move."""
    while True:
        try:
            chosenCell = int(input("Player 1!! Pick a position"))
            if chosenCell > 9 or chosenCell < 1:
                #checking if player 1 enters a number bigger than 9
                print("Position invalid. Please pick another position that is displayed on the board")
            elif chosenCell not in statusList:  # checking if the chosencell is not in the statusList
                print("Your cell has been taken!")  #prints message then loops again

            else:
                for i in range(len(statusList)):    # looping through statusList
                    if i == chosenCell:             # finds the element corresponding with chosen cell
                        statusList[i] = elem        # and overwrites it with "X"
                        #print(statusList) # TEST
                        break
                break

        except ValueError:
            print("Your input must be an integer!")

    return chosenCell, statusList

def inputChosenCell_2(elem, statusList):
    """prompts the player for input and returns their chosen move."""
    while True:
        try:
            chosenCell = int(input("Player2!! pick a position"))
            if chosenCell > 9 or chosenCell < 1:
                #checking if player 2 enters a number grater than 9
                print("position invalid. Please pick another position that is displayed on the board ")
            elif chosenCell not in statusList:  #checking if the chosencell is not in the statusList
                print("Your cell has been taken!")  #prints message then loops again
            else:
                for i in range(len(statusList)):    # looping through statusList
                    if i == chosenCell:             # find the element corresponding with chosen cell
                        statusList[i] = elem        # and overwrites it with "O"
                        #print(statusList) # TEST
                        break
                break

        except ValueError:
            print("Your input must be an integer!")

    return chosenCell, statusList



def setElem(elem, chosenCell, board, boardsize):
    for j in range(3):
        for i in range(3):
            if chosenCell == board[i][j]:
                board[i][j] = elem
                return board


main()  # run the program


