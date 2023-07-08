import pygame
from sudoku import Sudoku
import numpy as np


class Game:

    def __init__(self):
        pygame.init()
        self._SCREEN_WIDTH = 600
        self._SCREEN_HEIGHT = 600
        self._SCREEN_SIZE = (self._SCREEN_WIDTH, self._SCREEN_HEIGHT)
        self._CELL_SIZE = self._SCREEN_WIDTH // 9
        self._screen = pygame.display.set_mode(self._SCREEN_SIZE)
        self._font = pygame.font.Font(None, 60)
        self._sudoku = Sudoku()
        self._selected_cell = (0, 0)
        pygame.display.set_caption("Sudoku")

    def draw_board(self):
        for rix, row in enumerate(self._sudoku.get_current_board()):
            for cix, value in enumerate(row):
                cellX = cix * self._CELL_SIZE
                cellY = rix * self._CELL_SIZE
                if value == 0:
                    cell_color = (150, 150, 150)
                    text = self._font.render("", True, (255, 255, 255))
                else:
                    cell_color = (0, 0, 0)
                    text = self._font.render(str(value), True, (255, 255, 255))
                rect_data = cellX, cellY, self._CELL_SIZE-5, self._CELL_SIZE-5
                slc_row, slc_col = self._selected_cell
                if rix == slc_row and cix == slc_col:
                    cell_color = (128, 0, 0)
                pygame.draw.rect(self._screen, cell_color, rect_data)
                x = cellX + self._CELL_SIZE // 2
                y = cellY + self._CELL_SIZE // 2
                text_rect = text.get_rect(center=(x, y))
                self._screen.blit(text, text_rect)

    def set_board(self):
        sudoku_board = np.array([[0, 0, 0, 0, 6, 4, 0, 3, 9],
                                 [3, 0, 0, 0, 8, 9, 7, 0, 0],
                                 [0, 7, 0, 0, 0, 0, 0, 0, 0],
                                 [0, 0, 5, 4, 0, 3, 9, 8, 7],
                                 [7, 9, 0, 6, 5, 8, 2, 0, 1],
                                 [0, 4, 0, 0, 0, 7, 3, 0, 0],
                                 [0, 2, 4, 8, 0, 0, 0, 0, 0],
                                 [0, 3, 0, 1, 0, 2, 6, 9, 8],
                                 [6, 0, 0, 3, 0, 5, 0, 0, 0]])
        self._sudoku.set_board(sudoku_board)

    def click_handle(self, mouse_pos):
        row = mouse_pos[1] // self._CELL_SIZE
        col = mouse_pos[0] // self._CELL_SIZE
        self._selected_cell = (row, col)

    def solve(self):
        self._sudoku.solve()

    def run(self):
        self.set_board()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()
                        self.click_handle(mouse_pos)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.solve()
                    elif event.key == pygame.K_0:
                        self._sudoku.set_value(self._selected_cell, 0)
                    elif event.key == pygame.K_1:
                        self._sudoku.set_value(self._selected_cell, 1)
                    elif event.key == pygame.K_2:
                        self._sudoku.set_value(self._selected_cell, 2)
                    elif event.key == pygame.K_3:
                        self._sudoku.set_value(self._selected_cell, 3)
                    elif event.key == pygame.K_4:
                        self._sudoku.set_value(self._selected_cell, 4)
                    elif event.key == pygame.K_5:
                        self._sudoku.set_value(self._selected_cell, 5)
                    elif event.key == pygame.K_6:
                        self._sudoku.set_value(self._selected_cell, 6)
                    elif event.key == pygame.K_7:
                        self._sudoku.set_value(self._selected_cell, 7)
                    elif event.key == pygame.K_8:
                        self._sudoku.set_value(self._selected_cell, 8)
                    elif event.key == pygame.K_9:
                        self._sudoku.set_value(self._selected_cell, 9)
            self._screen.fill((255, 255, 255))
            self.draw_board()
            pygame.display.update()

        pygame.quit()
