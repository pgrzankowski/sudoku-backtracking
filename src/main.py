from sudoku import Sudoku


def main():
    sudoku = Sudoku()
    sudoku.set_board([[0, 0, 0, 9, 0, 0, 4, 3, 7],
                      [0, 9, 0, 0, 6, 0, 0, 1, 0],
                      [0, 1, 0, 0, 0, 7, 8, 0, 0],
                      [2, 0, 0, 5, 0, 0, 9, 0, 0],
                      [0, 5, 0, 8, 0, 0, 0, 0, 0],
                      [1, 8, 0, 0, 0, 0, 0, 6, 0],
                      [0, 0, 0, 0, 2, 4, 0, 0, 0],
                      [0, 6, 0, 0, 0, 0, 0, 8, 1],
                      [0, 0, 0, 0, 0, 0, 0, 0, 9]])
    print(sudoku)
    sudoku.solve()
    print(sudoku)


if __name__ == '__main__':
    main()
