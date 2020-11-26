from classes.tetrimino import Tetrimino


def test_collision():
    assert True


def test_tetrimino_giver():
    tetrimino = Tetrimino(0)
    assert (tetrimino.get_color() == [255, 255, 0])
    assert tetrimino.get_shape() == [[1, 1], [1, 1]]


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
