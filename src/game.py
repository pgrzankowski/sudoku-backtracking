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
        self._OG_VALS = self._sudoku.get_og_values()
        self._selected_cell = (0, 0)
        pygame.display.set_caption("Sudoku")

    def draw_board(self):
        for rix, row in enumerate(self._sudoku.get_current_board()):
            for cix, value in enumerate(row):
                cellX = cix * self._CELL_SIZE
                cellY = rix * self._CELL_SIZE
                if (rix, cix) not in self._OG_VALS:
                    cell_color = (150, 150, 150)
                    if (rix, cix) == self._selected_cell:
                        cell_color = (255, 0, 0)
                    text_color = (0, 0, 0)
                else:
                    cell_color = (0, 0, 0)
                    text_color = (255, 255, 255)
                if value == 0:
                    text = self._font.render("", True, text_color)
                else:
                    text = self._font.render(str(value), True, text_color)
                rect_data = cellX, cellY, self._CELL_SIZE-5, self._CELL_SIZE-5
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
        self._OG_VALS = self._sudoku.get_og_values()

    def click_handle(self, mouse_pos):
        row = mouse_pos[1] // self._CELL_SIZE
        col = mouse_pos[0] // self._CELL_SIZE
        self._selected_cell = (row, col)

    def solve(self):
        self._sudoku.solve()

    def set_value(self, value):
        if self._selected_cell not in self._sudoku.get_og_values():
            solution = self._sudoku.get_solution()
            proper_val = self._sudoku.get_value(solution, self._selected_cell)
            if value == proper_val:
                self._sudoku.set_value(self._selected_cell, value)

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
                        self.set_value(0)
                    elif event.key == pygame.K_1:
                        self.set_value(1)
                    elif event.key == pygame.K_2:
                        self.set_value(2)
                    elif event.key == pygame.K_3:
                        self.set_value(3)
                    elif event.key == pygame.K_4:
                        self.set_value(4)
                    elif event.key == pygame.K_5:
                        self.set_value(5)
                    elif event.key == pygame.K_6:
                        self.set_value(6)
                    elif event.key == pygame.K_7:
                        self.set_value(7)
                    elif event.key == pygame.K_8:
                        self.set_value(8)
                    elif event.key == pygame.K_9:
                        self.set_value(9)
            self._screen.fill((255, 255, 255))
            self.draw_board()
            pygame.display.update()

        pygame.quit()
