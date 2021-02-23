#
# Epitech 2020 Python3 project tests - Gomoku.
#
# (02/05/2021) - Barcelona
# Authors:  Corentin COUTRET-ROZET <corentin.rozet@epitech.eu>
#           Maxence DESROUSSEAUX <maxence.desrousseaux@epitech.eu>
#           Hugo LACKAR <hugo1.lachkar@epitech.eu>
#

import pytest

from sources.utils.tools import isInt


def test_isInt_normal_case():

    assert isInt(2) is True


def test_isInt_letter_case():

    assert isInt('a') is False


def test_isInt_float_case():

    assert isInt('1.2') is False
