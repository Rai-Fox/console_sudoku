from src.Utility import *


class GameSession:
    def __init__(self):
        self.field = None
        self.answer_field = None
        self.missed_cells = 0
        self.count_mistakes = 0

    def create_new_session(self, number_hints):
        self.field, self.answer_field = generate_field(Field.SIZE * Field.SIZE - number_hints)
        self.missed_cells = 0
        self.count_mistakes = 0
