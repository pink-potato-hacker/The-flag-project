import Consts
import random

mine_field = []
mines = [[] for n in range(20)]
grass = []

# change for loop
def create_empty_mine_field():
    global mine_field
    mine_field = [[Consts.EMPTY for col in range(Consts.NUMBER_OF_COLUMNS)] for row in range(Consts.NUMBER_OF_ROWS)]

def randomize_mines():

    for mine_index in range(20):
        rnd_row = random.randint(0, 24)
        rnd_col = random.randint(0, 46)
        mines[mine_index].append(rnd_row)

        for i in range(3):
            mine_field[rnd_row][rnd_col + i] = Consts.MINES
            mines[mine_index].append(rnd_col + i)

def randomize_grass():
    for grass_index in range(20):
        rnd_x = random.randint(0, Consts.NUMBER_OF_COLUMNS * 25)
        rnd_y = random.randint(0, Consts.NUMBER_OF_ROWS * 25)
        grass.append((rnd_x, rnd_y))
def put_flag():
    pass


create_empty_mine_field()
randomize_mines()
randomize_grass()
print(grass)
