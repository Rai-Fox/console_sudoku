from src.player.BasePlayer import BasePlayer
from src.MenuService import get_making_move_input

class HumanPlayer(BasePlayer):
    def make_move(self, field):
        return get_making_move_input()