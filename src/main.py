from sudoku import Sudoku
import numpy as np


def main():
    sudoku = Sudoku()
    starting_grid = np.array([[0, 0, 0, 9, 0, 0, 4, 3, 7],
                              [0, 9, 0, 0, 6, 0, 0, 1, 0],
                              [0, 1, 0, 0, 0, 7, 8, 0, 0],
                              [2, 0, 0, 5, 0, 0, 9, 0, 0],
                              [0, 5, 0, 8, 0, 0, 0, 0, 0],
                              [1, 8, 0, 0, 0, 0, 0, 6, 0],
                              [0, 0, 0, 0, 2, 4, 0, 0, 0],
                              [0, 6, 0, 0, 0, 0, 0, 8, 1],
                              [0, 0, 0, 0, 0, 0, 0, 0, 9]])
    sudoku.set_board(starting_grid)
    if sudoku.solve():
        print(sudoku)
    else:
        print("Given board is unsolvable")


if __name__ == '__main__':
    main()
