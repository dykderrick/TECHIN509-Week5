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
