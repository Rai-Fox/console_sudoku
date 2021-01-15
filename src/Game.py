from enum import Enum
from src.FieldGenerator import generate_field

class Game:
    def __init__(self, player):
        self.state = State.idle
        self.player = player
        self.field = None
        self.answer_field = None

    def run_game(self):
        self.field, self.answer_field = generate_field(81-55)
        self.field.print()

class State(Enum):
    idle = 1
    running = 2
    game_over = 3
