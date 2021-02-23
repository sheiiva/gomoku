#
# Epitech 2020 Python3 project tests - Gomoku.
#
# (02/05/2021) - Barcelona
# Authors:  Corentin COUTRET-ROZET <corentin.rozet@epitech.eu>
#           Maxence DESROUSSEAUX <maxence.desrousseaux@epitech.eu>
#           Hugo LACKAR <hugo1.lachkar@epitech.eu>
#

import pytest

from sources.commands.Begin import Begin
from sources.GameBoard import GameBoard


def test_normal_case(capsys):

    # Set
    args = ['BEGIN']
    gameBoard = GameBoard(20)
    # Run
    Begin(args, gameBoard)
    # Tests
    assert gameBoard._board[10][10] == 1

    redir = capsys.readouterr()
    assert redir.out == '10,10\n'


def test_ko_args(capsys):

    args = ['BEGIN', '_']

    Begin(args, None)

    redir = capsys.readouterr()
    assert redir.out == 'ERROR Begin command - No arguments expected.\n'
