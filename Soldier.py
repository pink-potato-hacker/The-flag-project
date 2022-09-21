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
        capybara_img = pygame.image.load("png files/daycapybara.png")
    elif solider_type == "night":
        capybara_img = pygame.image.load("png files/nightcapybara.png")
    elif solider_type == "dead":
        capybara_img = pygame.image.load("png files/deadcapybara.png")

    capybara_img = pygame.transform.scale(capybara_img, (Consts.SIZE * 4, Consts.SIZE * 4))
    Screen.screen.blit(capybara_img, cords_tuple)

