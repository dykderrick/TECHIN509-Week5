import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        """
        Given a given board for X to win, check if the get_winner function works.
        """
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    def test_make_empty_board(self):
        """
        Given a correct empty board, check if the make_empty_board() function works.
        """
        correct_board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

        self.assertEqual(logic.make_empty_board(), correct_board)

    def test_other_player(self):
        """
        Given a current player X, check if the other_player() function replies with a O. And check otherwise.
        """
        self.assertEqual(logic.other_player("X"), "O")
        self.assertEqual(logic.other_player("O"), "X")


if __name__ == '__main__':
    unittest.main()
