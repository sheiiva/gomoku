#
# Epitech 2020 Python3 project tests - Gomoku.
#
# (02/05/2021) - Barcelona
# Authors:  Corentin COUTRET-ROZET <corentin.rozet@epitech.eu>
#           Maxence DESROUSSEAUX <maxence.desrousseaux@epitech.eu>
#           Hugo LACKAR <hugo1.lachkar@epitech.eu>
#

import pytest

from sources.commands.About import About
from deps.infos import *


def test_normal_case(capsys):

    args = ['ABOUT']

    About(args, None)

    redir = capsys.readouterr()
    assert redir.out == f'name="{NAME}", version="{VERSION}", author="{AUTHORS}", country="{COUNTRY}"\n'


def test_ko_args(capsys):

    args = ['ABOUT', '_']

    About(args, None)

    redir = capsys.readouterr()
    assert redir.out == 'ERROR About command - No arguments expected.\n'
