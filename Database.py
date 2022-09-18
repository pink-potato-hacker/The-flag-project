import MineField
import pygame
import time
import pandas


def key_press_timer():
    running = True
    clock = pygame.time.get_ticks()
    keys = [
        pygame.K_1,
        pygame.K_2,
        pygame.K_3,
        pygame.K_4,
        pygame.K_5,
        pygame.K_6,
        pygame.K_7,
        pygame.K_8,
        pygame.K_9,
    ]
    times = [0 for _ in keys]
    counters = [0 for _ in keys]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                for i, key in enumerate(keys):
                    if event.key == key:
                        counters[i] = (pygame.time.get_ticks() - clock) - counters[i]
                        times[i] += counters[i]
                        key_press_time_ms = pygame.time.get_ticks() - clock
                        key_pressed = i + 1
                        return key_pressed, key_press_time_ms // 1000


# key_press_time_ms is time of pressing on event.key in milliseconds


# less than sec save the game
save_files = {}


def add_elements_to_file(key_and_time_key_pressed):
    key_pressed, time_pressed = key_and_time_key_pressed

    if time_pressed <= 1:
        save_files[key_pressed] = [MineField.mines,
                                   MineField.flowers,
                                   MineField.bushes,
                                   MineField.grass,
                                   MineField.get_soldier_location()]

    data_frame = pandas.DataFrame(save_files)
    data_frame.to_csv("CSV/CSV_data.csv", index=False)
