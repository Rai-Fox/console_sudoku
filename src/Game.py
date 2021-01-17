from src.MenuService import *
from src.GameSession import *


class GameState(Enum):
    idling = 1
    starting_game = 2
    running = 3
    exiting = 4
    making_move = 5
    saving_session = 6
    uploading_session = 7


class Game:
    handlers = {GameState.idling: 'self.main_menu_handler',
                GameState.starting_game: 'self.starting_game_handler',
                GameState.running: 'self.ingame_menu_handler',
                GameState.making_move: 'self.making_move_handler',
                GameState.uploading_session: 'self.uploading_session_handler',
                GameState.saving_session: 'self.saving_session_handler'}

    def __init__(self, player):
        self.__state = GameState.idling
        self.__player = player
        self.__game_session = GameSession()
        if not os.path.isdir("saves"):
            os.mkdir("saves")

    def run_game(self):
        while True:
            clear_console()
            if self.__state is GameState.exiting:
                return
            if self.__state in Game.handlers:
                eval(Game.handlers[self.__state])()

    def main_menu_handler(self):
        print_main_menu()
        option = get_main_menu_input()
        if option is None:
            return
        if option is MainMenuOption.exit:
            self.__state = GameState.exiting
            return
        if option is MainMenuOption.new_game:
            self.__state = GameState.starting_game
            return
        if option is MainMenuOption.upload_session:
            self.__state = GameState.uploading_session
            return

    def starting_game_handler(self):
        print_starting_game_menu()
        number_hints = get_starting_game_input()
        if number_hints is None:
            return
        self.__game_session.create_new_session(number_hints)
        self.__state = GameState.running

    def ingame_menu_handler(self):
        self.__game_session.print_information()
        print_ingame_menu()
        option = get_ingame_menu_input()
        if option is None:
            return
        if option is InGameMenuOption.exit_to_main_menu:
            self.__state = GameState.idling
            return
        if option is InGameMenuOption.make_move:
            self.__state = GameState.making_move
            return
        if option is InGameMenuOption.save_session:
            self.__state = GameState.saving_session
            return

    def making_move_handler(self):
        self.__game_session.print_information()
        print_making_move_menu()
        row, column, digit = self.__player.make_move(self.__game_session.field)
        self.__state = GameState.running
        if row is not None:
            result = self.__game_session.try_move(row, column, digit)
            print_moving_result(result)
            if result == MovingResult.win:
                self.__game_session.field.print()
                self.__state = GameState.idling

    def uploading_session_handler(self):
        print_uploading_session_menu()
        filename = get_uploading_session_menu_input()
        if filename is None:
            self.__state = GameState.idling
        if self.__game_session.load_session(filename):
            self.__state = GameState.running
        else:
            self.__state = GameState.idling

    def saving_session_handler(self):
        print_saving_session_menu()
        filename = get_saving_session_menu_input()
        if filename is None:
            self.__state = GameState.running
        self.__game_session.save_session(filename)
        self.__state = GameState.running
