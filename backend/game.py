from backend.board import Board
class Game:
    def __init__(self):
        self.new_board()
        self.repl()

    def new_board(self):
        self.board = Board()
        self.board.print()

    def repl(self):
        valid_x_cords = ["a", "b", "c", "d", "e", "f", "g", "h"]
        valid_y_cords = [1, 2, 3, 4, 5, 6, 7, 8]
        while(True):
            user_input = input(">>> ").lower()

            if user_input == 'concede':
                print("lost")
                break
            elif user_input == 'restart':
                print("restarted")
                self.new_board()

            elif (len(user_input) != 2
                  or user_input[0] not in valid_x_cords
                  or user_input[1] not in valid_y_cords):
                print ("invalid piece")
            else
            # board.getpiece at this location, print eligible moves and attack list,
            # request another input for move, it must be contained in the eligible moves and attack list
            # set piece to move or attack




