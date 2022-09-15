import pygame
import MineField
import Consts
import main

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

    flower_img = pygame.image.load("png files/flower.png").convert_alpha()
    flower_img = pygame.transform.scale(flower_img, (Consts.SIZE * 2, Consts.SIZE * 3))

    for flower_index in range(10):
        screen.blit(flower_img, MineField.flower[flower_index])

    flag_img = pygame.image.load("png files/flag.png").convert_alpha()
    flag_img = pygame.transform.scale(flag_img, (Consts.SIZE * 4, Consts.SIZE * 3))
    screen.blit(flag_img, (
        Consts.NUMBER_OF_COLUMNS * Consts.SIZE - 4 * Consts.SIZE,
        Consts.NUMBER_OF_ROWS * Consts.SIZE - 3 * Consts.SIZE))


def welcome_text():
    font = pygame.font.SysFont(Consts.WELCOME_MESSAGE1, 35)
    text1 = font.render(Consts.WELCOME_MESSAGE1, True, Consts.TEXT_COLOR)
    text2 = font.render(Consts.WELCOME_MESSAGE2, True, Consts.TEXT_COLOR)

    screen.blit(text1, (Consts.NUMBER_OF_COLUMNS * Consts.SIZE / 3, 0))
    screen.blit(text2, (Consts.NUMBER_OF_COLUMNS * Consts.SIZE / 3 + 100, 35))

    pygame.display.flip()
    pygame.display.update()


def lose_text():
    font = pygame.font.SysFont(Consts.LOSE_MESSAGE, 100)
    lose_text = font.render(Consts.LOSE_MESSAGE, True, Consts.TEXT_COLOR)
    screen.blit(lose_text, (500, 250))
    pygame.display.flip()
    pygame.display.update()


def win_text():
    font = pygame.font.SysFont(Consts.WIN_MESSAGE, 100)
    win_text = font.render(Consts.WIN_MESSAGE, True, Consts.TEXT_COLOR)
    screen.blit(win_text, (500, 250))
    pygame.display.flip()
    pygame.display.update()


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
    screen.blit(flag_img, (
        Consts.NUMBER_OF_COLUMNS * Consts.SIZE - 4 * Consts.SIZE,
        Consts.NUMBER_OF_ROWS * Consts.SIZE - 3 * Consts.SIZE))


def fill_colors(matrix):
    # run over all the cells in the current matrix
    for i in range(Consts.NUMBER_OF_ROWS):
        for j in range(Consts.NUMBER_OF_COLUMNS):
            color = Consts.BACKGROUND_DARK_COLOR
            pygame.draw.rect(screen, color, (j * Consts.SIZE, i * Consts.SIZE, Consts.SIZE - 1, Consts.SIZE - 1))

def show_boom(cords_tuple):
    boom_img = pygame.image.load("png files/boom.png").convert_alpha()
    boom_img = pygame.transform.scale(boom_img, (Consts.SIZE * 4, Consts.SIZE * 4))
    screen.blit(boom_img, cords_tuple)

pygame.init()
