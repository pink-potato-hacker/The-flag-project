import pygame
import Consts
def solider():
    screen_size = pygame.display.set_mode((600, 600))
    soldier_img = pygame.image.load("png files/soldier.png").convert()
    soldier_img = pygame.transform.scale(soldier_img,(Consts.SIZE * 2,Consts.SIZE * 4))
    screen_size.blit(soldier_img, (0, 0))
    pygame.display.flip()
    status = True
    while (status):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                status = False
