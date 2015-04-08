class Entity(object):

    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.char = char

    def draw(self, window):
        window.drawChar(self.x, self.y, self.char)
