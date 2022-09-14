import pygame
import time
import MineField
import Consts

screen = pygame.display.set_mode((Consts.NUMBER_OF_COLUMNS * Consts.SIZE, Consts.NUMBER_OF_ROWS * Consts.SIZE))

# dark_surface
# light_surface
# soldier_flag_surface
solider_location = (0,0)
def create_light_surface():
    # Set the screen size
    size = (Consts.SIZE * Consts.NUMBER_OF_COLUMNS, Consts.SIZE * Consts.NUMBER_OF_ROWS)
    light_surface = pygame.Surface(size)
    light_surface = pygame.display.set_mode(size)
    pygame.draw.rect(light_surface, Consts.BACKGROUND_LIGHT_COLOR, pygame.Rect(0, 0, Consts.SIZE * Consts.NUMBER_OF_COLUMNS, Consts.SIZE * Consts.NUMBER_OF_ROWS))
    soldier_img = pygame.image.load("png files/fat_green_soldier.png").convert()
    soldier_img = pygame.transform.scale(soldier_img, (Consts.SIZE * 2, Consts.SIZE * 4))
    light_surface.blit(soldier_img, solider_location)
    pygame.display.update()
    flag_img = pygame.image.load("png files/fat_green_flag.png").convert()
    flag_img = pygame.transform.scale(flag_img, (Consts.SIZE * 2, Consts.SIZE * 4))
    light_surface.blit(flag_img, (1200, 525))
    pygame.display.update()
    grass_img = pygame.image.load("png files/grass.png").convert_alpha()
    grass_img = pygame.transform.scale(grass_img, (Consts.SIZE * 2, Consts.SIZE * 3))

    for grass_index in range(20):
        screen.blit(grass_img, MineField.grass[grass_index])

    pygame.display.flip()
    pygame.display.update()

    while True:
        # Wait for events
        for event in pygame.event.get():
            # if user wants to QUIT, close pygame
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    create_dark_surface()

def create_dark_surface():
    # Set the screen size
    size = (Consts.SIZE * Consts.NUMBER_OF_COLUMNS, Consts.SIZE * Consts.NUMBER_OF_ROWS)
    dark_surface = pygame.Surface(size)
    dark_surface = pygame.display.set_mode(size)
    pygame.draw.rect(dark_surface, Consts.GRID_COLOR, pygame.Rect(0, 0, Consts.SIZE * Consts.NUMBER_OF_COLUMNS, Consts.SIZE * Consts.NUMBER_OF_ROWS))
    pygame.display.flip()
    pygame.display.update()
    # Create zeros matrix
    matrix = [[0 for x in range(Consts.NUMBER_OF_COLUMNS)] for y in range(Consts.NUMBER_OF_ROWS)]
    fill_colors(matrix)
    soldier_img = pygame.image.load("png files/fat_night_soldier.png").convert()
    soldier_img = pygame.transform.scale(soldier_img, (Consts.SIZE * 2, Consts.SIZE * 4))
    dark_surface.blit(soldier_img, solider_location)
    pygame.display.update()
    flag_img = pygame.image.load("png files/fat_night_flag.png").convert()
    flag_img = pygame.transform.scale(flag_img, (Consts.SIZE * 2, Consts.SIZE * 4))
    dark_surface.blit(flag_img, (1200, 525))
    pygame.display.update()
    mine_img = pygame.image.load("png files/mine.png").convert_alpha()
    mine_img = pygame.transform.scale(mine_img, (Consts.SIZE * Consts.MINES_SIZE[1], Consts.SIZE * Consts.MINES_SIZE[0]))

    for mine_index in range(20):
        x = MineField.mines[mine_index][1] * Consts.SIZE
        y = MineField.mines[mine_index][0] * Consts.SIZE
        screen.blit(mine_img, (x, y))

    pygame.display.flip()
    pygame.display.update()

    start_time = time.time()

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        # Wait for events
        for event in pygame.event.get():
            # if user wants to QUIT, close pygame
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if elapsed_time > 1:
                create_light_surface()

def fill_colors(matrix):
    # run over all the cells in the current matrix
    for i in range(Consts.NUMBER_OF_ROWS):
        for j in range(Consts.NUMBER_OF_COLUMNS):
            color = Consts.BACKGROUND_DARK_COLOR
            pygame.draw.rect(screen, color, (j * Consts.SIZE, i * Consts.SIZE, Consts.SIZE - 1, Consts.SIZE - 1))
    pygame.display.update()

pygame.init()

create_light_surface()
