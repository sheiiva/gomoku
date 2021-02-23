#
# Epitech 2020 Python3 project tests - Gomoku.
#
# (02/05/2021) - Barcelona
# Authors:  Corentin COUTRET-ROZET <corentin.rozet@epitech.eu>
#           Maxence DESROUSSEAUX <maxence.desrousseaux@epitech.eu>
#           Hugo LACKAR <hugo1.lachkar@epitech.eu>
#

import pytest

from sources.commands.End import End
from deps.infos import *


def test_normal_case():

    args = ['END']

    try:
        End(args, None)
    except SystemExit:
        assert True
    else:
        assert False


def test_ko_args(capsys):

    args = ['END', '_']

    End(args, None)

    redir = capsys.readouterr()
    assert redir.out == 'ERROR End command - No arguments expected.\n'
