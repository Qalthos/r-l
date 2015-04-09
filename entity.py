import random

import tdl


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


class Player(Entity):
    """Entity representing the player's character."""

    def handle_key(self, event):
        if event.keychar in ['UP', 'DOWN', 'LEFT', 'RIGHT', 'h', 'j', 'k', 'l']:
            dx, dy = 0, 0
            if event.keychar in ['UP', 'k']:
                dy = -1
            elif event.keychar in ['LEFT', 'h']:
                dx = -1
            elif event.keychar in ['DOWN', 'j']:
                dy = 1
            elif event.keychar in ['RIGHT', 'l']:
                dx = 1

            self._move(self.x+dx, self.y+dy)

    def move(self):
        self.handle_key(tdl.event.keyWait())


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
