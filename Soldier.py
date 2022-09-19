import Consts
import Screen
import pygame


def place_soldier(cords_tuple, solider_type="day"):
    if solider_type == "day":
        soldier_img = pygame.image.load("png files/soldier.png")
    elif solider_type == "night":
        soldier_img = pygame.image.load("png files/soldier_nigth.png")
    elif solider_type == "dead":
        soldier_img = pygame.image.load("png files/injury.png")

    soldier_img = pygame.transform.scale(soldier_img, (Consts.SIZE * 2, Consts.SIZE * 4))
    Screen.screen.blit(soldier_img, cords_tuple)


# move
def move_soldier(soldier_x_location, soldier_y_location, key):
    if key == pygame.K_LEFT:
        soldier_x_location -= Consts.SIZE
        if soldier_x_location - Consts.SIZE < -Consts.SIZE:
            soldier_x_location += Consts.SIZE

    elif key == pygame.K_UP:
        soldier_y_location -= Consts.SIZE
        if soldier_y_location - Consts.SIZE < -Consts.SIZE:
            soldier_y_location += Consts.SIZE

    elif key == pygame.K_RIGHT:
        soldier_x_location += Consts.SIZE
        if soldier_x_location + Consts.SIZE > Consts.NUMBER_OF_COLUMNS * Consts.SIZE - Consts.SIZE:
            soldier_x_location -= Consts.SIZE

    elif key == pygame.K_DOWN:
        soldier_y_location += Consts.SIZE
        if soldier_y_location + Consts.SIZE > Consts.NUMBER_OF_ROWS * Consts.SIZE - Consts.SIZE * 3:
            soldier_y_location -= Consts.SIZE
    return soldier_x_location, soldier_y_location
