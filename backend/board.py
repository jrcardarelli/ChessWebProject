from backend.color import Color
from backend.pawn import Pawn
from backend.piece import Piece
from typing import List


class Board:

    def __init__(self):
        self.board: List[List[Piece]] = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]
        ]
        for i in range(8):
            self.board[1][i] = Pawn(1, i, Color.BLACK)
            self.board[6][i] = Pawn(6, i, Color.WHITE)

    def print(self):
        for row in self.board:
            for element in row:
                print(element, end=" ")
            print()  # Move to the next line after each row
    def same_color(self, row: int, col: int, player_color: Color) -> bool:
        piece = self.board[row][col]
        if piece is None or piece.color is not player_color:
            return False

        return True