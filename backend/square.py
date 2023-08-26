from backend.piece import Piece


class Square:

    def __init__(self):
        self.piece = None
        self.isEmpty = True

    def set_piece(self, piece: Piece):
        self.piece = piece
        self.isEmpty = False

    def remove_piece(self):
        self.piece = None
        self.isEmpty = True

    def __str__(self):
        if self.isEmpty:
            return "."
        return self.piece.__str__()
