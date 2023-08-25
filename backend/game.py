from backend.board import Board
from backend.color import Color


class Game:
    def __init__(self):
        self.new_board()
        self.repl()

    def new_board(self):
        self.board = Board()
        self.board.print()

    def repl(self):
        # sorry joe :( I thought about it again and I believe hashmap is actually better
        # since the math way right after the user input will always run even when if the user inputs
        # concede or restart, which makes the math operations unnecessary for those edge cases

        valid_cords = {
            "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7,
            "1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0
        }
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

            #invalid coordinates
            elif (len(user_input) != 2
                  or user_input[1] not in valid_cords
                  or user_input[0] not in valid_cords):
                print("invalid coordinate. pick a valid coordinate")

            #valid coordinates but if not one of the player's piece, therefore not his color, return error
            elif not self.board.same_color(valid_cords[user_input[1]], valid_cords[user_input[0]], player_color):
                print("invalid. pick a piece with your color")

            else:
                print("valid move")
            # board.getpiece at this location, get canMove list,
            # if canMove list is empty, invalid move
            # request another input for move, it must be contained in the canMove list
            # set piece to move
            # once moves changes color to black and so on





