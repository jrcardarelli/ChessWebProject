from backend.board import Board
class Game:
    def __init__(self):
        self.new_board()
        self.repl()

    def new_board(self):
        self.board = Board()
        self.board.print()

    def repl(self):
        valid_x_cords = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        valid_y_cords = ['1', '2', '3', '4', '5', '6', '7', '8']
        white = True
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

                #todo white or black player also not none
                print ("invalid piece. pick a valid piece")
            else:
                print("valid move")
            # board.getpiece at this location, get canMove list,
            # request another input for move, it must be contained in the canMove list
            # set piece to move
            # once moves white = !white




