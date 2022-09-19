import pygame
import Consts
import Screen


"""
This function will place the soldier on surface (day/night/dead - type of soldier)
with the given coordinates.
:param cords_tuple: the coordinates to the soldier
:param soldier_type: the type of the soldier
:type cords_tuple: tuple
:type soldier_type: list
"""


def place_soldier(cords_tuple, solider_type="day"):
    if solider_type == "day":
        soldier_img = pygame.image.load("png files/soldier.png")
    elif solider_type == "night":
        soldier_img = pygame.image.load("png files/soldier_nigth.png")
    elif solider_type == "dead":
        soldier_img = pygame.image.load("png files/injury.png")

    soldier_img = pygame.transform.scale(soldier_img, (Consts.SIZE * 2, Consts.SIZE * 4))
    Screen.screen.blit(soldier_img, cords_tuple)


"""
This function will move the soldier on surface with the given coordinates.
:param soldier_x_location: the x coordinate of the soldier
:param soldier_y_location: the y coordinate of the soldier
:param key: the arrow key that was pressed on keyboard
:type soldier_x_location: int
:type soldier_y_location: int
:type key: int
:return soldier_x_location: the new x coordinate of the soldier
:return soldier_y_location: the new x coordinate of the soldier
:rtype soldier_x_location: int
:rtype soldier_y_location: int
"""


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
