import MineField
import pygame
import time


def key_press_timer():
    running = True
    clock = pygame.time.Clock()
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
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                for i, key in enumerate(keys):
                    if event.key == key:
                        counters[i] = time.time()
            if event.type == pygame.KEYUP:
                for i, key in enumerate(keys):
                    if event.key == key:
                        counters[i] = time.time() - counters[i]
                        times[i] += counters[i]
                        key_press_time_ms = int(1000 * counters[i])
                        key_pressed = i+1
            clock.tick(60)
    return (key_pressed,key_press_time_ms)

#key_press_time_ms is time of pressing on event.key in milliseconds


key_pressed = key_press_timer()
#less than sec save the game
save_files = {}


def add_elements_to_file():
    if key_pressed % 1 == 0:
        save_files[key_pressed - 0.5] = [MineField.mines,
                                         MineField.flowers,
                                         MineField.bushes,
                                         MineField.grass,
                                         MineField.get_soldier_location()]

