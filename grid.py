import pygame
import defs
import colors
import random

pygame.init()

class Grid():

    def __init__(self):
        self.x = defs.width * defs.x_grid_gap
        self.y = defs.height * defs.y_grid_gap
        self.square_len = defs.grid_square_len
        self.width = self.square_len * defs.x_grid_squares
        self.height = self.square_len * defs.y_grid_squares
        self.dominos = defs.dominos[:]
        self.grid_numbers = []
        self.grid = []
        self.false_value = 8

    def grid_number_place(self, domino1, domino2):

        # random chance to place the domino vertically or horizontally
        x_or_y = random.randrange(0, 2)

        for row in range(len(self.grid_numbers)):
            for square in range(len(self.grid_numbers[row])):
                if self.grid_numbers[row][square] == self.false_value:
                    self.grid_numbers[row][square] = domino1
                    if row == defs.y_grid_squares - 1 and self.grid_numbers[row][square + 1] == self.false_value or self.grid_numbers[row + 1][square] != self.false_value:
                        self.grid_numbers[row][square + 1] = domino2
                        return
                    if square == defs.x_grid_squares - 1 and self.grid_numbers[row + 1][square] == self.false_value or self.grid_numbers[row][square + 1] != self.false_value:
                        self.grid_numbers[row + 1][square] = domino2
                        return
                    if x_or_y == 0 and self.grid_numbers[row][square + 1] == self.false_value:
                        self.grid_numbers[row][square + 1] = domino2
                        return
                    if x_or_y == 1 and self.grid_numbers[row + 1][square] == self.false_value:
                        self.grid_numbers[row + 1][square] = domino2
                        return
                    else:
                        return False

    def init_grid_numbers(self):
        # Fill with false values
        for y in range(defs.y_grid_squares):
            row = []
            for x in range(defs.x_grid_squares):
                row.append(self.false_value)

            self.grid_numbers.append(row)

        # Places dominos in grid
        for n in range(len(self.dominos)):
            random_index = random.randrange(0, len(self.dominos))
            domino = self.dominos.pop(random_index)
            domino1 = domino[0]
            domino2 = domino[1]

            # random chance to invert the domino
            invert = random.randrange(0, 2)
            if invert == 1:
                domino1 = domino[1]
                domino2 = domino[0]

            self.grid_number_place(domino1, domino2)

    def render_grid(self):
        pygame.draw.rect(defs.display, colors.BLACK, (self.x - 1, self.y - 1 , self.width + 2, self.height + 2), 1)
        for y in range(defs.y_grid_squares):
            for x in range(defs.x_grid_squares):
                pygame.draw.rect(defs.display, colors.BLACK, (self.x + (self.square_len * x), self.y + (self.square_len * y), self.square_len, self.square_len), 1)
                self.grid.append(pygame.Rect(self.x + (self.square_len * x), self.y + (self.square_len * y), self.square_len, self.square_len))

    def square_highlight(self, rect):
        pygame.draw.rect(defs.display, colors.YELLOW, (rect))
