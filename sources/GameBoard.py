#
# Epitech 2020 Python3 project - Gomoku.
#
# (02/02/2021) - Barcelona
# Authors:  Corentin COUTRET-ROZET <corentin.rozet@epitech.eu>
#           Maxence DESROUSSEAUX <maxence.desrousseaux@epitech.eu>
#           Hugo LACKAR <hugo1.lachkar@epitech.eu>
#

from sources.utils.definitions import *


class GameBoard():

    """
    GameBoard class that allows game board data computations and storage.
    """

    def __init__(self, size: int):
        self._size = size  # Default size
        self._settings = {
            'timeout_turn': 0,
            'timeout_match': 0,
            'max_memory': 0,
            'time_left': 0,
            'game_type': 0,
            'rule': 0,
            'evaluate': 0,
            'folder': './'
            }
        self._board = self.create(size)

    def copy(self):
        copy = GameBoard(self._size)
        copy._settings = self._settings
        copy._board = self._board
        return copy

    def hasNeighbor(self, x: int, y: int) -> bool:
        """Check around map[y][x] for empty space.

        Args:
            x (int): X axis coordinates
            j (int): Y axis coordinates

        Returns:
            bool: True if there is at least one neighbor. False Otherwise
        """

        for dir in VECTOR:
            nx = x + dir[X]
            ny = y + dir[Y]
            if nx not in range(self._size) or ny not in range(self._size):
                continue
            if self._board[nx][ny] is not EMPTY:
                return True
        return False

    def create(self, size: int) -> list:
        """Create a n*n sized map.

        Args:
            size (int): Size of the board.

        Returns:
            list: Result map as a list of list.
        """
        return [[0 for _ in range(size)] for _ in range(size)]

    def evalVictory(self, coords: list, player: int) -> bool:
        
        x = coords[X]
        y = coords[Y]

        counter = 0
        for i in range(1, RANGE+1):
            if x+i not in range(self._size):
                continue
            neighbor = self._board[x+i][y]
            if neighbor is player:
                counter += 1
            else:
                break
        for i in range(1, RANGE+1):
            if x-i not in range(self._size):
                continue
            neighbor = self._board[x-i][y]
            if neighbor is player:
                counter += 1
            else:
                break
        if counter >= RANGE:
            return True

        counter = 0
        for i in range(1, RANGE+1):
            if y+i not in range(self._size):
                continue
            neighbor = self._board[x][y+i]
            if neighbor is player:
                counter += 1
            else:
                break
        for i in range(1, RANGE+1):
            if y-i not in range(self._size):
                continue
            neighbor = self._board[x][y-i]
            if neighbor is player:
                counter += 1
            else:
                break
        if counter >= RANGE:
            return True

        counter = 0
        for i in range(1, RANGE+1):
            if x+i not in range(self._size) or y+i not in range(self._size):
                continue
            neighbor = self._board[x+i][y+i]
            if neighbor is player:
                counter += 1
            else:
                break
        for i in range(1, RANGE+1):
            if x-i not in range(self._size) or y-i not in range(self._size):
                continue
            neighbor = self._board[x-i][y-i]
            if neighbor is player:
                counter += 1
            else:
                break
        if counter >= RANGE:
            return True

        counter = 0
        for i in range(1, RANGE+1):
            if x+i not in range(self._size) or y-i not in range(self._size):
                continue
            neighbor = self._board[x+i][y-i]
            if neighbor is player:
                counter += 1
            else:
                break
        for i in range(1, RANGE+1):
            if x-i not in range(self._size) or y+i not in range(self._size):
                continue
            neighbor = self._board[x-i][y+i]
            if neighbor is player:
                counter += 1
            else:
                break
        if counter >= RANGE:
            return True

        return False

    def isWinning(self, coords: list, player: int) -> int:

        nextPlayer = BRAIN if player is OPPONENT else OPPONENT

        if self.evalVictory(coords, player):
            return 1
        elif self.evalVictory(coords, nextPlayer):
            return 2
        return 0