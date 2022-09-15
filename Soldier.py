import Consts
import Screen
import pygame

def placing_soldier(coords_tuple):
    soldier_img = pygame.image.load("png files/soldier.png").convert_alpha()
    soldier_img = pygame.transform.scale(soldier_img, (Consts.SIZE * 3.5, Consts.SIZE * 3.5))
    Screen.screen.blit(soldier_img, coords_tuple)

def moving_soldier(soldier_x_location, soldier_y_location):
    while True:
        key_input = pygame.key.get_pressed()
        if key_input[pygame.K_LEFT]:
            soldier_x_location -= Consts.SIZE
            if soldier_x_location - Consts.SIZE < -Consts.SIZE:
                soldier_x_location += Consts.SIZE
        elif key_input[pygame.K_UP]:
            soldier_y_location -= Consts.SIZE
            if soldier_y_location - Consts.SIZE < -Consts.SIZE:
                soldier_y_location += Consts.SIZE
        elif key_input[pygame.K_RIGHT]:
            soldier_x_location += Consts.SIZE
            if soldier_x_location + Consts.SIZE > Consts.NUMBER_OF_COLUMNS * Consts.SIZE - Consts.SIZE:
                soldier_x_location -= Consts.SIZE
        elif key_input[pygame.K_DOWN]:
            soldier_y_location += Consts.SIZE
            if soldier_y_location + Consts.SIZE > Consts.NUMBER_OF_ROWS * Consts.SIZE - Consts.SIZE * 3:
                soldier_y_location -= Consts.SIZE
        return ((soldier_x_location, soldier_y_location))
