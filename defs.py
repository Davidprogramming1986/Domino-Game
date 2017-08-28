import pygame
pygame.init()

FPS = 60

display = pygame.display.Info()
width = display.current_w
height = display.current_h

display = pygame.display.set_mode((width, height))

mouse_x = 0
mouse_y = 0

# Sets grid width to percentage of screen
grid_width = 0.4
x_grid_gap = 0.1
y_grid_gap = 0.15
x_grid_squares = 8
y_grid_squares = 7
grid_square_len = (width * grid_width) / x_grid_squares

# Dominos

dominos = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6],
          [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6],
          [2, 2], [2, 3], [2, 4], [2, 5], [2, 6],
          [3, 3], [3, 4], [3, 5], [3, 6],
          [4, 4], [4, 5], [4, 6],
          [5, 5], [5, 6],
          [6, 6]]
