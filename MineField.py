import Consts
import random

mine_field = []


def create_empty_mine_field():
    global mine_field
    mine_field = [[Consts.EMPTY for col in range(Consts.NUMBER_OF_COLUMNS)] for row in range(Consts.NUMBER_OF_ROWS)]


def randomize_mines():
    for rand in range(21):
        rnd_row = random.randint(0, 24)
        rnd_col = random.randint(0, 49)
        for i in range(3):
            mine_field[rnd_row][rnd_col + i] = Consts.MINES


def put_flag():
    pass


create_empty_mine_field()
randomize_mines()
print(mine_field)
