from sudoku import Sudoku
import numpy as np

sudoku_board = np.array([[0, 0, 0, 0, 6, 4, 0, 3, 9],
                         [3, 0, 0, 0, 8, 9, 7, 0, 0],
                         [0, 7, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 5, 4, 0, 3, 9, 8, 7],
                         [7, 9, 0, 6, 5, 8, 2, 0, 1],
                         [0, 4, 0, 0, 0, 7, 3, 0, 0],
                         [0, 2, 4, 8, 0, 0, 0, 0, 0],
                         [0, 3, 0, 1, 0, 2, 6, 9, 8],
                         [6, 0, 0, 3, 0, 5, 0, 0, 0]])
sudoku = Sudoku(sudoku_board)

print(sudoku.get_og_values())
