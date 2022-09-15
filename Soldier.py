import Consts
import Screen
import pygame

def placing_soldier(coords_tuple):
    soldier_img = pygame.image.load("png files/soldier.png").convert_alpha()
    soldier_img = pygame.transform.scale(soldier_img, (Consts.SIZE * 2, Consts.SIZE * 4))
    Screen.screen.blit(soldier_img, coords_tuple)

def moving_soldier(soldier_x_location, soldier_y_location):
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_LEFT]:
        soldier_x_location -= Consts.SIZE
    if key_input[pygame.K_UP]:
        soldier_y_location -= Consts.SIZE
    if key_input[pygame.K_RIGHT]:
        soldier_x_location += Consts.SIZE
    if key_input[pygame.K_DOWN]:
        soldier_y_location += Consts.SIZE
    return ((soldier_x_location, soldier_y_location))
