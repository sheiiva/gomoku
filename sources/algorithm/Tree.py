#
# Epitech 2020 Python3 project - Gomoku.
#
# (02/17/2021) - Barcelona
# Authors:  Corentin COUTRET-ROZET <corentin.rozet@epitech.eu>
#           Maxence DESROUSSEAUX <maxence.desrousseaux@epitech.eu>
#           Hugo LACKAR <hugo1.lachkar@epitech.eu>
#

from copy import deepcopy, copy
from math import inf

from sources.GameBoard import GameBoard
from sources.utils.Log import Log
from sources.utils.tools import isInt
from sources.utils.definitions import *


class Node():

    """
    Node class to run Node move and weights computations.
    """

    def __init__(self, gameBoard=None, x=-1, y=-1, score=0):
        self._coords = [x, y, score]
        if gameBoard:
            self._board = gameBoard.copy()
        else:
            self._board = GameBoard(0)
        self._children = []

    def setChild(self, gameBoard: GameBoard, coords: list) -> None:
        self._children.append(Node(gameBoard, coords[X], coords[Y], coords[SCORE]))

    def computeMaximizeWeights(self, next: int, maximize: bool, res: list, player: int) -> list:

        if maximize and next is player:
            res[0] += 10
        else:
            maximize = False

        return maximize

    def computeMinimizeWeights(self, next: int, maximize: bool, res: list, player: int) -> list:

        enemy = BRAIN if player is OPPONENT else OPPONENT

        if not maximize and next is enemy:
            res[1] += 10
        else:
            maximize = True

        return maximize


    def evalDir(self, gameBoard: GameBoard, dirs: list, coords: list, player: int) -> list:
        
        def addStrikes(gameBoard: GameBoard, dirs: list, coords: list, player: int, res: list) -> None:

            enemy = BRAIN if player is OPPONENT else OPPONENT

            for dir in dirs:
                for i in range(1, RANGE+1):
                    nx = coords[X] + (GETVECTOR(dir)[X] * i)
                    ny = coords[Y] + (GETVECTOR(dir)[Y] * i)
                    if nx not in range(gameBoard._size) or ny not in range(gameBoard._size):
                        continue
                    next = gameBoard._board[nx][ny]
                    if next is enemy:
                        break
                    elif next is EMPTY:
                        res[0] += 1
                        break
            for dir in dirs:
                for i in range(1, RANGE+1):
                    nx = coords[X] + (GETVECTOR(dir)[X] * i)
                    ny = coords[Y] + (GETVECTOR(dir)[Y] * i)
                    if nx not in range(gameBoard._size) or ny not in range(gameBoard._size):
                        continue
                    next = gameBoard._board[nx][ny]
                    if next is player:
                        break
                    elif next is EMPTY:
                        res[1] += 1
                        break

        def evalDirWeights(gameBoard: GameBoard, dirs: list, res: list, coords: list, player: int, maximize: bool) -> None:
            
            for dir in dirs:
                maxi = maximize
                for i in range(1, RANGE+1):
                    nx = coords[X] + (GETVECTOR(dir)[X] * i)
                    ny = coords[Y] + (GETVECTOR(dir)[Y] * i)
                    if nx not in range(gameBoard._size) or ny not in range(gameBoard._size):
                        continue
                    next = gameBoard._board[nx][ny]
                    if maximize:
                        maxi = self.computeMaximizeWeights(next, maxi, res, player)
                    else:
                        maxi = self.computeMinimizeWeights(next, maxi, res, player)

        res = [10, 10]
        # Compute both maximizing and minizing weights
        evalDirWeights(gameBoard, dirs, res, coords, player, True)
        evalDirWeights(gameBoard, dirs, res, coords, player, False)
        addStrikes(gameBoard, dirs, coords, player, res)
        return res

    def eval(self, gameBoard: GameBoard, coords: list, player: int) -> int:

        # Check for victory
        win = gameBoard.isWinning(coords, player)
        if win == BRAIN:
            return inf
        elif win == OPPONENT:
            return 10000000000

        evals = [
            # Vertical
            self.evalDir(gameBoard, [SOUTH, NORTH], coords, player),
            # Horizontal
            self.evalDir(gameBoard, [EAST, WEST], coords, player),
            # Diagonal (Top-Left - Bottom-Right)
            self.evalDir(gameBoard, [NORTHWEST, SOUTHEAST], coords, player),
            # Diagonal (Top-Right - Bottom-Left)
            self.evalDir(gameBoard, [NORTHEAST, SOUTHWEST], coords, player)
        ]

        transpose = list(map(list, zip(*evals)))
        return max(max(res for res in transpose))


class Tree():

    """
    Tree class to manage Nodes.
    """

    def __init__(self, gameBoard: GameBoard, depth: int, player: int):
        self._root = Node()
        #
        self.generate(gameBoard, depth, player, self._root)

    def generate(self, gameBoard: GameBoard, depth: int, player: int, node: Node):

        if depth == 0:
            return

        node._board = gameBoard.copy()
        for i in range(gameBoard._size):
            for j in range(gameBoard._size):
                if gameBoard._board[i][j] is EMPTY and gameBoard.hasNeighbor(i, j):
                    # Simulate move
                    gameBoard._board[i][j] = player
                    # Generate children
                    score = node.eval(gameBoard, [i, j], player)
                    node.setChild(gameBoard.copy(), [i, j, score])
                    # Get to next level
                    nextPlayer = BRAIN if player is OPPONENT else OPPONENT
                    self.generate(gameBoard, depth-1, nextPlayer, node._children[-1])
                    # Undo Simulation
                    gameBoard._board[i][j] = EMPTY
