from src.player.BasePlayer import BasePlayer
from src.Field import Field
import random

class RandomPlayer(BasePlayer):
    def make_move(self, field):
        empty_cells = []
        for i in range(Field.SIZE):
            for j in range(Field.SIZE):
                if field.cells[i][j] == '.':
                    empty_cells.append((i, j))
        row, column = random.sample(empty_cells, k=1)[0]
        digit = random.randint(1, 9)
        print(row, column, digit)
        return row, column, digit
