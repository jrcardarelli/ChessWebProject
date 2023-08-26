from backend.color import Color
from backend.piece import Piece
from backend.square import Square


class Pawn(Piece):

    def __init__(self, row: int, col: int, color: Color):
        self.hasMoved = False
        Piece.__init__(self, row, col, color)

    def move(self, board: list[list[Square]], new_col: int, new_row: int):
        self.hasMoved = True
        Piece.move(self, board, new_col, new_row)

    # click, it shows all the squares you can move to
    def can_move(self, board: list[list[Square]]) -> list:  # todo: en passant!!!!!!!!!!!!!!!!!!!
        # list of movable squares
        movable_squares: list[Square] = []
        multiplier = self.color.value

        # pawns will never be able to move
        # out of bounds since they will
        # become a new piece
        move_target = board[self.row + multiplier][self.col]

        attack_vert = self.row + multiplier
        attack_left = self.col - 1
        attack_right = self.col + 1

        # check for available move
        if move_target.isEmpty:
            movable_squares.append(Square(self.row + multiplier, self.col))

        if not self.hasMoved:
            move_target = board[self.row + 2 * multiplier][self.col]

            if move_target.isEmpty:  # todo: cleanup, repeated code snippet
                movable_squares.append(move_target)

        if Piece.check_bounds(attack_vert, attack_right):
            attack_target_right = board[attack_vert][attack_right]

            # check for available attack
            if attack_target_right.isEmpty and attack_target_right.piece.color is not self.color:
                movable_squares.append(attack_target_right)

        if Piece.check_bounds(attack_vert, attack_left):
            attack_target_left = board[attack_vert][attack_left]

            # check for available attack
            if attack_target_left.isEmpty and attack_target_left.piece.color is not self.color:
                movable_squares.append(attack_target_left)

        return movable_squares

    def __str__(self):
        color = self.color.name[0]

        return color + 'p'
