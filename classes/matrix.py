class Matrix:
    def __init__(self, _pygame, block_size, max_x):
        self.obj = _pygame.Surface((block_size*10+11, block_size*20+22))
        self.obj.fill((255, 255, 255))
        self.pos = ((max_x-(block_size*10+11))/2, 15)

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
