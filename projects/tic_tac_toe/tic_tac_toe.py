#!/usr/bin/env python3

"""Tic Tac Toe project to explore Python 3, I went with dictionaries, I could have
used a list and done things by index too."""

marksPlacedOnBoard = {
    'e7': ' ', 'e8': ' ', 'e9': ' ',
    'e4': ' ', 'e5': ' ', 'e6': ' ',
    'e1': ' ', 'e2': ' ', 'e3': ' '
}


# marksPlacedOnBoard = [' ']*10

def checkForGameOver(currentPlayer):
    '''Has the last move caused the condition for game over to be met'''

    def checkColumnCondition():
        columns = [
            ['e7', 'e4', 'e1'],
            ['e8', 'e5', 'e2'],
            ['e9', 'e6', 'e3']
        ]

        hasConditionBeenMet = True
        for x in columns:
            hasConditionBeenMet = True
            for element in x:
                hasConditionBeenMet = hasConditionBeenMet and marksPlacedOnBoard[
                    element] == currentPlayer
            if hasConditionBeenMet:
                return True

        return False

    def checkRowCondition():
        rows = [
            ['e7', 'e8', 'e9'],
            ['e4', 'e5', 'e6'],
            ['e1', 'e2', 'e3']
        ]

        for x in rows:
            hasConditionBeenMet = True
            for element in x:
                hasConditionBeenMet = hasConditionBeenMet and marksPlacedOnBoard[
                    element] == currentPlayer
            if hasConditionBeenMet:
                return True

        return False

    def checkDiagonalCondition():
        diagonals = [
            ['e7', 'e5', 'e3'],
            ['e1', 'e5', 'e9']
        ]

        for x in diagonals:
            hasConditionBeenMet = True
            for element in x:
                hasConditionBeenMet = hasConditionBeenMet and marksPlacedOnBoard[
                    element] == currentPlayer
            if hasConditionBeenMet:
                return True

        return False

    def checkIfItIsADraw():
        hasConditionBeenMet = True
        for element in marksPlacedOnBoard:
            hasConditionBeenMet = hasConditionBeenMet and marksPlacedOnBoard[
                element] != ' '

        return hasConditionBeenMet

    hasPlayerWon = checkColumnCondition() or checkRowCondition() or checkDiagonalCondition()
    isDraw = checkIfItIsADraw()

    if hasPlayerWon:
        print('Congratulations player {}, game over!'.format(currentPlayer))
        return True
    elif isDraw:
        print('A strange game. The only winning move is not to play. How about a nice game of chess?')
        return True
    else:
        return False


def checkForGameOver_v2():
    # marksPlacedOnBoard[1] == marksPlacedOnBoard[2] == marksPlacedOnBoard[3] == 'X'
    # etc...
    # also, check for winning combinations, we don't care how they are arranged.
    # ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    pass


def move(player):
    '''Gets a valid move for the player'''

    def isPlayerMoveValid(playerInput):
        '''Test that the current player can make their intended move'''

        if not playerInput.isnumeric():
            print('Only numbers 1-9 are allowed, please try again.')
            return False

        playerInputAsInt = int(playerInput)

        if playerInputAsInt < 1 or playerInputAsInt > 9:
            print('Only numbers in the range 1-9 are allowed, please try again.')
            return False

        placeholderKey = 'e' + str(playerInputAsInt)
        hasPlaceholderAlreadyBeenTaken = marksPlacedOnBoard[placeholderKey] is not ' '
        if hasPlaceholderAlreadyBeenTaken:
            print('That space has already been taken, please try again.')
            return False

        # If we get here, the player has entered a valid play
        return True

    # loop while player move is invalid, until we get a valid move.
    while True:

        playerInput = input('Choose your next position: (1-9) ')

        if isPlayerMoveValid(playerInput):
            # update the board
            placeholderKey = 'e' + playerInput
            marksPlacedOnBoard[placeholderKey] = player
            break


def drawBoard():
    '''Draws the marks on the board'''

    print("\n" * 100)
    print("WOPR - Deep Learning Platform v1.23")
    theBoardTemplate = '''\n
           |   |   
         {e7} | {e8} | {e9}
           |   |   
        ———+———+———
           |   |   
         {e4} | {e5} | {e6} 
           |   |   
        ———+———+———
           |   |   
         {e1} | {e2} | {e3} 
           |   |   \n'''
    print(theBoardTemplate.format(**marksPlacedOnBoard))
    #  print("{} {} {}\n{} {} {}\n {} {} {}\n".format(*board))


def main():
    '''Main execution loop where the game is played out'''

    isGameOver = False

    while True:

        drawBoard()

        for currentPlayer in ('X', 'O'):

            print('Ready player \'{}\'\n'.format(currentPlayer))
            move(currentPlayer)
            drawBoard()
            isGameOver = checkForGameOver(currentPlayer)
            if isGameOver:
                break

        if isGameOver:
            break


# execution starts here
main()
