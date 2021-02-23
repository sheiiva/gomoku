#
# Epitech 2020 Python3 project - Gomoku.
#
# (02/02/2021) - Barcelona
# Authors:  Corentin COUTRET-ROZET <corentin.rozet@epitech.eu>
#           Maxence DESROUSSEAUX <maxence.desrousseaux@epitech.eu>
#           Hugo LACKAR <hugo1.lachkar@epitech.eu>
#

from sources.GameBoard import GameBoard
from sources.commands.Start import Start
from sources.commands.Turn import Turn
from sources.commands.Begin import Begin
from sources.commands.Board import Board
from sources.commands.Info import Info
from sources.commands.End import End
from sources.commands.About import About
from sources.utils.Log import Log


class Game():

    """
    Main class that allows computation and output printing for the game.
    """

    def __init__(self):
        self._gameBoard = GameBoard(19)
        self._commands = {
            'START': Start,
            'TURN': Turn,
            'BEGIN': Begin,
            'BOARD': Board,
            'INFO': Info,
            'END': End,
            'ABOUT': About
        }

    def parse(self, act: str) -> list:
        """Parse the input from into list of words.

        Args:
            act (str): Input to parse.

        Returns:
            list: Parsed input.
        """

        if act == '':
            return ['UNKNOWN']

        return act.replace(',', ' ').split()

    def action(self, parsedInput: list):
        """Fetch the right command to process and process it.

        Args:
            parsedInput (list): Input command to process.
        """

        try:
            self._commands[parsedInput[0]](parsedInput, self._gameBoard)
        except KeyError:
            Log('Error', 'Invalid command.')

    def run(self) -> None:

        """
        Run computations and process outputs.
        """

        while True:
            # Get opponent action
            ipt = input()
            # Process opponent action
            parsedInput = self.parse(ipt)
            # Answer back
            self.action(parsedInput)
