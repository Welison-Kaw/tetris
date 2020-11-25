from my_constants import *


def grid_position(t):
    return t[0] * BLOCK_SIZE + t[0] + 1, t[1] * BLOCK_SIZE + t[1] + 2


# transforma numa estrutura que o pygame consiga escrever
def reshape(old_shape):
    r = []
    for i in range(len(old_shape)):
        for j in (range(len(old_shape[i]))):
            if old_shape[i][j] == 1:
                r.append([j, i])
    return r
