from typing import List

from backend.color import Color
from backend.coordinate import Coordinate


class Piece:

    def check_bounds(self, row: int, col: int):
        if col < 0 or col > 7:
            return False
        if row < 0 or row > 7:
            return False

        return True

    def __init__(self, row: int, col: int, color: Color):
        self.isTaken = False
        self.coordinate = Coordinate(row, col)
        self.color = color

    def set_taken(self):
        self.isTaken = True
        # remove the piece from the board
        # perhaps by setting coords to something outside the board?

    def move(self, board: List[List['Piece']], new_col: int, new_row: int):
        occupier = board[new_row][new_col]

        if occupier is not None:
            occupier.set_taken()

        self.coordinate = Coordinate(new_row, new_col)
