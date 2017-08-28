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

def init_grid_numbers():
    for n in range(50):
        print(n)
        try:
            grid.init_grid_numbers()
        except IndexError:
            continue
        break

init_grid_numbers()

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

    for n in range(56):
        display.blit(defs.grid_value_font.render('Test', True, colors.BLACK), (n, 500))

    grid.render_grid()

    # checks collisions
    for rect in grid.grid:
        if rect.collidepoint(defs.mouse_x, defs.mouse_y):
            grid.square_highlight(rect)
            break


    pygame.display.flip()
    clock.tick(defs.FPS)

pygame.quit()
