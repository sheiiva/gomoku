#
# Epitech 2020 Python3 project tests - Gomoku.
#
# (02/05/2021) - Barcelona
# Authors:  Corentin COUTRET-ROZET <corentin.rozet@epitech.eu>
#           Maxence DESROUSSEAUX <maxence.desrousseaux@epitech.eu>
#           Hugo LACKAR <hugo1.lachkar@epitech.eu>
#

import pytest

from sources.commands.Start import Start


def test_normal_case(capsys):

    # Set
    args = ['START', '20']
    # Run
    Start(args, None)
    # Tests
    redir = capsys.readouterr()
    assert redir.out == 'OK\n'


def test_wrong_args(capsys):

    # Set
    args = ['START']
    # Run
    Start(args, None)
    # Tests
    redir = capsys.readouterr()
    assert redir.out == 'ERROR Start command - Invalid arguments.\n'


def test_args_not_digit(capsys):

    # Set
    args = ['START', 'digit']
    # Run
    Start(args, None)
    # Tests
    redir = capsys.readouterr()
    assert redir.out == 'ERROR Start command - Invalid arguments.\n'


def test_ko_wrong_size(capsys):

    # Set
    args = ['START', '-1']
    # Run
    Start(args, None)
    # Tests
    redir = capsys.readouterr()
    assert redir.out == 'ERROR Start command - Invalid size.\n'
