#
# Epitech 2020 Python3 project - Gomoku.
#
# (02/15/2021) - Barcelona
# Authors:  Corentin COUTRET-ROZET <corentin.rozet@epitech.eu>
#           Maxence DESROUSSEAUX <maxence.desrousseaux@epitech.eu>
#           Hugo LACKAR <hugo1.lachkar@epitech.eu>
#

from copy import deepcopy
from math import inf

from sources.GameBoard import GameBoard
from sources.algorithm.Tree import Tree, Node
from sources.utils.Log import Log
from sources.utils.definitions import *


class AI():

    """
    AI class to run AI move computations.
    """

    def minimax(self, gameBoard: GameBoard, depth: int, node: Node, player: int) -> list:

        if depth == 0 or len(node._children) == 0:
            return node._coords

        if player is BRAIN:
            bestMove = [-1, -1, -inf]
            for child in node._children:
                move = self.minimax(gameBoard, depth-1, child, NEXTPLAYER(player))
                if move[SCORE] > bestMove[SCORE]:
                    bestMove = deepcopy(move)
        else:
            bestMove = [-1, -1, inf]
            for child in node._children:
                move = self.minimax(gameBoard, depth-1, child, NEXTPLAYER(player))
                if move[SCORE] < bestMove[SCORE]:
                    bestMove = deepcopy(move)

        return bestMove

    def getBestMove(self, gameBoard: GameBoard) -> list:

        """Look for the best move to plan following a minimax-like algorithm.

        Args:
            gameBoard (GameBoard): The bord of the game.

        Returns:
            x, y: The coordinates of the best move.
        """

        depth = 1

        # Generate Possible move (Tree shaped)
        tree = Tree(gameBoard, depth, BRAIN)
        # Look for best moves
        x, y, _ = self.minimax(gameBoard, depth, tree._root, BRAIN)

        return [x, y]
