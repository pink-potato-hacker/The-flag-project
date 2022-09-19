import Consts
import random
import Screen
import copy

mine_field = []
mines = [[] for n in range(Consts.NUMBER_OF_MINES)]
grass = []
bushes = []
flowers = []

def create_mine_field_from_saved_files(saved_dict):
    saved_list = list(saved_dict.values())
    mines = saved_list[0][0]
    flowers = saved_list[0][1]
    bushes = saved_list[0][2]
    grass = saved_list[0][3]
    soldier_location = saved_list[0][4]

    for row in range(len(mine_field)):
        for col in range(len(mine_field[0])):
            if mine_field[row][col] != Consts.EMPTY:
                mine_field[row][col] = Consts.EMPTY

    for mine_index in range(Consts.NUMBER_OF_MINES):
        for i in range(1, 4):
            mine_field[mines[mine_index][0]][mines[mine_index][i]] = Consts.MINES

    for position in range(len(soldier_location)):  # [[1,2],[3,4]]
        if position < 6:
            mine_field[soldier_location[position][0]][soldier_location[position][1]] = Consts.SOLIDER_BODY
        else:
            mine_field[soldier_location[position][0]][soldier_location[position][1]] = Consts.SOLIDER_LEGS

    put_flag()

def create_empty_mine_field():
    for i in range(Consts.NUMBER_OF_ROWS):
        row = []
        for col in range(Consts.NUMBER_OF_COLUMNS):
            row.append(Consts.EMPTY)
        mine_field.append(row)


def randomize_mines():
    for mine_index in range(Consts.NUMBER_OF_MINES):
        rnd_row = random.randint(3, 24)
        rnd_col = random.randint(0, 46)

        while (rnd_row <= 3 and rnd_col <= 1) or (rnd_row >= 22 and rnd_col >= 45):
            rnd_row = random.randint(3, 24)
            rnd_col = random.randint(0, 46)

        mines[mine_index].append(rnd_row)

        for i in range(3):
            mine_field[rnd_row][rnd_col + i] = Consts.MINES
            mines[mine_index].append(rnd_col + i)


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


def put_flag():
    for row in range(21, 24):
        for col in range(46, 50):
            mine_field[row][col] = Consts.FLAG


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

def get_soldier_location():
    soldier_location = []
    for x_index in range(len(mine_field)):
        for y_index in range(len(mine_field[0])):
            if mine_field[x_index][y_index] == Consts.SOLIDER_BODY:
                soldier_location.append((x_index, y_index))
            if mine_field[x_index][y_index] == Consts.SOLIDER_LEGS:
                soldier_location.append((x_index, y_index))
    return soldier_location

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

