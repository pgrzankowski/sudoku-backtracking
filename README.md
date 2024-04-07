# Sudoku Solver (Backtracking)

## Introduction
This project implements a Sudoku solver using the backtracking algorithm. It features a graphical user interface (GUI) created with Pygame for users to input Sudoku puzzles and visualize the solving process.

## Dependencies
- NumPy: For efficient array operations.
- Pygame: For the graphical user interface.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
1. **Run the Solver**: Execute the `main.py` script to launch the GUI.
   ```bash
   python src/main.py
   ```

2. **Input Sudoku Puzzle**: Click on a cell and type a number to input a value.

3. **Solve the Puzzle**: Press the `Space` key to start the solver and show the solution.

## Functionality
1. **Sudoku Solver Algorithm**: Utilizes backtracking for efficient puzzle solving.
   
2. **Graphical User Interface (GUI)**: Created using Pygame, allowing intuitive interaction with the solver.

3. **Solving Animation**: Updates GUI to reflect solver progress.

4. **Performance Optimization**: Utilizes NumPy arrays for efficient handling of Sudoku grids.

## Conclusion
This project showcases the use of backtracking to solve Sudoku puzzles, complemented by a user-friendly GUI developed with Pygame. It provides an accessible platform for solving Sudoku puzzles and visualizing the solving process. Further enhancements could include additional features or optimization strategies.