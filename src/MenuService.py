from enum import Enum

class MainMenuOption(Enum):
    new_game = 1
    exit = 2

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
        return None
