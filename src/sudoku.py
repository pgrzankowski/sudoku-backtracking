import numpy as np

from my_exceptions import (
    # IndexOutOfRange,
    NotADigit,
)


class Sudoku:

    def __init__(self, board=np.zeros((9, 9), dtype=int)):
        self.set_board(board)

    def get_current_board(self):
        return self._board

    def get_subgrid(self, coordinates):
        start_row = (coordinates[0] // 3) * 3
        start_col = (coordinates[1] // 3) * 3
        subgrid = self._board[start_row:start_row+3, start_col:start_col+3]
        return subgrid

    def get_value(self, coordinates):
        return self._board[coordinates[0], coordinates[1]]

    def set_value(self, coordinates, value):
        if value < 0 or value > 9:
            raise NotADigit("Number must be a digit")
        else:
            self._board[coordinates[0], coordinates[1]] = value

    def set_board(self, board_to_set):
        self._board = board_to_set

    def solve(self):
        blank = self.find_blank()
        if not blank:
            return True
        else:
            for x in range(1, 10):
                if self.possible_value(x, blank):
                    self.set_value(blank, x)
                    if self.solve():
                        return True
                    self.set_value(blank, 0)
        return False

    def find_blank(self):
        for rix, row in enumerate(self._board):
            for cix, value in enumerate(row):
                if value == 0:
                    return (rix, cix)
        return None

    def possible_value(self, value, coordinates):
        # check if same value is in the row
        for x in self._board[coordinates[0]]:
            if x == value:
                return False
        # check if same value is in the column
        for x in self._board:
            if x[coordinates[1]] == value:
                return False
        # check if same value is in the 3x3 subgrid
        subgrid = self.get_subgrid(coordinates)
        for row in subgrid:
            for x in row:
                if x == value:
                    return False
        return True

    def __str__(self) -> str:
        board_ui = ''
        for i, row in enumerate(self._board):
            if i % 3 == 0 and i != 0:
                board_ui += 21 * '-' + '\n'
            for j, value in enumerate(row):
                if j % 3 == 0 and j != 0:
                    board_ui += '| '
                board_ui += str(value) + ' '
            board_ui += '\n'
        return board_ui
