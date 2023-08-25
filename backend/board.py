from backend.color import Color
from backend.pawn import Pawn


class Board:

    def __init__(self):
        self.board = [
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

    # def isColor(self, color: Color) -> bool:
    #     for row in self.board:
    #         for element in row:
    #             print(element, end=" ")
    #         print()  # Move to the next line after each row