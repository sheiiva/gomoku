#
# Epitech 2020 Python3 project tests - Gomoku.
#
# (02/05/2021) - Barcelona
# Authors:  Corentin COUTRET-ROZET <corentin.rozet@epitech.eu>
#           Maxence DESROUSSEAUX <maxence.desrousseaux@epitech.eu>
#           Hugo LACKAR <hugo1.lachkar@epitech.eu>
#

import pytest

from sources.commands.Board import Board
from sources.GameBoard import GameBoard


def test_ko_args(capsys):

    args = ['BOARD', '_']

    Board(args, None)

    redir = capsys.readouterr()
    assert redir.out == 'ERROR Board command - No arguments expected.\n'
