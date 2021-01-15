from src.Field import Field
import copy
import random


def generate_initial_grid():
    initial_grid = [[i for i in range(1, Field.SIZE + 1)] for _ in range(Field.SIZE)]
    for i in range(Field.BLOCK_SIZE):
        for j in range(Field.BLOCK_SIZE):
            ind_row = i * Field.BLOCK_SIZE + j
            shift = j * Field.BLOCK_SIZE + i
            initial_grid[ind_row] = initial_grid[ind_row][shift:] + initial_grid[ind_row][0:shift]
    return initial_grid

def transpose(grid):
    grid[:] = [list(row) for row in zip(*grid)]

def swap_rows(grid):
    block = random.randint(0, 2)
    row1 = block * Field.BLOCK_SIZE + random.randint(0, 2)
    row2 = block * Field.BLOCK_SIZE + random.randint(0, 2)
    grid[row1], grid[row2] = grid[row2], grid[row1]

def swap_blocks(grid):
    block1 = random.randint(0, 2)
    block2 = random.randint(0, 2)
    slice1 = slice(block1 * Field.BLOCK_SIZE, block1 * Field.BLOCK_SIZE + Field.BLOCK_SIZE)
    slice2 = slice(block2 * Field.BLOCK_SIZE, block2 * Field.BLOCK_SIZE + Field.BLOCK_SIZE)
    grid[slice1], grid[slice2] = grid[slice2], grid[slice1]

random_functions = [transpose, swap_blocks, swap_rows]

def generate_field(num_missed):
    n_iters = 100
    grid = generate_initial_grid()
    for i in range(n_iters):
        random_functions[random.randint(0, 2)](grid)
    answer = copy.deepcopy(grid)
    for miss in random.sample(range(Field.SIZE * Field.SIZE), k=num_missed):
        grid[miss // Field.SIZE][miss % Field.SIZE] = '.'
    return Field(grid), Field(answer)



