#
# Epitech 2020 Python3 project - Gomoku.
#
# (02/02/2021) - Barcelona
# Authors:  Corentin COUTRET-ROZET <corentin.rozet@epitech.eu>
#           Maxence DESROUSSEAUX <maxence.desrousseaux@epitech.eu>
#           Hugo LACKAR <hugo1.lachkar@epitech.eu>
#

from sources.utils.definitions import BRAIN

from sources.GameBoard import GameBoard
from sources.utils.Log import Log


class Begin():

    """
    Begin class to run 'Begin' command.
    """

    def __init__(self, parsedInput: list, gameBoard: GameBoard):
        if self.check(parsedInput) != 84:
            self.run(parsedInput, gameBoard)

    def check(self, parsedInput: list) -> int:

        if len(parsedInput) != 1:
            Log('ERROR', 'Begin command - No arguments expected.')
            return 84
        return 0

    def run(self, parsedInput: list, gameBoard: GameBoard) -> None:

        x = int(gameBoard._size/2)
        y = int(gameBoard._size/2)

        # Print out the move
        print(f'{x},{y}')
        # Save the move
        gameBoard._board[x][y] = BRAIN
