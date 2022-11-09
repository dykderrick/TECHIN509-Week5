from typing import List


def validate_game_mode_input(user_input: str) -> bool:
    try:
        game_mode = int(user_input)
    except ValueError:
        return False

    return game_mode == 1 or game_mode == 2


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
