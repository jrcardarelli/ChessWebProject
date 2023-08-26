from backend.color import Color
from backend.pawn import Pawn
from backend.piece import Piece

from backend.square import Square


class Board:

    def __init__(self):
        self.board: list[list[Square]] = []
        self.map = {}

        for i in range(8):
            new_list: list[Square] = []
            self.board.append(new_list)

            for j in range(8):
                new_square = Square()

                row = str(8 - i)  # convert 0 index to reverse 1 index
                col = chr(j + 97)  # convert from number to letter in ascii
                coord = col + row  # save each square to map of its coordinate

                self.map[coord] = new_square
                self.board[i].append(new_square)

    def populate(self):
        # fill each square with the correct pieces
        # just pawns rn

        for i in range(8):
            self.board[1][i].set_piece(Piece(Color.BLACK, 1, i))
            self.board[6][i].set_piece(Piece(Color.WHITE, 6, i))

    def print(self):
        for row in self.board:
            for element in row:
                print(element, end=" ")
            print()  # Move to the next line after each row

    def same_color(self, square: Square, player_color: Color):
        if square.isEmpty:
            return False
        if square.piece.color is not player_color:
            return False

        return True
