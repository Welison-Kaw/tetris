class Matrix:
    def __init__(self, _pygame, block_size, max_x):
        self.__block_size = block_size
        self.obj = _pygame.Surface((self.__block_size*10+11, self.__block_size*20+22))
        self.obj.fill((255, 255, 255))
        self.pos = ((max_x-(self.__block_size*10+11))/2, 15)

    @property
    def obj(self):
        return self.__obj

    @obj.setter
    def obj(self, obj):
        self.__obj = obj

    @property
    def pos(self):
        return self.__pos

    @pos.setter
    def pos(self, pos):
        self.__pos = pos

    def grid_position(self, t):
        return t[0] * self.__block_size + t[0] + 1, t[1] * self.__block_size + t[1] + 2
