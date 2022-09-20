import Consts
import pygame
import Screen

guard_locations = []
import main


def place_guard(cords_tuple, guard_type='right'):
    if guard_type == "right":
        guard_img = pygame.image.load("png files/guardleft.png")
    elif guard_type == "left":
        guard_img = pygame.image.load("png files/guardright.png")

    guard_img = pygame.transform.scale(guard_img, (Consts.SIZE * 2, Consts.SIZE * 4))
    Screen.screen.blit(guard_img, cords_tuple)


def move_guard(guard_x,guard_type):
    if guard_type == 'left':
        guard_x += Consts.SIZE
        if guard_x + Consts.SIZE < -Consts.SIZE:
            guard_x -= Consts.SIZE
    elif guard_type == 'right':
        guard_x -= Consts.SIZE
        if guard_x - Consts.SIZE < -Consts.SIZE:
            guard_x += Consts.SIZE
    return guard_x


