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
from deps.infos import *


class Info():

    """
    Info class to run 'Info' command.
    """

    def __init__(self, parsedInput: list, gameBoard: GameBoard):
        if self.check(parsedInput, gameBoard._settings) != 84:
            self.run(parsedInput, gameBoard)

    def check(self, parsedInput: list, settings: dict) -> int:

        if len(parsedInput) != 3:
            Log('ERROR', 'Info command - Invalid arguments.')
            return 84
        if parsedInput[1] not in settings.keys():
            Log('ERROR', 'Info command - Invalid key.')
            return 84
        return 0

    def run(self, parsedInput: list, gameBoard: GameBoard) -> None:

        key = parsedInput[1]
        value = parsedInput[2]

        gameBoard._settings[key] = int(value)
