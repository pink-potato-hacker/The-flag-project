import MineField
import Teleport
import pandas
import os
import ast
import Guard

save_files = {}
curr_file = {}


"""
This function will add/remove data from the csv file according to the examinations.
:param key_and_time_key_pressed: the key that the player has pressed and the time he held it for.
:type key_and_time_key_pressed: tuple
:return True: if none of the data have changed.
:return False: if some of the data have changed.
:rtype True, False: boolean
"""


def add_to_file(key_and_time_key_pressed):
    global save_files, curr_file

    key_pressed, time_pressed = key_and_time_key_pressed
    file_size = os.path.getsize("CSV/CSV_data.csv")

    if time_pressed <= 1:
        if file_size == 0:  # file empty
            save_files[key_pressed] = [MineField.mines,
                                       MineField.flowers,
                                       MineField.bushes,
                                       MineField.grass,
                                       MineField.get_soldier_location(),
                                       Teleport.teleports,
                                       Guard.get_guard_location()]
            data_frame = pandas.DataFrame(save_files)
            data_frame.to_csv("CSV/CSV_data.csv", index=False)

        elif not check_for_header(key_pressed):  # file doesn't contain the given header
            data_frame = pandas.read_csv("CSV/CSV_data.csv")
            data_frame[key_pressed] = [MineField.mines,
                                       MineField.flowers,
                                       MineField.bushes,
                                       MineField.grass,
                                       MineField.get_soldier_location(),
                                       Teleport.teleports,
                                       Guard.get_guard_location()]
            data_frame.to_csv("CSV/CSV_data.csv", index=False)

        elif check_for_header(key_pressed):  # file contains the given header
            data_frame = pandas.read_csv("CSV/CSV_data.csv")
            data_frame.drop(str(key_pressed), inplace=True, axis=1)
            data_frame[key_pressed] = [MineField.mines,
                                       MineField.flowers,
                                       MineField.bushes,
                                       MineField.grass,
                                       MineField.get_soldier_location(),
                                       Teleport.teleports,
                                       Guard.get_guard_location()]
            data_frame.to_csv("CSV/CSV_data.csv", index=False)

    else:
        if file_size != 0:
            if check_for_header(key_pressed):
                data_frame = pandas.read_csv("CSV/CSV_data.csv")
                data_list = []

                for row in data_frame[str(key_pressed)]:
                    data_list.append(ast.literal_eval(row))

                curr_file[key_pressed] = data_list
                MineField.load(curr_file)
                Teleport.load_tels(curr_file)
                Guard.load_guard(curr_file)
                curr_file = {}

                return True

    save_files = {}
    return False


"""
This function will check if the given header exists in the csv file.
:param header: the key that the player has pressed. 
:type header: int
:return str(header) in header_list: True if the header exists, else - False.
:rtype str(header) in header_list: boolean
"""


def check_for_header(header):
    header_list = pandas.read_csv("CSV/CSV_data.csv", nrows=0).columns.tolist()
    return str(header) in header_list
