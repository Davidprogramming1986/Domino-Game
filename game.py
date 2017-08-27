import pygame
import colors
import defs
import grid



pygame.init()


display = defs.display

pygame.display.set_caption('Davids Domino Game')
clock = pygame.time.Clock()

game_over = False


grid = grid.Grid()



while not game_over:

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Logic


    # Graphics
    display.fill(colors.WHITE)

    grid.render_grid()

    pygame.display.flip()
