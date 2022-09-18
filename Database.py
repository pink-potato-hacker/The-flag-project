import pandas
import pygame
import MineField

save_files = {}


def key_pressed_or_held():
    while True:
        for event in pygame.event.get():
            timer = pygame.time.get_ticks()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    if (pygame.time.get_ticks() - timer) / 1000 <= 1:
                        return 1.5
                    else:
                        return 1

                if event.key == pygame.K_2:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            if (pygame.time.get_ticks() - timer) / 1000 <= 1:
                                return 2.5
                            else:
                                return 2

                if event.key == pygame.K_3:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            if (pygame.time.get_ticks() - timer) / 1000 <= 1:
                                return 3.5
                            else:
                                return 3

                if event.key == pygame.K_4:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            if (pygame.time.get_ticks() - timer) / 1000 <= 1:
                                return 4.5
                            else:
                                return 4

                if event.key == pygame.K_5:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            if (pygame.time.get_ticks() - timer) / 1000 <= 1:
                                return 5.5
                            else:
                                return 5

                if event.key == pygame.K_6:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            if (pygame.time.get_ticks() - timer) / 1000 <= 1:
                                return 6.5
                            else:
                                return 6

                if event.key == pygame.K_7:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            if (pygame.time.get_ticks() - timer) / 1000 <= 1:
                                return 7.5
                            else:
                                return 7

                if event.key == pygame.K_8:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            if (pygame.time.get_ticks() - timer) / 1000 <= 1:
                                return 8.5
                            else:
                                return 8

                if event.key == pygame.K_9:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            if (pygame.time.get_ticks() - timer) / 1000 <= 1:
                                return 9.5
                            else:
                                return 9


key_pressed = key_pressed_or_held()


# less than sec save the game

def add_elements_to_file():
    if key_pressed % 1 == 0:
        save_files[key_pressed - 0.5] = [MineField.mines, MineField.flowers, MineField.bushes, MineField.grass]

