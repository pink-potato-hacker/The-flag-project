import pygame
import Consts
import Screen
import MineField

guard_locations = []


"""
This function will place the guard on surface (day/night/dead - type of soldier)
with the given coordinates.
:param cords_tuple: the coordinates to the guard
:param guard_type: the type of the guard
:type cords_tuple: tuple
:type guard_type: list
"""


def place_guard(cords_tuple, guard_type='right'):
    if guard_type == "right":
        guard_img = pygame.image.load("png files/guardleft.png")
    elif guard_type == "left":
        guard_img = pygame.image.load("png files/guardright.png")

    guard_img = pygame.transform.scale(guard_img, (Consts.SIZE * 2, Consts.SIZE * 4))
    Screen.screen.blit(guard_img, cords_tuple)


"""
This function will move the guard on surface with the given coordinates.
:param guard_x: the x coordinate of the guard
:type guard_x: int
:return guard_x: the new x coordinate of the guard
:rtype guard_x: int
"""


def move_guard(guard_x, guard_type):
    if guard_type == 'left':
        guard_x += Consts.SIZE
        if guard_x + Consts.SIZE < -Consts.SIZE:
            guard_x -= Consts.SIZE
    elif guard_type == 'right':
        guard_x -= Consts.SIZE
        if guard_x - Consts.SIZE < -Consts.SIZE:
            guard_x += Consts.SIZE

    return guard_x


"""
This function will return the current position of the guard in matrix.
:return guard_location: list of tuples of guard's position in matrix.
:rtype soldier_location: list
"""


def get_guard_location():
    guard_location = []
    for x_index in range(len(MineField.mine_field)):
        for y_index in range(len(MineField.mine_field[0])):
            if MineField.mine_field[x_index][y_index] == Consts.GUARD:
                guard_location.append((x_index, y_index))
    return guard_location


"""
This function will load a saved game.
:param saved_dict: a dictionary that contains the coordinates/indexes of these elements in order:
mines, flowers, bushes, grass, soldier locations, teleports and guard locations.
:type saved_dict: dict
"""


def load_guard(saved_dict):
    global guard_locations

    saved_list = list(saved_dict.values())
    guard_locations = saved_list[0][6]

    for guard_index in range(len(guard_locations)):
        MineField.mine_field[guard_locations[guard_index][0]][guard_locations[guard_index][1]] = Consts.GUARD
