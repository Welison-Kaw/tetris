from my_functions import *


def test_collision():
    assert True


def test_tetrimino_giver():
    tetrimino = tetrimino_giver(0)
    assert (tetrimino == ([255, 255, 0], [[1, 1], [1, 1]]))


def test_move_right():
    position_x = 9
    position_y = 0
    shape = [[1, 1], [1, 1]]

    if not collision(tetrimino_mover(reshape(shape), position_x + 1, position_y), WALL):
        position_x += 1
    assert(position_x == 9)

    position_x = 8
    if not collision(tetrimino_mover(reshape(shape), position_x + 1, position_y), WALL):
        position_x += 1
    assert(position_x == 8)

    position_x = 7
    if not collision(tetrimino_mover(reshape(shape), position_x + 1, position_y), WALL):
        position_x += 1
    assert(position_x == 8)

    position_y = 10
    position_x = 7
    if not collision(tetrimino_mover(reshape(shape), position_x + 1, position_y), WALL):
        position_x += 1
    assert(position_x == 8)


def test_move_left():
    position_x = 0
    position_y = 0
    shape = [[1, 1], [1, 1]]
    if not collision(tetrimino_mover(reshape(shape), position_x - 1, position_y), WALL):
        position_x -= 1
    assert(position_x == 0)

    position_x = 1
    if not collision(tetrimino_mover(reshape(shape), position_x - 1, position_y), WALL):
        position_x -= 1
    assert(position_x == 0)

    position_x = 2
    if not collision(tetrimino_mover(reshape(shape), position_x - 1, position_y), WALL):
        position_x -= 1
    assert(position_x == 1)

    position_x = 2
    position_y = 10
    if not collision(tetrimino_mover(reshape(shape), position_x - 1, position_y), WALL):
        position_x -= 1
    assert(position_x == 1)
