#
# Epitech 2020 Python3 project - Gomoku.
#
# (02/02/2021) - Barcelona
# Authors:  Corentin COUTRET-ROZET <corentin.rozet@epitech.eu>
#           Maxence DESROUSSEAUX <maxence.desrousseaux@epitech.eu>
#           Hugo LACKAR <hugo1.lachkar@epitech.eu>
#

from sources.GameBoard import GameBoard
from sources.utils.tools import isInt
from sources.utils.Log import Log


class Start():

    """
    Start class to run 'Start' command.
    """

    def __init__(self, parsedInput: list, gameBoard: GameBoard):
        if self.check(parsedInput) != 84:
            self.run()

    def check(self, parsedInput: list) -> int:

        if len(parsedInput) != 2 or isInt(parsedInput[1]) is False:
            Log('ERROR', 'Start command - Invalid arguments.')
            return 84
        if int(parsedInput[1]) < 5:
            Log('ERROR', 'Start command - Invalid size.')
            return 84
        return 0

    def run(self) -> None:

        print('OK')
