import pygame
import time
import MineField
import Consts

screen = pygame.display.set_mode((Consts.NUMBER_OF_COLUMNS * Consts.SIZE, Consts.NUMBER_OF_ROWS * Consts.SIZE))

# dark_surface
# light_surface
# soldier_flag_surface

def create_light_surface():
    # Set the screen size
    size = (Consts.SIZE * Consts.NUMBER_OF_COLUMNS, Consts.SIZE * Consts.NUMBER_OF_ROWS)
    light_surface = pygame.Surface(size)
    light_surface = pygame.display.set_mode(size)
    pygame.draw.rect(light_surface, Consts.BACKGROUND_LIGHT_COLOR,
                     pygame.Rect(0, 0, Consts.SIZE * Consts.NUMBER_OF_COLUMNS, Consts.SIZE * Consts.NUMBER_OF_ROWS))

    grass_img = pygame.image.load("png files/grass.png").convert_alpha()
    grass_img = pygame.transform.scale(grass_img, (Consts.SIZE * 2, Consts.SIZE * 3))

    for grass_index in range(20):
        screen.blit(grass_img, MineField.grass[grass_index])

    flag_img = pygame.image.load("png files/flag.png").convert_alpha()
    flag_img = pygame.transform.scale(flag_img, (Consts.SIZE * 4, Consts.SIZE * 3))
    screen.blit(flag_img, (Consts.NUMBER_OF_COLUMNS * Consts.SIZE - 4 * Consts.SIZE, Consts.NUMBER_OF_ROWS * Consts.SIZE - 3 * Consts.SIZE))


def create_dark_surface():
    # Set the screen size
    size = (Consts.SIZE * Consts.NUMBER_OF_COLUMNS, Consts.SIZE * Consts.NUMBER_OF_ROWS)
    dark_surface = pygame.Surface(size)
    dark_surface = pygame.display.set_mode(size)
    pygame.draw.rect(dark_surface, Consts.GRID_COLOR,
                     pygame.Rect(0, 0, Consts.SIZE * Consts.NUMBER_OF_COLUMNS, Consts.SIZE * Consts.NUMBER_OF_ROWS))

    # Create zeros matrix
    matrix = [[0 for x in range(Consts.NUMBER_OF_COLUMNS)] for y in range(Consts.NUMBER_OF_ROWS)]
    fill_colors(matrix)

    mine_img = pygame.image.load("png files/mine.png").convert_alpha()
    mine_img = pygame.transform.scale(mine_img,
                                      (Consts.SIZE * Consts.MINES_SIZE[1], Consts.SIZE * Consts.MINES_SIZE[0]))

    for mine_index in range(20):
        x = MineField.mines[mine_index][1] * Consts.SIZE
        y = MineField.mines[mine_index][0] * Consts.SIZE
        screen.blit(mine_img, (x, y))

    flag_img = pygame.image.load("png files/flag.png").convert_alpha()
    flag_img = pygame.transform.scale(flag_img, (Consts.SIZE * 4, Consts.SIZE * 3))
    screen.blit(flag_img, (Consts.NUMBER_OF_COLUMNS * Consts.SIZE - 4 * Consts.SIZE, Consts.NUMBER_OF_ROWS * Consts.SIZE - 3 * Consts.SIZE))


def fill_colors(matrix):
    # run over all the cells in the current matrix
    for i in range(Consts.NUMBER_OF_ROWS):
        for j in range(Consts.NUMBER_OF_COLUMNS):
            color = Consts.BACKGROUND_DARK_COLOR
            pygame.draw.rect(screen, color, (j * Consts.SIZE, i * Consts.SIZE, Consts.SIZE - 1, Consts.SIZE - 1))


pygame.init()

create_light_surface()