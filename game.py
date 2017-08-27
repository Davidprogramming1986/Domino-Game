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
grid.init_grid()

print(grid.grid)

while not game_over:

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    mouse = pygame.mouse.get_pos()
    defs.mouse_x = mouse[0]
    defs.mouse_y = mouse[1]

    print('x: ' + str(defs.mouse_x) + ', y: ' + str(defs.mouse_y))

    # Logic


    # Graphics
    display.fill(colors.WHITE)

    grid.render_grid()

    # checks collisions

    for square in grid.grid:
        if square.x > 

    pygame.display.flip()
    clock.tick(defs.FPS)

pygame.quit()
