import Consts
import random
import Screen

mine_field = []
mines = [[] for n in range(20)]
grass = []
bushes = []
flower = []


def create_empty_mine_field():
    global mine_field

    for i in range(Consts.NUMBER_OF_ROWS):
        row = []
        for col in range(Consts.NUMBER_OF_COLUMNS):
            row.append(Consts.EMPTY)
        mine_field.append(row)


def randomize_mines():
    for mine_index in range(20):
        rnd_row = random.randint(3, 24)
        rnd_col = random.randint(0, 46)

        while (rnd_row <= 3 and rnd_col <= 2) or (rnd_row >= 22 and rnd_col >= 45):
            rnd_row = random.randint(3, 24)
            rnd_col = random.randint(0, 46)

        mines[mine_index].append(rnd_row)

        for i in range(3):
            mine_field[rnd_row][rnd_col + i] = Consts.MINES
            mines[mine_index].append(rnd_col + i)


def randomize_bushes():
    for grass_index in range(20):
        rnd_x = random.randint(0, Consts.NUMBER_OF_COLUMNS * 25)
        rnd_y = random.randint(0, Consts.NUMBER_OF_ROWS * 25)
        bushes.append((rnd_x, rnd_y))


def randomize_grass():
    for grass_index in range(10):
        rnd_x = random.randint(0, Consts.NUMBER_OF_COLUMNS * 25)
        rnd_y = random.randint(0, Consts.NUMBER_OF_ROWS * 25)
        grass.append((rnd_x, rnd_y))


def randomize_flower():
    for flower_index in range(20):
        rnd_x = random.randint(0, Consts.NUMBER_OF_COLUMNS * 25)
        rnd_y = random.randint(0, Consts.NUMBER_OF_ROWS * 25)
        flower.append((rnd_x, rnd_y))


def put_flag():
    for row in range(21, 25):
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


def win_or_lose(coord_x, coord_y):
    # 1 - Lose, 2 - Win
    if mine_field[coord_y // Consts.SIZE + 3][coord_x // Consts.SIZE] == Consts.MINES or \
            mine_field[coord_y // Consts.SIZE + 3][coord_x // Consts.SIZE + 1] == Consts.MINES:
        Screen.show_boom((coord_x - Consts.SIZE, coord_y + Consts.SIZE))
        return 1

    elif mine_field[coord_y // Consts.SIZE][coord_x // Consts.SIZE] == Consts.FLAG and \
            mine_field[coord_y // Consts.SIZE][coord_x // Consts.SIZE + 1] == Consts.FLAG:
        return 2

    return 0
