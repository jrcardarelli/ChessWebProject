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
            self.board[1][i] = Pawn(1, i, "BLACK")
            self.board[6][i] = Pawn(6, i, "WHITE")


    def