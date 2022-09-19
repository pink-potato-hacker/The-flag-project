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

