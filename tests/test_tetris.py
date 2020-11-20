from myFunctions import tetrimino_giver


def test_collision():
    print("\n.abc")
    assert True


def test_tetrimino_giver():
    tetrimino = tetrimino_giver(0)
    assert (tetrimino == ([255, 255, 0], [[1, 1], [1, 1]]))
