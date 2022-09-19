import pygame
import Consts


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


"""
This function will check for how long the player presses a key (1-9).
:param key: the key that the player has pressed.
:type key: int
:return key: the key that the player has pressed.
:return (pygame.time.get_ticks() - clock) // 1000: a var that checks for how long the key was held.
:rtype key: int
:rtype (pygame.time.get_ticks() - clock) // 1000: int
"""


def key_press_timer(key):
    clock = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP and event.key == key:
                return int(chr(key)), (pygame.time.get_ticks() - clock) // 1000

