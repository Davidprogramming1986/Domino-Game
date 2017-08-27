import pygame
import defs
import colors

pygame.init()

class Grid():

    #def __init__(self):


    def render_grid(self):
        pygame.draw.rect(defs.display, colors.BLACK, (defs.width * defs.x_grid_gap, defs.height * defs.y_grid_gap, defs.grid_square_len * defs.x_grid_squares, defs.grid_square_len * defs.y_grid_squares), 1)
