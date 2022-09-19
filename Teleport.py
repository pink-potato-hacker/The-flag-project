import Consts
import MineField
import random

teleports = []

"""
This function will randomize the indexes of the teleports in the matrix.
"""


def randomize_teleports():
    for tel_index in range(Consts.NUMBER_OF_TELEPORTS):
        rnd_row = random.randint(4, 20)
        rnd_col = random.randint(0, 46)

        while (rnd_row <= 3 and rnd_col <= 1) or (rnd_row >= 22 and rnd_col >= 45):
            rnd_row = random.randint(3, 24)
            rnd_col = random.randint(0, 46)

        teleports[tel_index].append(rnd_row)

        for i in range(3):
            teleports[rnd_row][rnd_col + i] = Consts.MINES
            teleports[tel_index].append(rnd_col + i)
