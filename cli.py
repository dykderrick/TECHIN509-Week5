# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from typing import List, Tuple
from logic import make_empty_board, other_player, get_winner
import random


class Game:
    def __init__(self):
        self.game_mode = 0  # 1 means one-gamer (user vs bot), 2 means two-player (user vs user)
        self.board = make_empty_board()
        self.players = ["X", other_player("X")]
        self.winner = None

    def get_board(self):
        return self.board

    def get_winner(self):
        return self.winner

    def game_interface(self):
        pass


class SingleModeGame(Game):
    def __init__(self):
        super().__init__()
        self.is_user_turn = True

    def _get_empty_space(self):
        space = []

        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    space.append((i, j))

        return space

    def bot_random_step(self) -> Tuple:
        _empty_space = self._get_empty_space()

        return _empty_space[random.randint(0, len(_empty_space) - 1)]

    def game_interface(self):
        while self.winner is None:
            if not self.is_user_turn:
                print("Bot takes a turn!")

                bot_step = self.bot_random_step()

                print("Bot takes " + str(bot_step))

                self.board[bot_step[0]][bot_step[1]] = "O"  # bot always takes O

            else:
                print("Player takes a turn!")

                # Show the board to the user.
                print("CURRENT BOARD: ")
                BoardPrinter(self.board).print_board()

                # Input a move from the player.
                valid_input = False
                _x, _y = "", ""

                while not valid_input:
                    _x = input("Enter Coordinate For Row (zero-index): ")
                    _y = input("Enter Coordinate For Col (zero-index): ")

                    valid_input = validate_input(self.board, _x, _y)

                    if not valid_input:
                        print("INVALID INPUT. PLEASE RE-ENTER.")

                print("Your input is (%s, %s)" % (_x, _y))

                # Update the board.
                coordinate = (int(_x), int(_y))
                self.board[coordinate[0]][coordinate[1]] = "X"  # User always takes O

            # Print the board
            print("CURRENT BOARD: ")
            BoardPrinter(self.board).print_board()

            # Update who's turn it is.
            self.is_user_turn = not self.is_user_turn

            self.winner = get_winner(self.board)

            print("---------------------------------------")

        if self.winner is not None:
            print("GAME OVER. " + self.winner + " WINS.")
        else:
            print("GAME OVER. DRAW.")


class TwoPlayerModeGame(Game):
    def __init__(self):
        super().__init__()
        self.current_player = "X"

    def game_interface(self):
        while self.winner is None:
            print(self.current_player + " take a turn!")

            # Show the board to the user.
            print("CURRENT BOARD: ")
            BoardPrinter(self.board).print_board()

            # Input a move from the player.
            valid_input = False
            _x, _y = "", ""

            while not valid_input:
                _x = input("Enter Coordinate For Row (zero-index): ")
                _y = input("Enter Coordinate For Col (zero-index): ")

                valid_input = validate_input(board, _x, _y)

                if not valid_input:
                    print("INVALID INPUT. PLEASE RE-ENTER.")

            print("Your input is (%s, %s)" % (_x, _y))

            # Update the board.
            coordinate = (int(_x), int(_y))
            self.board[coordinate[0]][coordinate[1]] = self.current_player

            # Print the board
            print("CURRENT BOARD: ")
            BoardPrinter(self.board).print_board()

            # Update who's turn it is.
            self.current_player = other_player(self.current_player)

            self.winner = get_winner(board)

            print("---------------------------------------")

        if self.winner is not None:
            print("GAME OVER. " + self.winner + " WINS.")
        else:
            print("GAME OVER. DRAW.")


class BoardPrinter:
    def __init__(self, board):
        self.board = board

    def print_board(self):
        for i in range(3):
            current_row = ""
            for j in range(3):
                if self.board[i][j] is not None:
                    current_row += self.board[i][j]
                else:
                    current_row += "_"

                current_row += " "

            print(current_row)


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
