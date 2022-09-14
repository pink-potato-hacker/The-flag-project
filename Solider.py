import pygame
import Consts
import Screen

solider = pygame.image.load('png files/soldier.png')

Screen.screen(solider, Consts.SOLIDER_STARTING_PLACE)
pygame.display.update()