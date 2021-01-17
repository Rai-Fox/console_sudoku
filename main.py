from src.Game import Game
from src.player.HumanPlayer import HumanPlayer
from src.player.RandomPlayer import RandomPlayer
import sys

players = {'human': HumanPlayer(),
           'random': RandomPlayer()}

if len(sys.argv) > 1 and sys.argv[1] in players:
    game = Game(players[sys.argv[1]])
    game.run_game()
else:
    print(f'Please, enter player as the first argument (possible players: {list(players.keys())})')
