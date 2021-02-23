#
# Epitech 2020 Python3 project - Gomoku.
#
# (02/02/2021) - Barcelona
# Authors:  Corentin COUTRET-ROZET <corentin.rozet@epitech.eu>
#           Maxence DESROUSSEAUX <maxence.desrousseaux@epitech.eu>
#           Hugo LACKAR <hugo1.lachkar@epitech.eu>
#

from sources.GameBoard import GameBoard
from sources.utils.Log import Log
from sources.utils.tools import isInt
from sources.utils.definitions import * # remove if not used
from sources.algorithm.AIMove import AI


class Turn():

    """
    Turn class to run 'Turn' command.
    """

    def __init__(self, parsedInput: list, gameBoard: GameBoard):
        if self.check(parsedInput, gameBoard) != 84:
            self.run(parsedInput, gameBoard)

    def check(self, parsedInput: list, gameBoard: GameBoard) -> int:

        if len(parsedInput) != 3:
            Log('ERROR', 'Turn command - Invalid arguments.')
            return 84
        if isInt(parsedInput[1]) is False or isInt(parsedInput[2]) is False:
            Log('ERROR', 'Turn command - Invalid size.')
            return 84
        if int(parsedInput[1]) not in range(gameBoard._size)\
            or int(parsedInput[2]) not in range(gameBoard._size):
            Log('ERROR', 'Turn command - Invalid size.')
            return 84
        return 0

    def run(self, parsedInput: list, gameBoard: GameBoard) -> None:

        # Save opponent move
        x = int(parsedInput[1])
        y = int(parsedInput[2])
        gameBoard._board[x][y] = OPPONENT

        ## Plan new move
        x, y = AI().getBestMove(gameBoard)
        # Print out the move
        print(f'{x},{y}')
        # Save the move
        gameBoard._board[x][y] = BRAIN
