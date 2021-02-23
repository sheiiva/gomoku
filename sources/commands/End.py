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


class End():

    """
    End class to run 'End' command.
    """

    def __init__(self, parsedInput: list, gameBoard: GameBoard):
        if self.check(parsedInput) != 84:
            self.run()

    def check(self, parsedInput: list) -> int:

        if len(parsedInput) != 1:
            Log('ERROR', 'End command - No arguments expected.')
            return 84
        return 0

    def run(self) -> None:

        exit(0)
