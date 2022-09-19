import MineField
import pygame
import pandas
import os
import ast


def key_press_timer(key):
    clock = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP and event.key == key:
                return int(chr(key)) - 1, (pygame.time.get_ticks() - clock) // 1000


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

    else:
        if file_size != 0:
            if check_if_header_in_csv(key_pressed):
                data_frame = pandas.read_csv("CSV/CSV_data.csv")
                data_list = []
                for row in data_frame[str(key_pressed)]:
                    data_list.append(ast.literal_eval(row))
                curr_file[key_pressed] = data_list

                MineField.create_mine_field_from_saved_files(curr_file)
                return True
    return False


def check_if_header_in_csv(header):
    header_list = pandas.read_csv("CSV/CSV_data.csv", nrows=0).columns.tolist()
    return str(header) in header_list
