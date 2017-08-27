import pygame
pygame.init()

display = pygame.display.Info()
width = display.current_w
height = display.current_h

display = pygame.display.set_mode((width, height))

# Sets grid width to percentage of screen
grid_width = 0.4
x_grid_gap = 0.1
y_grid_gap = 0.15
x_grid_squares = 8
y_grid_squares = 7
grid_square_len = (width * grid_width) / x_grid_squares
