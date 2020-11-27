from classes.matrix import Matrix
from classes.tetrimino import Tetrimino
import pygame


def test_collision():
    assert True


def test_tetrimino_giver():
    tetrimino = Tetrimino(0)
    assert (tetrimino.color == [255, 255, 0])
    assert tetrimino.shape == [[1, 1], [1, 1]]


def test_tetrimino_move():
    tetrimino = Tetrimino(2)
    assert tetrimino.position() == [[4, 0], [3, 1], [4, 1], [5, 1]]
    tetrimino.move_right()
    assert tetrimino.position() == [[5, 0], [4, 1], [5, 1], [6, 1]]
    tetrimino.move_right()
    assert tetrimino.position() == [[6, 0], [5, 1], [6, 1], [7, 1]]
    tetrimino.move_left()
    assert tetrimino.position() == [[5, 0], [4, 1], [5, 1], [6, 1]]
    tetrimino.move_right()
    tetrimino.move_right()
    tetrimino.move_right()
    tetrimino.move_right()
    tetrimino.move_right()
    tetrimino.move_right()
    assert tetrimino.position() == [[8, 0], [7, 1], [8, 1], [9, 1]]


def test_ghost_position():
    matrix = Matrix(pygame, 20, 400)

    matrix.cell[9][19].color = (0xFF, 0xFF, 0x00)
    matrix.cell[8][19].color = (0xFF, 0xFF, 0x00)
    matrix.cell[9][18].color = (0xFF, 0xFF, 0x00)
    matrix.cell[8][18].color = (0xFF, 0xFF, 0x00)

    tetrimino = Tetrimino(2)
    tetrimino.move_right()
    tetrimino.move_right()
    tetrimino.move_right()
    tetrimino.move_right()
    tetrimino.move_right()
    tetrimino.move_right()

    print("\n.{}".format(tetrimino.position()))
    print("\n.{}".format(tetrimino.ghost_position()))

    assert tetrimino.ghost_position() == [[8, 16], [7, 17], [8, 17], [9, 17]]

    pass
