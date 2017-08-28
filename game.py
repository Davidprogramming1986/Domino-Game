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

count = 0


grid.init_grid_numbers()


print(grid.grid_numbers)

while not game_over:

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    mouse = pygame.mouse.get_pos()
    defs.mouse_x = mouse[0]
    defs.mouse_y = mouse[1]

    # Logic


    # Graphics
    display.fill(colors.WHITE)

    grid.render_grid()

    # checks collisions
    for rect in grid.grid:
        if rect.collidepoint(defs.mouse_x, defs.mouse_y):
            grid.square_highlight(rect)
            break


    pygame.display.flip()
    clock.tick(defs.FPS)

pygame.quit()
