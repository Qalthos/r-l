import random


class Entity(object):

    def __init__(self, x, y, char, parent):
        self.x = x
        self.y = y
        self.char = char
        self.parent = parent

    def draw(self, window):
        window.drawChar(self.x, self.y, self.char)

class Walker(Entity):

    def move(self):
        vector = random.randrange(4)
        direction = vector & 1
        magnitude = (vector >> 1 & 1) * 2 - 1

        # Change the location
        delta = [self.x, self.y]
        delta[direction] += magnitude
        self.x, self.y = delta
