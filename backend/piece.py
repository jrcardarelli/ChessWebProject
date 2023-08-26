from backend.color import Color


class Piece:

    def check_bounds(self, row: int, col: int):
        if col < 0 or col > 7:
            return False
        if row < 0 or row > 7:
            return False

        return True

    def __init__(self, color: Color, row: int, col: int):
        self.isTaken = False
        self.color = color
        self.row = row
        self.col = col

    def set_taken(self):
        self.isTaken = True
        self.row = None
        self.col = None

    def move(self, board, new_col: int, new_row: int):
        pos = board[self.row][self.col]
        target = board[new_row][new_col]

        if not target.isEmpty:
            target.piece.set_taken()

        self.row = new_row
        self.col = new_col
        target.piece = self
        pos.remove_piece()

    def __str__(self):
        color = self.color.name[0]

        return color
