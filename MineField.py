import Consts
import random

mine_field = []
def create_empty_mine_field():
    global mine_field
    mine_field = [[Consts.EMPTY for col in range(Consts.NUMBER_OF_COLUMNS)] for row in range(Consts.NUMBER_OF_ROWS)]

def randomize_mines():
    global mine_field
    for rand in range(20):
        rnd_row = random.randint(0, 24)
        rnd_col = random.randint(0, 49)
        mine_field[rnd_row][rnd_col] = Consts.MINES




