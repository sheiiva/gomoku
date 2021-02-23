#
# Epitech 2020 Python3 project - Gomoku.
#
# (02/02/2021) - Barcelona
# Authors:  Corentin COUTRET-ROZET <corentin.rozet@epitech.eu>
#           Maxence DESROUSSEAUX <maxence.desrousseaux@epitech.eu>
#           Hugo LACKAR <hugo1.lachkar@epitech.eu>
#


class Log():

    """
    Turn class to run 'Turn' command.
    """

    def __init__(self, logtype: str, message: str):
        self._types = ['ERROR', 'UNKNOWN', 'MESSAGE', 'DEBUG']
        self.run(logtype, message)

    def run(self, logtype: str, message: str) -> None:

        print(f"{logtype if logtype in self._types else 'ERROR'} {message}")
