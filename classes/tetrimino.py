from my_constants import *
from my_functions import *


class Tetrimino:
    def __init__(self, _type):
        self.type = _type
        self.x = 3
        self.y = 0
        # self.__color = get_color
        # self.__shape = get_shape

    def get_color(self):
        switcher = {
            O_SHAPE: [0xFF, 0xFF, 0x00],  # yellow
            I_SHAPE: [0x00, 0xBF, 0xFF],  # deep sky blue
            T_SHAPE: [0x80, 0x00, 0x80],  # purple
            L_SHAPE: [0xFF, 0xA5, 0x00],  # orange
            J_SHAPE: [0x1E, 0x32, 0xFF],  # blue
            S_SHAPE: [0x00, 0x80, 0x00],  # green
            Z_SHAPE: [0xFF, 0x00, 0x00]   # red
        }
        return switcher.get(self.type, "Invalid Shape")

    def get_shape(self):
        switcher = {
            O_SHAPE: [[1, 1],
                      [1, 1]],
            I_SHAPE: [[0, 0, 0, 0],
                      [1, 1, 1, 1],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]],
            T_SHAPE: [[0, 1, 0],
                      [1, 1, 1],
                      [0, 0, 0]],
            L_SHAPE: [[0, 0, 1],
                      [1, 1, 1],
                      [0, 0, 0]],
            J_SHAPE: [[1, 0, 0],
                      [1, 1, 1],
                      [0, 0, 0]],
            S_SHAPE: [[0, 1, 1],
                      [1, 1, 0],
                      [0, 0, 0]],
            Z_SHAPE: [[1, 1, 0],
                      [0, 1, 1],
                      [0, 0, 0]]
        }
        return switcher.get(self.type, "Invalid Shape")

    def position(self):
        r = reshape(self.get_shape())
        for i in range(len(r)):
            r[i][0] += self.x
            r[i][1] += self.y
        return r

    def collision(self, target):
        if target == WALL:
            for i in range(len(self.position())):
                if self.position()[i][0] < 0 or self.position()[i][0] > 9:
                    return self.position()[i][0]
        return False

    def move_right(self):
        self.x += 1
        if self.collision(WALL):
            self.x -= 1

    def move_left(self):
        self.x -= 1
        if self.collision(WALL):
            self.x += 1
