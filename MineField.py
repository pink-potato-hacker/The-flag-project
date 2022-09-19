import Consts
import random
import Screen

mine_field = []
mines = [[] for n in range(Consts.NUMBER_OF_MINES)]
grass = []
bushes = []
flowers = []
soldier_locations = []


"""
This function will load a saved game.
:param saved_dict: a dictionary that contains the coordinates/indexes of these elements in order:
mines, flowers, bushes, grass, soldier locations and teleports.
:type saved_dict: dict
"""


def load(saved_dict):
    global flowers, bushes, grass, mines, soldier_locations

    saved_list = list(saved_dict.values())
    mines = saved_list[0][0]
    flowers = saved_list[0][1]
    bushes = saved_list[0][2]
    grass = saved_list[0][3]
    soldier_locations = saved_list[0][4]

    for row in range(len(mine_field)):
        for col in range(len(mine_field[0])):
            if mine_field[row][col] != Consts.EMPTY:
                mine_field[row][col] = Consts.EMPTY

    for mine_index in range(Consts.NUMBER_OF_MINES):
        for i in range(1, 4):
            mine_field[mines[mine_index][0]][mines[mine_index][i]] = Consts.MINES

    for position in range(len(soldier_locations)):
        if position < 6:
            mine_field[soldier_locations[position][0]][soldier_locations[position][1]] = Consts.SOLIDER_BODY
        else:
            mine_field[soldier_locations[position][0]][soldier_locations[position][1]] = Consts.SOLIDER_LEGS

    put_flag()


"""
This function will create an empty 'mine field' matrix.
"""


def create_empty():
    for i in range(Consts.NUMBER_OF_ROWS):
        row = []
        for col in range(Consts.NUMBER_OF_COLUMNS):
            row.append(Consts.EMPTY)
        mine_field.append(row)


"""
This function will randomize the indexes of the mines in the matrix.
"""


def randomize_mines():
    for mine_index in range(Consts.NUMBER_OF_MINES):
        rnd_row = random.randint(3, 24)
        rnd_col = random.randint(0, 46)

        while (rnd_row <= 3 and rnd_col <= 1) or (rnd_row >= 22 and rnd_col >= 45):
            rnd_row = random.randint(3, 24)
            rnd_col = random.randint(0, 46)

        mines[mine_index].append(rnd_row)

        for i in range(Consts.TRAP_LENGTH):
            mine_field[rnd_row][rnd_col + i] = Consts.MINES
            mines[mine_index].append(rnd_col + i)


"""
This function will set the coordinates of the flowers, bushes and grass on surface.
"""


def get_cords_for_elements():
    for bush_index in range(Consts.NUMBER_OF_BUSHES):
        rnd_x = random.randint(0, Consts.NUMBER_OF_COLUMNS * Consts.SIZE)
        rnd_y = random.randint(0, Consts.NUMBER_OF_ROWS * Consts.SIZE)
        bushes.append((rnd_x, rnd_y))

    for grass_index in range(Consts.NUMBER_OF_GRASS):
        rnd_x = random.randint(0, Consts.NUMBER_OF_COLUMNS * Consts.SIZE)
        rnd_y = random.randint(0, Consts.NUMBER_OF_ROWS * Consts.SIZE)
        grass.append((rnd_x, rnd_y))

    for flower_index in range(Consts.NUMBER_OF_FLOWERS):
        rnd_x = random.randint(0, Consts.NUMBER_OF_COLUMNS * Consts.SIZE)
        rnd_y = random.randint(0, Consts.NUMBER_OF_ROWS * Consts.SIZE)
        flowers.append((rnd_x, rnd_y))


"""
This function will put the flag in the matrix.
"""


def put_flag():
    for row in range(21, 24):
        for col in range(46, 50):
            mine_field[row][col] = Consts.FLAG


"""
This function will put the soldier in the matrix with the given coordinates
:param coord_x: the x coordinate of the soldier
:param coord_y: the y coordinate of the soldier
:type coord_x: float
:type coord_y: float
"""


def put_solider_in_matrix(coord_x, coord_y):
    col = coord_x // Consts.SIZE
    row = coord_y // Consts.SIZE

    for x_index in range(len(mine_field)):
        for y_index in range(len(mine_field[0])):
            if (mine_field[x_index][y_index] == Consts.SOLIDER_BODY) or (
                    mine_field[x_index][y_index] == Consts.SOLIDER_LEGS):
                mine_field[x_index][y_index] = Consts.EMPTY

    for i in range(4):
        if mine_field[row + i][col] != Consts.MINES and mine_field[row + i][col + 1] != Consts.MINES:
            if mine_field[row + i][col] != Consts.FLAG and mine_field[row + i][col + 1] != Consts.FLAG:
                mine_field[row + i][col] = Consts.SOLIDER_BODY
                mine_field[row + i][col + 1] = Consts.SOLIDER_BODY
            if i == 3:
                mine_field[row + i][col] = Consts.SOLIDER_LEGS
                mine_field[row + i][col + 1] = Consts.SOLIDER_LEGS


"""
This function will return the current position of the soldier in matrix.
:return soldier_location: list of tuples of soldier's position in matrix.
:rtype 0,1,soldier_location: list
"""


def get_soldier_location():
    soldier_location = []
    for x_index in range(len(mine_field)):
        for y_index in range(len(mine_field[0])):
            if mine_field[x_index][y_index] == Consts.SOLIDER_BODY:
                soldier_location.append((x_index, y_index))
            if mine_field[x_index][y_index] == Consts.SOLIDER_LEGS:
                soldier_location.append((x_index, y_index))
    return soldier_location


"""
This function will check if the player has won the game or lost it.
:param coord_x: the x coordinate of the soldier
:param coord_y: the y coordinate of the soldier
:type coord_x: float
:type coord_y: float
:return 0: if nothing happened
:return 1: if the player has lost the game
:return 2: if the player has won the game
:rtype 0,1,2: int
"""


def win_or_lose(coord_x, coord_y):
    # 1 - Lose, 2 - Win
    if mine_field[coord_y // Consts.SIZE + 3][coord_x // Consts.SIZE] == Consts.MINES or \
            mine_field[coord_y // Consts.SIZE + 3][coord_x // Consts.SIZE + 1] == Consts.MINES:
        Screen.show_boom((coord_x - Consts.SIZE, coord_y + Consts.SIZE))
        return 1

    elif (coord_y // Consts.SIZE + 1 == 22 and coord_x // Consts.SIZE + 1 == 47) or \
            (coord_y // Consts.SIZE + 1 == 22 and coord_x // Consts.SIZE + 1 == 48) or \
            (coord_y // Consts.SIZE + 1 == 21 and coord_x // Consts.SIZE + 1 == 47) or \
            (coord_y // Consts.SIZE + 1 == 21 and coord_x // Consts.SIZE + 1 == 48):
        return 2

    elif (coord_y // Consts.SIZE + 1 == 22 and coord_x // Consts.SIZE == 47) or \
            (coord_y // Consts.SIZE + 1 == 22 and coord_x // Consts.SIZE == 48) or \
            (coord_y // Consts.SIZE + 1 == 21 and coord_x // Consts.SIZE == 47) or \
            (coord_y // Consts.SIZE + 1 == 21 and coord_x // Consts.SIZE == 48):
        return 2

    return 0
