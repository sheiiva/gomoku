#
# Epitech 2020 Python3 project - Gomoku.
#
# (02/05/2021) - Barcelona
# Authors:  Corentin COUTRET-ROZET <corentin.rozet@epitech.eu>
#           Maxence DESROUSSEAUX <maxence.desrousseaux@epitech.eu>
#           Hugo LACKAR <hugo1.lachkar@epitech.eu>
#

def isInt(var) -> bool:

    try:
        int(var)
    except ValueError:
        return False
    else:
        return True
