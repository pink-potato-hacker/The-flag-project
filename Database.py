import MineField
import pygame
import pandas
import os
import ast

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
curr_file = {}


def add_elements_to_file(key_and_time_key_pressed):
    global save_files
    key_pressed, time_pressed = key_and_time_key_pressed
    file_size = os.path.getsize("CSV/CSV_data.csv")

    if time_pressed <= 1:
        if file_size == 0:  # file empty
            save_files[key_pressed] = [MineField.mines,
                                       MineField.flowers,
                                       MineField.bushes,
                                       MineField.grass,
                                       MineField.get_soldier_location()]
            data_frame = pandas.DataFrame(save_files)
            data_frame.to_csv("CSV/CSV_data.csv", index=False)

        elif not check_if_header_in_csv(key_pressed):  # file doesn't contain the given header
            data_frame = pandas.read_csv("CSV/CSV_data.csv")
            data_frame.insert(key_pressed - 1, column=key_pressed, value=[MineField.mines,
                                       MineField.flowers,
                                       MineField.bushes,
                                       MineField.grass,
                                       MineField.get_soldier_location()])
            data_frame.to_csv("CSV/CSV_data.csv", index=False)

        elif check_if_header_in_csv(key_pressed):  # file contains the given header
            data_frame = pandas.read_csv("CSV/CSV_data.csv")
            data_frame.drop(str(key_pressed), inplace=True, axis=1)
            data_frame.insert(key_pressed - 1, column=str(key_pressed), value=[MineField.mines,
                                       MineField.flowers,
                                       MineField.bushes,
                                       MineField.grass,
                                       MineField.get_soldier_location()])
            data_frame.to_csv("CSV/CSV_data.csv", index=False)

    elif time_pressed > 1:
        if file_size != 0:
            data_frame = pandas.read_csv("CSV/CSV_data.csv")
            data_list = []
            for row in data_frame[str(key_pressed)]:
                data_list.append(ast.literal_eval(row))
            curr_file[key_pressed] = data_list

    print(curr_file)
    save_files = {}

def check_if_header_in_csv(header):

    header_list = pandas.read_csv("CSV/CSV_data.csv", nrows=0).columns.tolist()
    if str(header) in header_list:
        return True
    return False
