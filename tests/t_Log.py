#
# Epitech 2020 Python3 project tests - Gomoku.
#
# (02/05/2021) - Barcelona
# Authors:  Corentin COUTRET-ROZET <corentin.rozet@epitech.eu>
#           Maxence DESROUSSEAUX <maxence.desrousseaux@epitech.eu>
#           Hugo LACKAR <hugo1.lachkar@epitech.eu>
#

import pytest

from sources.utils.Log import Log


def test_normal_case(capsys):

    typ = 'ERROR'
    message = 'This is an error.'
    Log(typ, message)

    redir = capsys.readouterr()
    assert redir.out == f'{typ} {message}\n'


def test_message_case(capsys):

    typ = 'MESSAGE'
    message = 'This is an error.'
    Log(typ, message)

    redir = capsys.readouterr()
    assert redir.out == f'{typ} {message}\n'


def test_wrong_type_case(capsys):

    message = 'This is an error.'
    Log('PIEJZAPIJZPAIJZ', message)

    redir = capsys.readouterr()
    assert redir.out == f'ERROR {message}\n'
