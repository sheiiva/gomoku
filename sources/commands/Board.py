#
# Epitech 2020 Python3 project - Gomoku.
#
# (02/02/2021) - Barcelona
# Authors:  Corentin COUTRET-ROZET <corentin.rozet@epitech.eu>
#           Maxence DESROUSSEAUX <maxence.desrousseaux@epitech.eu>
#           Hugo LACKAR <hugo1.lachkar@epitech.eu>
#

from sources.algorithm.AIMove import AI
from sources.utils.definitions import *
from sources.GameBoard import GameBoard
from sources.utils.Log import Log
from sources.utils.tools import isInt


class Board():

    """
    Board class to run 'Board' command.
    """

    def __init__(self, parsedInput: list, gameBoard: GameBoard):
        if self.check(parsedInput) != 84:
            self.run(gameBoard)

    def check(self, parsedInput: list) -> int:

        if len(parsedInput) != 1:
            Log('ERROR', 'Board command - No arguments expected.')
            return 84
        return 0

    def setBoard(self, gameBoard: GameBoard) -> list:

        def checkInput(coords: str) -> int:
            cs = coords.split(',')
            if len(cs) != 3:
                return 84
            for c in cs:
                if isInt(c) is False:
                    return 84
            if int(cs[2]) not in [1, 2, 3]:
                return 84
            if int(cs[0]) not in range(gameBoard._size) or int(cs[1]) not in range(gameBoard._size):
                return 84
            return 0

        while True:
            inpt = input()
            if inpt == "DONE":
                break
            elif checkInput(inpt) == 84:
                Log('ERROR', 'Board command - Wrong coordinates format.')
            else:
                cs = inpt.split(',')
                gameBoard._board[int(cs[0])][int(cs[1])] = int(cs[2])

    def run(self, gameBoard: GameBoard) -> int:

        # Reset board
        gameBoard._board = gameBoard.create(gameBoard._size)
        # Get information
        self.setBoard(gameBoard)

        ## Plan new move
        x, y = AI().getBestMove(gameBoard)
        # Print out the move
        print(f'{x},{y}')
        # Save the move
        gameBoard._board[x][y] = BRAIN
