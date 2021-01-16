from src.Utility import *
from enum import Enum


class GameSession:
    def __init__(self):
        self.field = None
        self.answer_field = None
        self.empty_cells = 0
        self.count_mistakes = 0

    def create_new_session(self, number_hints):
        self.field, self.answer_field = generate_field(Field.SIZE * Field.SIZE - number_hints)
        self.empty_cells = Field.SIZE * Field.SIZE - number_hints
        self.count_mistakes = 0

    def print_information(self):
        print(f'----{self.empty_cells} empty cells left----you made {self.count_mistakes} mistakes----')
        self.field.print()

    def try_move(self, row, column, digit):
        if self.field.cells[row][column] != '.':
            return MovingResult.already_filled
        if self.answer_field.cells[row][column] == digit:
            self.empty_cells -= 1
            self.field.cells[row][column] = digit
            if self.empty_cells == 0:
                return MovingResult.win
            else:
                return MovingResult.successful
        if self.answer_field.cells[row][column] != digit:
            self.count_mistakes += 1
            return MovingResult.fail

class MovingResult(Enum):
    already_filled = 1
    successful = 2
    fail = 3
    win = 4
