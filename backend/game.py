from backend.board import Board
class Game:
    def __init__(self):
        self.board = Board()
        self.print()
        self.start()

    #start game for white to start typing cords

    def print(self):
        for row in self.board:
            for element in row:
                print(element, end=" ")
            print()  # Move to the next line after each row



    def start(self):
        while(True):
            user_input = input(">>> ")
            if user_input.lower() == 'concede':
                print("lost")
                break
            elif user_input.lower().length() != 2 or user_input.lower().charAt(0) != abcdefgh or
                user_input.lower().charAt(1) != 01234567):
                print ("invalid move")

            elif user_input.lower().charAt()



