import numpy as np

from my_exceptions import IndexOutOfRange

class Sudoku:
    def __init__(self):
        board = np.zeros((9, 9))

    def get_subarray(self, id):
        match id:
            case 1:
                subboard = self.board[0:3, 0:3]
            case 2:
                subboard = self.board[0:3, 3:6]
            case 3:
                subboard = self.board[0:3, 6:9]
            case 4:
                subboard = self.board[3:6, 0:3]
            case 5:
                subboard = self.board[3:6, 3:6]
            case 6:
                subboard = self.board[3:6, 6:9]
            case 7:
                subboard = self.board[6:9, 0:3]
            case 8:
                subboard = self.board[6:9, 3:6]
            case 9:
                subboard = self.board[6:9, 6:9]
            case _:
                raise IndexOutOfRange("Sudoku board has only 9 3x3 subboards")
        return subboard
    
    