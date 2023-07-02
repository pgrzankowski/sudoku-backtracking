from sudoku import Sudoku


def main():
    sudoku = Sudoku()
    sudoku.set_value((0, 0), 8)
    sudoku.set_value((2, 2), 3)
    print(sudoku)


if __name__ == '__main__':
    main()
