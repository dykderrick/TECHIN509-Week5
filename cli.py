# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from typing import List
from game import *


def validate_input(board: List[List[str]], user_input_x: str, user_input_y: str) -> bool:
    try:
        x_coordinate = int(user_input_x)
    except ValueError:
        return False

    try:
        y_coordinate = int(user_input_y)
    except ValueError:
        return False

    return 0 <= x_coordinate <= 2 and 0 <= y_coordinate <= 2 and board[x_coordinate][y_coordinate] is None


def validate_game_mode_input(user_input: str) -> bool:
    try:
        game_mode = int(user_input)
    except ValueError:
        return False

    return game_mode == 1 or game_mode == 2


if __name__ == '__main__':
    print("Please Select a Game Mode:")
    print("1 - One Player Mode")
    print("2 - Two Player Mode")

    valid_input_game_mode = False
    _game_mode = ""

    while not valid_input_game_mode:
        _game_mode = input("Enter number: ")

        valid_input_game_mode = validate_game_mode_input(_game_mode)

        if not valid_input_game_mode:
            print("INVALID INPUT. PLEASE RE-ENTER.")

    game_mode = int(_game_mode)

    game = None

    if game_mode == 1:
        print("You are on One Player Mode")
        game = SingleModeGame()
    elif game_mode == 2:
        print("You are on Two Player Mode")
        game = TwoPlayerModeGame()

    board = game.get_board()
    winner = game.get_winner()

    current_player = "X"

    print()
    print("GAME START")
    print("---------------------------------------")

    game.game_interface()
