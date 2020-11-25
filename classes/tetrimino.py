from my_constants import *


class Tetrimino:
    def __init__(self, _type):
        self.type = _type
        self.x = 3
        self.y = 0
        switcher = {
            O_SHAPE: [0xFF, 0xFF, 0x00],  # yellow
            I_SHAPE: [0x00, 0xBF, 0xFF],  # deep sky blue
            T_SHAPE: [0x80, 0x00, 0x80],  # purple
            L_SHAPE: [0xFF, 0xA5, 0x00],  # orange
            J_SHAPE: [0x1E, 0x32, 0xFF],  # blue
            S_SHAPE: [0x00, 0x80, 0x00],  # green
            Z_SHAPE: [0xFF, 0x00, 0x00]   # red
        }
        self.color = switcher.get(_type, "Invalid Shape")
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
        self.shape = switcher.get(self.type, "Invalid Shape")

    def get_color(self):
        return self.color

    def get_shape(self):
        return self.shape

    def position(self):
        r = []
        for i in range(len(self.shape)):
            for j in (range(len(self.shape[i]))):
                if self.shape[i][j] == 1:
                    r.append([j, i])
        # r = reshape(self.get_shape())
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

    def rotate(self):
        size = len(self.shape)
        r = [[0 for j in range(size)] for i in range(size)]
        for i in range(len(self.shape)):
            for j in (range(len(self.shape[i]))):
                if self.shape[i][j] == 1:
                    r[j][abs(i - size + 1)] = 1
        self.shape = r

        collision_point = self.collision(WALL)
        if collision_point < 0:
            self.x = 0
        if collision_point > 9:
            self.x = 10-len(self.shape)

    def ghost_position(self):
        ghost_shape = self.position().copy()

        while ghost_shape[3][1] < 19:
            for i in range(len(ghost_shape)):
                ghost_shape[i][1] += 1

        return ghost_shape
