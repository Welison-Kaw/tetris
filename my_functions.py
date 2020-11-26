from my_constants import BLOCK_SIZE


def grid_position(t):
    return t[0] * BLOCK_SIZE + t[0] + 1, t[1] * BLOCK_SIZE + t[1] + 2
