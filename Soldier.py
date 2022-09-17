import Consts
import Screen
import pygame

def placing_day_soldier(cords_tuple):
    soldier_day_img = pygame.image.load("png files/soldier.png")
    soldier_day_img = pygame.transform.scale(soldier_day_img, (Consts.SIZE * 2, Consts.SIZE * 4))
    Screen.screen.blit(soldier_day_img, cords_tuple)


def placing_night_soldier(cords_tuple):
    soldier_img = pygame.image.load("png files/soldier_nigth.png")
    soldier_img = pygame.transform.scale(soldier_img, (Consts.SIZE * 2, Consts.SIZE * 4))
    Screen.screen.blit(soldier_img, cords_tuple)


def placing_dead_solider(cords_tuple):
    dead_img = pygame.image.load("png files/injury.png")
    dead_img = pygame.transform.scale(dead_img, (Consts.SIZE * 2, Consts.SIZE * 4))
    Screen.screen.blit(dead_img, cords_tuple)


def moving_soldier(soldier_x_location, soldier_y_location, key):
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
