#
# Epitech 2020 Python3 project tests - Gomoku.
#
# (02/05/2021) - Barcelona
# Authors:  Corentin COUTRET-ROZET <corentin.rozet@epitech.eu>
#           Maxence DESROUSSEAUX <maxence.desrousseaux@epitech.eu>
#           Hugo LACKAR <hugo1.lachkar@epitech.eu>
#

import pytest

from sources.commands.Info import Info
from sources.GameBoard import GameBoard
from deps.infos import *


def test_normal_case():

    # Set
    args = ['INFO', 'timeout_turn', '2']
    gameBoard = GameBoard(19)

    # Run
    Info(args, gameBoard)

    # Test
    assert gameBoard._settings['timeout_turn'] == 2


def test_ko_args(capsys):

    # Set
    args = ['INFO', '_']
    gameBoard = GameBoard(19)

    # Run
    Info(args, gameBoard)

    # Test
    redir = capsys.readouterr()
    assert redir.out == 'ERROR Info command - Invalid arguments.\n'


def test_ko_key(capsys):

    # Set
    args = ['INFO', 'wrongKey', '2']
    gameBoard = GameBoard(19)

    # Run
    Info(args, gameBoard)

    # Test
    redir = capsys.readouterr()
    assert redir.out == 'ERROR Info command - Invalid key.\n'
