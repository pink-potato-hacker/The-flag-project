import Consts
import Screen
import pygame

def placing_soldier(coords_tuple):
    soldier_img = pygame.image.load("png files/soldier.png").convert()
    soldier_img = pygame.transform.scale(soldier_img, (Consts.SIZE * 2, Consts.SIZE * 4))
    screen.blit(soldier_img, coords_tuple)
