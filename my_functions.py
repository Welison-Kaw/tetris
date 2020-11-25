from my_constants import *


def grid_position(t):
    return t[0] * BLOCK_SIZE + t[0] + 1, t[1] * BLOCK_SIZE + t[1] + 2


def tetrimino_mover(_shape, _column, _line):
    for i in range(len(_shape)):
        _shape[i][0] += _column
        _shape[i][1] += _line
    return _shape


# transforma numa estrutura que o pygame consiga escrever
def reshape(old_shape):
    r = []
    for i in range(len(old_shape)):
        for j in (range(len(old_shape[i]))):
            if old_shape[i][j] == 1:
                r.append([j, i])
    return r


# cria a sombra da peça
def ghost_position(_shape):
    ghost_shape = _shape.copy()

    while ghost_shape[3][1] < 19:
        for i in range(len(ghost_shape)):
            ghost_shape[i][1] += 1

    return ghost_shape
