from myConstants import *


def collision(object, target):
    if target == WALL:
        for i in range(len(object)):
            if object[i][0] < 0 or object[i][0] > 9:
                return object[i][0]
    return False


def grid_position(t):
    return t[0] * BLOCK_SIZE + t[0] + 1, t[1] * BLOCK_SIZE + t[1] + 2


def tetrimino_mover(_shape, _column, _line):
    for i in range(len(_shape)):
        _shape[i][0] += _column
        _shape[i][1] += _line
    return _shape


def tetrimino_rotator(_shape, _direction):
    size = len(_shape)
    r = [[0 for j in range(size)] for i in range(size)]
    for i in range(len(_shape)):
        for j in (range(len(_shape[i]))):
            if _shape[i][j] == 1:
                r[j][abs(i - size + 1)] = 1
    return r


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


# temp name
def tetrimino_giver(_type):
    # shape = north facing
    color = []
    shape = []

    if _type == O_SHAPE:
        color = [255, 255, 0]  # yellow
        shape = [
            [1, 1],
            [1, 1]
        ]

    if _type == I_SHAPE:
        color = [0, 191, 255]  # deep sky blue
        shape = [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

    if _type == T_SHAPE:
        color = [128, 0, 128]  # purple
        shape = [
            [0, 1, 0],
            [1, 1, 1],
            [0, 0, 0]
        ]

    if _type == L_SHAPE:
        color = [255, 165, 0]  # orange
        shape = [
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0]
        ]

    if _type == J_SHAPE:
        color = [30, 50, 255]  # blue
        shape = [
            [1, 0, 0],
            [1, 1, 1],
            [0, 0, 0]
        ]

    if _type == S_SHAPE:
        color = [0, 128, 0]  # green
        shape = [
            [0, 1, 1],
            [1, 1, 0],
            [0, 0, 0]
        ]

    if _type == Z_SHAPE:
        color = [255, 0, 0]  # red
        shape = [
            [1, 1, 0],
            [0, 1, 1],
            [0, 0, 0]
        ]

    return color, shape
