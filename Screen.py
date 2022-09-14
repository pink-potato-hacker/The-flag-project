
import pygame
import Consts


def fill_colors(matrix, screen):
    # run over all the cells in the current matrix
    for i in range(Consts.NUMBER_OF_ROWS):
        for j in range(Consts.NUMBER_OF_COLUMNS):
            color = Consts.BACKGROUND_COLOR
            pygame.draw.rect(screen, color, (j * Consts.SIZE, i * Consts.SIZE, Consts.SIZE - 1, Consts.SIZE - 1))
    pygame.display.update()
def create_board():
    pygame.init()
    # Set the screen size
    screen = pygame.display.set_mode((Consts.NUMBER_OF_COLUMNS * Consts.SIZE, Consts.NUMBER_OF_ROWS * Consts.SIZE))
    pygame.display.flip()
    pygame.display.update()
    # Create zeros matrix
    matrix = [[0 for x in range(Consts.NUMBER_OF_COLUMNS)] for y in range(Consts.NUMBER_OF_ROWS)]
    fill_colors(matrix, screen)

    while True:
        # Wait for events
        for event in pygame.event.get():
            # if user wants to QUIT, close pygame
            if event.type == pygame.QUIT:
                pygame.quit()
                return

create_board()