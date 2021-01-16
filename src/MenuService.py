from enum import Enum
from src.GameSession import MovingResult
import os


class MainMenuOption(Enum):
    new_game = 1
    exit = 2

class InGameMenuOption(Enum):
    make_move = 1
    #save_session = 2
    exit_to_main_menu = 2


def print_main_menu():
    print("-----------Main menu-----------")
    print("Enter number of option:")
    for option in MainMenuOption:
        print(f'{option.value}) {option.name}')


def get_main_menu_input():
    try:
        return MainMenuOption(int(input()))
    except BaseException:
        print("Error! Please enter one of the options")
        os.system('pause')
        return None

def print_starting_game_menu():
    print("-----------Starting game-----------")
    print("Please, enter number of hints (from 0 to 80)")

def get_starting_game_input():
    try:
        number_hints = int(input())
        if number_hints > 80 or number_hints < 0:
            raise BaseException()
        return number_hints
    except BaseException:
        print("Error! A number from 0 to 80 expected")
        os.system('pause')
        return None

def print_ingame_menu():
    print("-----------In-game menu-----------")
    print("Enter number of option:")
    for option in InGameMenuOption:
        print(f'{option.value}) {option.name}')

def get_ingame_menu_input():
    try:
        return InGameMenuOption(int(input()))
    except BaseException:
        print("Error! Please, enter one of the options")
        os.system('pause')
        return None

def print_making_move_menu():
    print("Please, enter three numbers by spaces: [row] [column] [the number you want to insert]")

def get_making_move_input():
    try:
        row, column, digit = map(int, input().split())
        if row is None or column is None or digit is None or \
                row < 1 or row > 9 or column < 1 or column > 9 or digit < 1 or digit > 9:
            raise BaseException()
        return row - 1, column - 1, digit
    except BaseException:
        print("Error! Please, enter three numbers by spaces")
        os.system('pause')
        return None, None, None

def print_moving_result(result):
    if result == MovingResult.successful:
        print("This move was successful")
    elif result == MovingResult.fail:
        print("There must be another number in this cell")
    elif result == MovingResult.already_filled:
        print("Error! This cell is already filled")
    elif result == MovingResult.win:
        print("Congratulations, you successfully solved this")
    os.system('pause')
