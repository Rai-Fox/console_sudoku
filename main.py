from src.Game import Game
from src.player.HumanPlayer import HumanPlayer
import sys

game = Game(sys.platform, HumanPlayer())
game.run_game()
