from backend.board import Board
from backend.color import Color


class Game:
    def __init__(self):
        self.board: Board = None
        self.new_board()
        self.repl()

    def new_board(self):
        self.board = Board()
        self.board.populate()
        self.board.print()

    def repl(self):

        player_color = Color.WHITE

        while True:
            user_input = input(">>> ").lower()
            # math way here would be unnecessary for when user concedes or restarts
            if user_input == 'concede':
                print("lost")
                break
            elif user_input == 'restart':
                print("restarted")
                self.new_board()

            # invalid coordinates
            elif (len(user_input) != 2
                  or user_input not in self.board.map):
                print("invalid coordinate. pick a valid coordinate")

            # valid coordinates but if not one of the player's piece, therefore not his color, return error
            elif not self.board.same_color(self.board.map[user_input], player_color):
                print("invalid. pick a piece with your color")

            else:
                print("valid move")
            # board.getpiece at this location, get canMove list,
            # if canMove list is empty, invalid move
            # request another input for move, it must be contained in the canMove list
            # set piece to move
            # once moves changes color to black and so on
