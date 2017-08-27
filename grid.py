import pygame
import defs
import colors

pygame.init()

class Grid():

    def __init__(self):
        self.x = defs.width * defs.x_grid_gap
        self.y = defs.height * defs.y_grid_gap
        self.sqaure_len = defs.grid_square_len
        self.width = self.sqaure_len * defs.x_grid_squares
        self.height = self.sqaure_len * defs.y_grid_squares
        self.grid = []
        self.false_value = 0

    def init_grid(self):
        for y in range(defs.y_grid_squares):
            for x in range(defs.x_grid_squares):
                square = {}
                square['x'] = self.x + (self.sqaure_len * x)
                square['y'] = self.y + (self.sqaure_len * y)
                square['value'] = self.false_value
                self.grid.append(square)

    def render_grid(self):
        pygame.draw.rect(defs.display, colors.BLACK, (self.x, self.y, self.width, self.height), 1)

        for gap in range(defs.x_grid_squares):
            pygame.draw.line(defs.display, colors.BLACK, (self.x + (gap * self.sqaure_len), self.y), (self.x + (gap * self.sqaure_len), self.y + self.height))

        for gap in range(defs.y_grid_squares):
            pygame.draw.line(defs.display, colors.BLACK, (self.x, self.y + (gap * self.sqaure_len)), (self.x + self.width, self.y + (gap * self.sqaure_len)))

    def square_highlight(x, y):
        pygame.draw.rect(defs.display, colors.YELLOW, (x, y, self.sqaure_len, self.sqaure_len))
