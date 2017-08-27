import pygame
import defs
import colors

pygame.init()

class Grid():

    def __init__(self):
        self.grid = []

    def render_grid(self):
        x = defs.width * defs.x_grid_gap
        y = defs.height * defs.y_grid_gap
        width = defs.grid_square_len * defs.x_grid_squares
        height = defs.grid_square_len * defs.y_grid_squares
        pygame.draw.rect(defs.display, colors.BLACK, (x, y, width, height), 1)

        for gap in range(defs.x_grid_squares):
            pygame.draw.line(defs.display, colors.BLACK, (x + (gap * defs.grid_square_len), y), (x + (gap * defs.grid_square_len), y + height))

        for gap in range(defs.y_grid_squares):
            pygame.draw.line(defs.display, colors.BLACK, (x, y + (gap * defs.grid_square_len)), (x + width, y + (gap * defs.grid_square_len)))
