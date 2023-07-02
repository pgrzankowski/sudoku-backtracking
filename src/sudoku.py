import numpy as np

from my_exceptions import (
    IndexOutOfRange,
    NotADigit,
)


class Sudoku:
    def __init__(self):
        self._board = np.zeros((9, 9), dtype=int)

    def get_subarray(self, id):
        match id:
            case 1:
                subboard = self._board[0:3, 0:3]
            case 2:
                subboard = self._board[0:3, 3:6]
            case 3:
                subboard = self._board[0:3, 6:9]
            case 4:
                subboard = self._board[3:6, 0:3]
            case 5:
                subboard = self._board[3:6, 3:6]
            case 6:
                subboard = self._board[3:6, 6:9]
            case 7:
                subboard = self._board[6:9, 0:3]
            case 8:
                subboard = self._board[6:9, 3:6]
            case 9:
                subboard = self._board[6:9, 6:9]
            case _:
                raise IndexOutOfRange("Sudoku board has only 9 3x3 subboards")
        return subboard

    def get_value(self, coordinates):
        return self._board[coordinates[0], coordinates[1]]

    def set_value(self, coordinates, value):
        if value < 1 or value > 9:
            raise NotADigit("Number must be a digit")
        else:
            self._board[coordinates[0], coordinates[1]] = value

    def set_board(self, board_to_set):
        self._board = board_to_set

    def solve(self):
        pass

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
