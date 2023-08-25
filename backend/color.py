from enum import Enum


# class syntax
class Color(Enum):
    WHITE = -1
    BLACK = 1


# functional syntax
Color = Enum('Color', ['WHITE', 'BLACK'])
