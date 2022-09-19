import Consts
import MineField
import random
import Screen

teleports = [[] for n in range(Consts.NUMBER_OF_TELEPORTS)]

"""
This function will randomize the indexes of the teleports in the matrix.
"""


def randomize_teleports():
    for tel_index in range(Consts.NUMBER_OF_TELEPORTS):
        rnd_row = random.randint(4, 20)
        rnd_col = random.randint(0, 46)

        while MineField.mine_field[rnd_row][rnd_col] != Consts.EMPTY:
            rnd_row = random.randint(3, 24)
            rnd_col = random.randint(0, 46)

        teleports[tel_index].append(rnd_row)

        for n in range(3):
            MineField.mine_field[rnd_row][rnd_col + n] = Consts.TELEPORTS
            teleports[tel_index].append(rnd_col + n)


"""
This function will check it the player have stepped on a teleport.
:param coord_x: the x coordinate of the soldier
:param coord_y: the y coordinate of the soldier
:type coord_x: float
:type coord_y: float
:return 0: if nothing happened
:return 1: if the player have stepped on a teleport
:rtype 0,1: int
"""


def step_on_teleport(coord_x, coord_y):
    if MineField.mine_field[coord_y // Consts.SIZE + 3][coord_x // Consts.SIZE] == Consts.TELEPORTS or \
            MineField.mine_field[coord_y // Consts.SIZE + 3][coord_x // Consts.SIZE + 1] == Consts.TELEPORTS:
        return 1
    return 0


"""
This function will pick randomly to which teleport the player teleports.
:param coord_x: the x coordinate of the soldier
:param coord_y: the y coordinate of the soldier
:type coord_x: float
:type coord_y: float
:return random_teleport: list of indexes of the teleport
:rtype random_teleport: list
"""


def pick_teleport(coord_x, coord_y):
    random_teleport = random.choice(teleports)

    while True:
        if random_teleport[0] == coord_y // Consts.SIZE + 3:
            for i in range(1, 4):
                if random_teleport[i] == coord_y // Consts.SIZE + 3:
                    random_teleport = random.choice(teleports)
        else:
            random_teleport[0] = random_teleport[0] - 1
            break

    return random_teleport
