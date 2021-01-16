from src.Utility import *
from src.MenuService import *

class Game:
    def __init__(self, player):
        self.__state = GameState.idle
        self.__player = player
        self.__field = None
        self.__answer_field = None

    def run_game(self):
        while True:
            if self.__state is GameState.exiting:
                return

            while self.__state == GameState.idle:
                self.__main_menu_handler()

            while self.__state == GameState.starting_game:
                self.__starting_game_handler()

    def __main_menu_handler(self):
        print_main_menu()
        option = get_main_menu_input()
        if option is None:
            return
        if option is MainMenuOption.exit:
            self.__state = GameState.exiting
            return
        if option is MainMenuOption.new_game:
            self.__state = GameState.starting_game

    def __starting_game_handler(self):
        print_starting_game_menu()
        number_hints = get_starting_game_input()
        if number_hints is None:
            return
        self.__field, self.__answer_field = generate_field(Field.SIZE * Field.SIZE - number_hints)
        self.__state = GameState.running


class GameState(Enum):
    idle = 1
    starting_game = 2
    running = 3
    exiting = 4
