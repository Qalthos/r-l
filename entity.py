import random


class Entity(object):

    def __init__(self, x, y, char, parent):
        self.x = x
        self.y = y
        self.char = char
        self.parent = parent

    def draw(self):
        self.parent.console.drawChar(self.x, self.y, self.char)

    def move(self):
        raise NotImplementedError

    def _move(self, x, y):
        if self.parent.check_move(x, y):
            self.x, self.y = x, y


class Walker(Entity):
    """This is an Entity that wanders around randomly."""

    def move(self):
        vector = random.randrange(4)
        direction = vector & 1
        magnitude = (vector >> 1 & 1) * 2 - 1

        # Change the location
        new_location = [self.x, self.y]
        new_location[direction] += magnitude

        self._move(*new_location)
