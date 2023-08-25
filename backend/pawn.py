from backend.color import Color
from backend.piece import Piece
from backend.coordinate import Coordinate
from typing import List


class Pawn(Piece):

    def __init__(self, row: int, col: int, color: Color):
        self.hasMoved = False
        Piece.__init__(self, row, col, color)

    def move(self, board: List[List['Piece']], new_col: int, new_row: int):
        self.hasMoved = True
        Piece.move(self, board, new_col, new_row)

    # click, it shows all the squares you can move to
    def can_move(self, board: List[List[Piece]]) -> List: # todo: en passant!!!!!!!!!!!!!!!!!!!
        # list of movable squares
        movable_squares: List[Coordinate] = []
        multiplier = self.color.value

        move_target = board[self.coordinate.row + multiplier][self.coordinate.col]  # pawns will never be able to move
                                                                                    # out of bounds since they will
                                                                                    # become a new piece

        attack_vert = self.coordinate.row + multiplier
        attack_left = self.coordinate.col - 1
        attack_right = self.coordinate.col + 1

        # check for available move
        if move_target is None:
            movable_squares.append(
                Coordinate.__new__(Coordinate).__init__(self.coordinate.row + multiplier, self.coordinate.col))

        if not self.hasMoved:
            move_target = board[self.coordinate.row + 2*multiplier][self.coordinate.col]

            if move_target is None:  # todo: cleanup, repeated code snippet
                movable_squares.append(
                    Coordinate.__new__(Coordinate).__init__(self.coordinate.row + multiplier, self.coordinate.col))

        if (Piece.check_bounds(attack_vert, attack_right) and Piece.check_bounds(attack_vert, attack_left)):
            attack_target_right = board[attack_vert][attack_right]
            attack_target_left = board[attack_vert][attack_left]

            # check for available attack
            if attack_target_right is not None and attack_target_right.color is not self.color:
                movable_squares.append(attack_target_right.coordinate)

            if attack_target_left is not None and attack_target_left.color is not self.color:
                movable_squares.append(attack_target_left.coordinate)


        return movable_squares



