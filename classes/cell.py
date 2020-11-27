class Cell:
    def __init__(self, _pygame, block_size):
        self.block = _pygame.Surface((block_size, block_size))
        self.color = (0, 0, 0)

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color
        self.block.fill(color)
