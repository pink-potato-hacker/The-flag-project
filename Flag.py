import pygame
import Consts
import Screen


def placing_flag():
    flag_img = pygame.image.load("png files/flag.png").convert_alpha()
    flag_img = pygame.transform.scale(flag_img, (Consts.SIZE * 2, Consts.SIZE * 4))
    Screen.screen.blit(flag_img, (1200, 525))
